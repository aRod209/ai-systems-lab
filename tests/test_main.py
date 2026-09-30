from unittest.mock import patch

from google.genai.errors import APIError
from pydantic import TypeAdapter, ValidationError
import pytest

from ai_systems_lab.main import main


class TestMain:
    def test_main_runs_and_closes_cli(self):
        # arrange
        with patch('ai_systems_lab.main.Cli') as mock_cli_class:
            # act
            main()

            # assert
            mock_cli_class.assert_called_once_with()
            mock_cli_class.return_value.run.assert_called_once_with()
            mock_cli_class.return_value.close.assert_called_once_with()

    def test_main_closes_cli_when_run_raises(self):
        # arrange
        run_error = RuntimeError('CLI run failed')
        with patch('ai_systems_lab.main.Cli') as mock_cli_class:
            mock_cli_class.return_value.run.side_effect = run_error

            # act
            with pytest.raises(RuntimeError) as exc_info:
                main()

            # assert
            assert exc_info.value is run_error
            mock_cli_class.return_value.close.assert_called_once_with()

    def test_main_reports_validation_error(self):
        # arrange
        with pytest.raises(ValidationError) as error_info:
            TypeAdapter(int).validate_python('not an int')

        with patch('ai_systems_lab.main.Cli') as mock_cli:
            mock_cli.return_value.run.side_effect = error_info.value

            # act
            with pytest.raises(SystemExit) as exc_info:
                main()

            # assert
            assert str(exc_info.value) == 'Configuration or response validation failed.'
            mock_cli.return_value.close.assert_called_once_with()

    def test_main_reports_api_error(self):
        # arrange
        api_error = APIError(503, {'error': {'message': 'Service unavailable', 'status': 'UNAVAILABLE'}})
        with patch('ai_systems_lab.main.Cli') as mock_cli_class:
            mock_cli_class.return_value.run.side_effect = api_error

            # act
            with pytest.raises(SystemExit) as exc_info:
                main()

            # assert
            assert str(exc_info.value) == 'The Gemini request failed. Please try again later.'
            mock_cli_class.return_value.close.assert_called_once_with()

    def test_main_reports_keyboard_interrupt(self):
        # arrange
        with patch('ai_systems_lab.main.Cli') as mock_cli_class:
            mock_cli_class.return_value.run.side_effect = KeyboardInterrupt()

            # act
            with pytest.raises(SystemExit) as exc_info:
                main()

            # assert
            assert str(exc_info.value) == 'Input cancelled.'
            mock_cli_class.return_value.close.assert_called_once_with()

    def test_main_reports_eof_error(self):
        # arrange
        with patch('ai_systems_lab.main.Cli') as mock_cli_class:
            mock_cli_class.return_value.run.side_effect = EOFError()

            # act
            with pytest.raises(SystemExit) as exc_info:
                main()

            # assert
            assert str(exc_info.value) == 'Input cancelled.'
            mock_cli_class.return_value.close.assert_called_once_with()