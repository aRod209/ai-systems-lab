"""Validate and decode research paper answers returned by Gemini."""

from typing import Any

from ai_systems_lab.gemini_client import GeminiClient
from ai_systems_lab.models.research_paper import ResearchPaper


class ResearchPaperService:
    """Coordinate Gemini requests and research paper response validation."""

    def __init__(self, gemini_client: GeminiClient | None = None) -> None:
        self.owns_gemini_client = gemini_client is None
        self.gemini_client = (
            gemini_client if gemini_client is not None else GeminiClient()
        )

    def prompt(self, prompt: str) -> dict[str, Any]:
        """Prompt Gemini about a research paper and return a validated response as a dictionary.

        Args:
            prompt: Research paper prompt to submit.

        Returns:
            The dictionary representation of a validated ``ResearchPaper``.

        Raises:
            pydantic.ValidationError: If the response is invalid JSON or does
                not match the research paper schema.
        """
        output_text = self.gemini_client.send_request(prompt)
        paper = ResearchPaper.model_validate_json(output_text)
        return paper.model_dump()

    def close(self) -> None:
        """Close the Gemini client only if this service created it."""
        if self.owns_gemini_client:
            self.gemini_client.close()
