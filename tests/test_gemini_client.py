from unittest.mock import patch

import pytest

from ai_systems_lab.gemini_client import GeminiClient
from ai_systems_lab.models.research_paper import ResearchPaper


class TestGeminiClient:
    def test_init_creates_google_client_with_configured_api_key(self):
        # arrange
        with patch('ai_systems_lab.gemini_client.Settings') as mock_settings, \
            patch('ai_systems_lab.gemini_client.genai.Client') as mock_google_client:
            mock_settings.return_value.gemini_api_key = 'test-key'

            # act
            GeminiClient()

            # assert
            mock_google_client.assert_called_once_with(api_key='test-key')

    def test_send_request_passes_prompt_and_model_to_google_client(self):
        # arrange
        question = 'What is the paper about?'
        with patch('ai_systems_lab.gemini_client.Settings') as mock_settings, \
                patch('ai_systems_lab.gemini_client.genai.Client') as mock_google_client:
            mock_settings.return_value.gemini_api_key = 'test-key'
            mock_google_client.return_value.interactions.create.return_value.output_text = 'test response'
            gemini = GeminiClient()

            # act
            gemini.send_request(question)

            # assert
            create_request = mock_google_client.return_value.interactions.create
            create_request.assert_called_once()
            assert create_request.call_args.kwargs['input'] == question
            assert create_request.call_args.kwargs['model'] == 'gemini-3.8-flash'

    def test_send_request_requests_research_paper_json_schema(self):
        # arrange
        with patch('ai_systems_lab.gemini_client.Settings') as mock_settings, \
        patch('ai_systems_lab.gemini_client.genai.Client') as mock_google_client:
            mock_settings.return_value.gemini_api_key = 'test-key'
            gemini = GeminiClient()

            # act
            gemini.send_request('test prompt')

            # assert
            create_request = mock_google_client.return_value.interactions.create
            create_request.assert_called_once()
            response_format = create_request.call_args.kwargs['response_format']
            assert response_format == {
                'type': 'text',
                'mime_type': 'application/json',
                'schema': ResearchPaper.model_json_schema()
            }

    def test_send_request_returns_interaction_output_text(self):
        # arrange
        output_text = '{"answer": "Test response"}'
        with patch('ai_systems_lab.gemini_client.Settings') as mock_settings, \
                patch('ai_systems_lab.gemini_client.genai.Client') as mock_google_client:
            mock_settings.return_value.gemini_api_key = 'test-key'
            mock_google_client.return_value.interactions.create.return_value.output_text = output_text
            gemini = GeminiClient()

            # act
            result = gemini.send_request('test prompt')

            # assert
            assert result == output_text

    def test_send_request_propagates_google_client_error(self):
        # arrange
        client_error = RuntimeError('Gemini request failed.')
        with patch('ai_systems_lab.gemini_client.Settings') as mock_settings, \
        patch('ai_systems_lab.gemini_client.genai.Client') as mock_google_client:
            mock_settings.return_value.gemini_api_key = 'test-key'
            mock_google_client.return_value.interactions.create.side_effect = client_error
            gemini = GeminiClient()

            # act
            with pytest.raises(RuntimeError) as exc_info:
                gemini.send_request('test prompt')

            # assert
            assert exc_info.value is client_error

    def test_close_closes_google_client(self):
        # arrange
        with patch('ai_systems_lab.gemini_client.Settings') as mock_settings, \
                patch('ai_systems_lab.gemini_client.genai.Client') as mock_google_client:
            mock_settings.return_value.gemini_api_key = 'test-key'
            gemini = GeminiClient()

            # act
            gemini.close()

            # assert
            mock_google_client.return_value.close.assert_called_once_with()
