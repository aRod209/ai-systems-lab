<div align="center">
  <h1>🔬 AI Systems Lab</h1>
  <p><strong>Ask about AI research papers from your terminal.</strong></p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" alt="Python 3.11 or newer" />
    <img src="https://img.shields.io/badge/Google-Gemini-4E72E0?style=flat-square&amp;logo=googlegemini&amp;logoColor=white" alt="Uses the Google Gemini API" />
    <img src="https://img.shields.io/badge/Pydantic-validation-E92063?style=flat-square&amp;logo=pydantic&amp;logoColor=white" alt="Response validation with Pydantic" />
  </p>
</div>

AI Systems Lab is a small Python CLI that sends a research-paper prompt to Gemini, validates the structured response with Pydantic, and prints formatted JSON.

## 🚀 Quick start

You'll need **Python 3.11 or newer**, a **Gemini API key**, and an internet connection for requests. Run these commands from the project directory.

### macOS / Linux (bash or zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
export GEMINI_API_KEY='your-api-key'
ai-systems-lab
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
$env:GEMINI_API_KEY = "your-api-key"
ai-systems-lab
```

Replace `your-api-key` with your own key. The editable install includes the project's test dependency; to install only runtime dependencies, use `python -m pip install -e .` instead.

> [!TIP]
> If PowerShell blocks virtual-environment activation, you can use `.\.venv\Scripts\python.exe -m pip install -e ".[dev]"` and then `.\.venv\Scripts\ai-systems-lab.exe` without activating it. Set `GEMINI_API_KEY` in that PowerShell session first.

## 🔑 Configuration

The only required setting is `GEMINI_API_KEY`. Instead of setting it in your shell, you can put it in a `.env` file **in the project root**:

```dotenv
GEMINI_API_KEY=your-api-key
```

The app looks for `.env` relative to the current working directory, so run it from the project root when using this option. `.env` is ignored by Git; **never commit or share a real API key**. A shell environment variable also works when running the command from another directory.

## 💬 Usage and output

Run `ai-systems-lab` and enter a nonempty prompt when asked. For example: `What is the main contribution of the paper "Attention Is All You Need"?`

The response is printed as JSON with the fields `paper_name`, `authors`, `pages`, `subfields`, and `answer`. Here is an **illustrative** response, not an actual API result:

```json
{
  "paper_name": "Example Paper",
  "authors": ["Example Author"],
  "pages": "12",
  "subfields": ["Machine Learning"],
  "answer": "An illustrative answer."
}
```

`answer` can be `null`; `pages` is currently represented as a string. The app reports configuration, API, and response-validation failures at the command line rather than returning a JSON response for those failures.

## 🧪 Development

Install with the `[dev]` extra shown above, then run the tests from the project root:

```bash
python -m pytest -q
```

The unit tests cover the `ResearchPaper` model, `ResearchPaperService`, `Cli`, the `main()` entry point, `GeminiClient`, and `Settings`. Gemini requests are mocked, and settings tests use an isolated environment and temporary `.env` files; the suite does not make live API requests or require a real API key.

## 🗂️ Project structure

| Path | Purpose |
| --- | --- |
| `src/ai_systems_lab/main.py` | CLI entry point and top-level error handling |
| `src/ai_systems_lab/cli.py` | Prompt input and JSON output |
| `src/ai_systems_lab/config.py` | Environment-based settings |
| `src/ai_systems_lab/gemini_client.py` | Gemini API requests |
| `src/ai_systems_lab/research_paper_service.py` | Response validation and decoding |
| `src/ai_systems_lab/models/research_paper.py` | Structured response model |
| `tests/` | Automated tests |

## ⚠️ Current limitations

- The app accepts a text prompt, not a paper file or a verified paper source. Name the paper in your prompt if relevant.
- A response matching the JSON schema is **not** proof that its claims, metadata, or citations are accurate. Verify research claims against the original paper.
- There is no built-in paper retrieval or document-grounded answering yet.
