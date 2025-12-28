# Explain My Repo

[![CI](https://github.com/Acquibi/Explain-My-Repo/actions/workflows/ci.yml/badge.svg)](https://github.com/Acquibi/Explain-My-Repo/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)

Short description

Explain My Repo is a simple CLI tool that analyzes a Git repository (local or remote) and generates:

- A short natural-language summary (via OpenAI),
- A simple Graphviz diagram showing files and class relationships,
- A concise `analysis` dictionary suitable for automation or further processing.

This repository contains a minimalist, well-tested implementation that you can install and run locally.

---

## Description

Explain My Repo scans a project and extracts structural information (files, languages, Python functions and classes). It then uses a text-generation model (OpenAI) to produce a human-readable summary and can render a visual diagram with Graphviz. The tool is intentionally small, portable, and easy to extend.

---

## How it works (project structure)

- `explain_my_repo/`
  - `__init__.py` — package metadata
  - `cli.py` — CLI (Click) that accepts `--local` and `--url` and orchestrates the workflow
  - `analyzer.py` — walks the repository, detects file types, and parses Python `def` and `class` using `ast`
  - `summarizer.py` — builds a prompt from the analysis and calls OpenAI (uses `OPENAI_API_KEY` from env)
  - `visualizer.py` — generates a Graphviz `.gv` file and can render a PNG

- `examples/sample_repo/` — small example repository to test the tool
- `tests/` — pytest tests for core behavior (analyzer and summarizer)
- `setup.py` & `requirements.txt` — packaging and dependencies
- `.github/workflows/ci.yml` — CI job that installs deps and runs tests

---

## Quickstart

1. Create a virtual environment and install:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

2. Run locally on the included example:

```bash
# Optional: set your OpenAI API key in environment
export OPENAI_API_KEY="sk-your_real_key_here"

explain_repo --local ./examples/sample_repo
```

3. Observe output:
- A summary printed to the terminal
- A `structure.gv` file (optionally `structure.png` if rendered with `--render`)

---

## Security

- **Never** commit API keys or secrets. Use `OPENAI_API_KEY` (env var) or CI secrets for automated runs. This repository intentionally redacts example keys and includes a `.gitignore` to avoid committing local environment files.

---

## Development & Testing

Run tests:

```bash
pytest -q
```

Suggested development workflow:
1. Fork and branch
2. Add tests for new behavior
3. Run `pytest` and ensure green
4. Open PR

---

## Contributing

Contributions are welcome. Please add tests and a clear description of the change in PRs.

---

## License

MIT © Acquibi



## 💻 Installation

1. Clone the repository:

```bash
git clone <repo_url>
cd explain_my_repo
Install dependencies:

bash
Copier le code
pip install -r requirements.txt
Or install the package directly:

bash
Copier le code
pip install -e .
🔑 OpenAI API Key Management
To generate summaries, Explain My Repo uses the OpenAI API. For security reasons, never hardcode your API key in the code.

Get your OpenAI API key from https://platform.openai.com.

Set it as an environment variable before running the program:

bash
Copier le code
export OPENAI_API_KEY="your_personal_key"
⚠️ Never share this key publicly. If your key is exposed, revoke it immediately from your OpenAI dashboard.

⚙️ Usage
Analyze a local repository
bash
Copier le code
explain_repo --local ./examples/sample_repo
Analyze a remote GitHub repository
bash
Copier le code
explain_repo --url https://github.com/user/project
The program will output:

A text summary of the project

A diagram file repo_structure.gv.pdf generated via Graphviz

📂 Project Structure
arduino
Copier le code
explain_my_repo/
│
├── explain_my_repo/
│   ├── __init__.py
│   ├── cli.py
│   ├── analyzer.py
│   ├── summarizer.py
│   └── visualizer.py
│
├── examples/sample_repo/
├── tests/
│   ├── test_analyzer.py
│   └── test_summarizer.py
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
🧩 Technical Details
analyzer.py
Scans all repository files

Detects:

Languages (.py, .js, etc.)

Python functions (def ...)

Python classes (class ...)

Returns a dictionary analysis

summarizer.py
Uses openai to generate a summary

Reads the API key securely via os.getenv("OPENAI_API_KEY")

Includes an example key EXAMPLE_KEY for demonstration only (never commit this)

Prompt includes languages, number of files, functions, and classes

visualizer.py
Generates a simple diagram of files and classes

Uses Graphviz to produce PDF/PNG

cli.py
Main command explain_repo

Options:

--url : remote GitHub repository

--local : local repository

Displays summary and generates diagram

🧪 Testing
The tests/ folder contains basic tests for:

File, function, and class analysis (test_analyzer.py)

Summary generation (test_summarizer.py)

Run tests with:

bash
Copier le code
pytest tests/
💡 Example Output
Sample summary:

vbnet
Copier le code
This project is a REST API for managing tasks. It contains 5 Python files, 2 main classes, and 8 functions. Key modules: tasks.py, utils.py. The structure is simple and modular.
Diagram repo_structure.gv.pdf visualizes files and classes.

📌 GitHub Best Practices
Never commit your OpenAI API key.

Add .gitignore:

bash
Copier le code
__pycache__/
*.pyc
.env
repo_structure.gv
Use environment variables for the key

Test with examples/sample_repo/ before analyzing real repositories

🛠️ Tech Stack
Python 3.10+

click (CLI)

tree_sitter (code parsing)

gitpython (remote repository)

graphviz (diagram generation)

openai (natural language summary)

rich (console formatting)

🔗 Useful Links
OpenAI: https://platform.openai.com

Graphviz: https://graphviz.org

Python: https://www.python.org

👨‍💻 Author & Contact
Developed by Acquibi.

For professional inquiries, feedback, or collaborations:

GitHub: https://github.com/Acquibi