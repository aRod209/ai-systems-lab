"""Define the structured response for a research paper question."""

from pydantic import BaseModel, Field

class ResearchPaper(BaseModel):
    """Represent paper metadata and an optional answer to a question."""

    paper_name: str = Field(min_length=1, description='Name of the CS research paper.')
    authors: list[str] = Field(min_length=1, description='Names of the research paper author(s).')
    pages: str = Field(description='Number of pages.')
    subfields: list[str] = Field(description='Sub-feilds of AI.')
    answer: str | None = Field(default=None, description='Answer to specific question about research paper.')
