"""Start the research paper command-line application."""

from google.genai.errors import APIError
from pydantic import ValidationError

from ai_systems_lab.cli import Cli


def main() -> None:
    """Create and run the command-line interface."""
    try:
        cli = Cli()
        try:
            cli.run()
        finally:
            cli.close()
    except ValidationError:
        raise SystemExit('Configuration or response validation failed.')
    except APIError:
        raise SystemExit('The Gemini request failed. Please try again later.')
    except (KeyboardInterrupt, EOFError):
        raise SystemExit('Input cancelled.')

if __name__ == '__main__':
    main()