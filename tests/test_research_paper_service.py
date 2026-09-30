import json
from unittest.mock import MagicMock, patch

from pydantic import ValidationError
import pytest

from ai_systems_lab.gemini_client import GeminiClient
from ai_systems_lab.research_paper_service import ResearchPaperService


class TestResearchPaperService:
    def test_prompt_returns_validated_research_paper_as_dictionary(self):
        # arrange
        paper_data = self.create_paper_data()
        json_paper_data = json.dumps(paper_data)
        mock_client = MagicMock(spec=GeminiClient)
        mock_client.send_request.return_value = json_paper_data
        service = ResearchPaperService(mock_client)

        # act
        actual = service.prompt("test prompt")

        # assert
        assert actual == paper_data

    def test_prompt_sends_the_provided_question_to_gemini_client(self):
        # arrange
        question = 'What is the paper about?'
        mock_client = MagicMock(spec=GeminiClient)
        mock_client.send_request.return_value = json.dumps(self.create_paper_data())
        service = ResearchPaperService(mock_client)

        # act
        service.prompt(question)

        # assert
        mock_client.send_request.assert_called_once_with(question)

    def test_prompt_raises_validation_error_for_invalid_json(self):
        # arrange
        paper_data = self.create_paper_data()
        json_paper_data = json.dumps(paper_data)
        json_paper_data = json_paper_data + '}'
        mock_client = MagicMock(spec=GeminiClient)
        mock_client.send_request.return_value = json_paper_data
        service = ResearchPaperService(mock_client)

        # act
        with pytest.raises(ValidationError) as exc_info:
            service.prompt('test prompt')

        error = exc_info.value.errors()[0]
                                        
        # assert
        assert error['loc'] == ()
        assert error['type'] == 'json_invalid'

    def test_prompt_raises_validation_error_for_missing_required_field(self):
        # arrange
        paper_data = self.create_paper_data()
        del paper_data['paper_name']
        mock_client = MagicMock(spec=GeminiClient)
        mock_client.send_request.return_value = json.dumps(paper_data)
        service = ResearchPaperService(mock_client)

        # act
        with pytest.raises(ValidationError) as exc_info:
            service.prompt('test prompt')

        # assert
        error = exc_info.value.errors()[0]
        assert error['loc'] == ('paper_name',)
        assert error['type'] == 'missing'

    def test_prompt_defaults_answer_to_none_when_omitted(self):
        # arrange
        paper_data = self.create_paper_data()
        del paper_data['answer']
        mock_client = MagicMock(spec=GeminiClient)
        mock_client.send_request.return_value = json.dumps(paper_data)
        service = ResearchPaperService(mock_client)

        # act
        response = service.prompt('test prompt')

        # assert
        assert response['answer'] is None

    def test_prompt_propagates_gemini_client_error(self):
        # arrange
        client_error = RuntimeError('Gemini request failed')
        mock_client = MagicMock(spec=GeminiClient)
        mock_client.send_request.side_effect = client_error
        service = ResearchPaperService(mock_client)

        # act
        with pytest.raises(RuntimeError) as exc_info:
            service.prompt('test prompt')

        # assert
        assert exc_info.value is client_error        

    def test_close_closes_client_created_by_service(self):
        # arrange
        with patch('ai_systems_lab.research_paper_service.GeminiClient') as mock_client_class:
            service = ResearchPaperService()

            # act
            service.close()

            # assert
            mock_client_class.assert_called_once_with()
            mock_client_class.return_value.close.assert_called_once_with()

    def test_close_does_not_close_injected_client(self):
        # arrange
        mock_client = MagicMock(spec=GeminiClient)
        service = ResearchPaperService(mock_client)

        # act
        service.close()

        # assert
        mock_client.close.assert_not_called()

    def create_paper_data(self):
        return {
                'paper_name': 'Test Paper',
                'authors': ['Test Author'],
                'pages': '1',
                'subfields': ['Machine Learning'],
                'answer': 'Test Answer'
            }