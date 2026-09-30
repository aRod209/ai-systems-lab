"""Handle console input and output for research paper questions."""

import json

from ai_systems_lab.research_paper_service import ResearchPaperService


class Cli:
    """Prompt for a research question and display its response."""

    def __init__(self):
        self.research_paper_service = ResearchPaperService()

    def run(self) -> None:
        """Prompt until a nonempty input is entered, then print the response in JSON format."""
        prompt = ''
        while not prompt:
            print('Enter your prompt about a research paper:')
            prompt = input().strip()

        response = self.research_paper_service.prompt(prompt)
        print(json.dumps(response, indent=2))

    def close(self) -> None:
        """Release resources owned by the research paper service."""
        self.research_paper_service.close()
