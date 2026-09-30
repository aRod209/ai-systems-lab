from pydantic import ValidationError
import pytest

from ai_systems_lab.models.research_paper import ResearchPaper


class TestResearchPaper:
    def test_creates_research_paper_when_all_fields_are_valid(self):
        # arrange
        paper_data = {
            'paper_name': 'Test Paper',
            'authors': ['Test Author'],
            'pages': '1',
            'subfields': ['Machine Learning'],
            'answer': 'Test Answer'
        }

        # act
        research_paper = ResearchPaper(**paper_data)

        # assert
        assert research_paper.model_dump() == paper_data

    def test_accepts_none_when_answer_is_explicitly_provided(self):
        # arrange
        paper_data = {
            'paper_name': 'Test Paper',
            'authors': ['Test Author'],
            'pages': '1',
            'subfields': ['Machine Learning'],
            'answer': None
        }

        # act
        research_paper = ResearchPaper(**paper_data)

        # assert
        assert research_paper.answer == None

    @pytest.mark.parametrize(
            'missing_field',
            ['paper_name', 'authors', 'pages', 'subfields']
    )
    def test_rejects_input_when_required_field_is_missing(self, missing_field: str) -> None:
        # arrange
        paper_data = {
                    'paper_name': 'Test Paper',
                    'authors': ['Test Author'],
                    'pages': '1',
                    'subfields': ['Machine Learning'],
                    'answer': 'Test Answer'
                }
        paper_data.pop(missing_field)

        # act
        with pytest.raises(ValidationError) as exc_info:
            ResearchPaper(**paper_data)

        error = exc_info.value.errors()[0]

        # assert
        assert error['loc'] == (missing_field,)
        assert error['type'] == 'missing'

    @pytest.mark.parametrize(
        "field_name",
        ["paper_name", "authors", "pages", "subfields"]
    )
    def test_rejects_input_when_required_field_is_none(self, field_name) -> None:
        # arrange
        paper_data = {
            'paper_name': 'Test Paper',
            'authors': ['Test Author'],
            'pages': '1',
            'subfields': ['Machine Learning'],
            'answer': 'Test Answer'
        }
        paper_data[field_name] = None

        # act
        with pytest.raises(ValidationError) as exc_info:
            ResearchPaper(**paper_data)
        error = exc_info.value.errors()[0]

        #assert
        assert error['loc'] == (field_name,)
        assert error['input'] is None

    @pytest.mark.parametrize(
        ("field_name", "invalid_value", 'expected_error_type'),
        [
            ("paper_name", 123, 'string_type'),
            ("authors", "Ada Lovelace", 'list_type'),
            ("pages", 10, 'string_type'),
            ("subfields", "Machine Learning", 'list_type'),
            ("answer", 123, 'string_type'),
        ],
    )
    def test_rejects_input_when_field_has_invalid_type(
        self,
        field_name: str,
        invalid_value: object,
        expected_error_type: str,
    ) -> None:
         # arrange
        paper_data = {
            'paper_name': 'Test Paper',
            'authors': ['Test Author'],
            'pages': '1',
            'subfields': ['Machine Learning'],
            'answer': 'Test Answer'
        }
        paper_data[field_name] = invalid_value

        # act
        with pytest.raises(ValidationError) as exc_info:
            ResearchPaper(**paper_data)
        error = exc_info.value.errors()[0]

        # assert
        assert error['loc'] == (field_name,)
        assert error['input'] == invalid_value
        assert error['type'] == expected_error_type
