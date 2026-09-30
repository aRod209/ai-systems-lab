import json
from unittest.mock import patch

import pytest

from ai_systems_lab.cli import Cli


class TestCli:
    def test_run_sends_entered_prompt_to_service(self):
        # arrange
        question = 'What is the paper about?'
        with patch('ai_systems_lab.cli.ResearchPaperService') as mock_service_class, \
                patch('builtins.input', return_value=question) as mock_input:
            mock_service_class.return_value.prompt.return_value = {'answer': 'Test answer'}
            cli = Cli()

            # act
            cli.run()

            # assert
            mock_input.assert_called_once_with()
            mock_service_class.return_value.prompt.assert_called_once_with(question)

    def test_run_reprompts_until_input_is_nonempty(self, capsys):
        # arrange
        question = 'What is the paper about?'
        with patch('ai_systems_lab.cli.ResearchPaperService') as mock_service_class, \
                patch('builtins.input', side_effect=['', '   ', question]) as mock_input:
            mock_service_class.return_value.prompt.return_value = {'answer': 'Test answer'}
            cli = Cli()

            # act
            cli.run()

            # assert
            assert mock_input.call_count == 3
            mock_service_class.return_value.prompt.assert_called_once_with(question)
            assert capsys.readouterr().out.count('Enter your prompt about a research paper:') == 3

    def test_run_strips_whitespace_from_prompt(self):
        # arrange
        question = 'What is the paper about?'
        with patch('ai_systems_lab.cli.ResearchPaperService') as mock_service_class, \
                patch('builtins.input', return_value=f'   {question}   '):
            mock_service_class.return_value.prompt.return_value = {'answer': 'Test answer'}
            cli = Cli()

            # act
            cli.run()

            # assert
            mock_service_class.return_value.prompt.assert_called_once_with(question)

    def test_run_prints_service_response_as_indented_json(self, capsys):
        # arrange
        response = {'paper_name': 'Test Paper', 'answer': 'Test answer'}
        with patch('ai_systems_lab.cli.ResearchPaperService') as mock_service_class, \
                patch('builtins.input', return_value='test prompt'):
            mock_service_class.return_value.prompt.return_value = response
            cli = Cli()

            # act
            cli.run()

            # assert
            assert capsys.readouterr().out == (
                'Enter your prompt about a research paper:\n'
                f'{json.dumps(response, indent=2)}\n'
            )

    def test_close_closes_research_paper_service(self):
        # arrange
        with patch('ai_systems_lab.cli.ResearchPaperService') as mock_service_class:
            cli = Cli()

            # act
            cli.close()

            # assert
            mock_service_class.return_value.close.assert_called_once_with()

    def test_run_propagates_service_error(self):
        # arrange
        service_error = RuntimeError('Research paper request failed')
        with patch('ai_systems_lab.cli.ResearchPaperService') as mock_service_class, \
                patch('builtins.input', return_value='test prompt'):
            mock_service_class.return_value.prompt.side_effect = service_error
            cli = Cli()

            # act
            with pytest.raises(RuntimeError) as exc_info:
                cli.run()

            # assert
            assert exc_info.value is service_error
