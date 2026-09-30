"""Provide access to Gemini for structured research paper responses."""

from google import genai

from ai_systems_lab.config import Settings
from ai_systems_lab.models.research_paper import ResearchPaper


class GeminiClient:
    """Send research paper questions to the configured Gemini client."""

    def __init__(self):
        self.settings = Settings()
        self.client = genai.Client(api_key=self.settings.gemini_api_key)

    def send_request(self, input_text: str) -> str:
        """Request a research paper response in the ``ResearchPaper`` JSON schema.

        Args:
            input_text: Question to send to Gemini.

        Returns:
            The response text produced by Gemini.
        """
        interaction = self.client.interactions.create(
            model='gemini-3.8-flash',
            input=input_text,
            response_format={
                'type': 'text',
                'mime_type': 'application/json',
                'schema': ResearchPaper.model_json_schema()
            }
        )

        return interaction.output_text

    def close(self) -> None:
        """Release the underlying Gemini client."""
        self.client.close()