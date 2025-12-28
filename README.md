# Explain My Repo  

[![CI](https://github.com/Acquibi/Explain-My-Repo/actions/workflows/ci.yml/badge.svg)](https://github.com/Acquibi/Explain-My-Repo/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org) [![PyPI (not published)](https://img.shields.io/badge/pypi-not%20published-lightgrey.svg)]()


A lightweight, fast tool to analyze any Git repository (local or remote) and instantly produce:

- A concise, human-friendly natural language summary (via OpenAI)
- A visual diagram of code structure (Graphviz)
- CLI-first UX for quick, repeatable scans

Explain My Repo helps engineers, auditors, and open-source explorers understand a codebase quickly — perfect for onboarding, code reviews, and quick audits. ✨

---

<p align="center">
  <img alt="demo gif" src="assets/demo.gif" width="640" />
  
  <sub>Demo GIF placeholder — add `assets/demo.gif` (short screen recording of `explain_repo --local ./examples/sample_repo`), convert to optimized GIF, and commit to show the project in action.</sub>
</p>

---

## 🔍 Key Features

- Fast repository scan (files, folders, and languages)
- Python AST-based detection of functions & classes
- Natural-language summaries via OpenAI (secure: env var)
- Graphviz visualizations (`.gv`, optional PNG render)
- Simple CLI: `explain_repo --local <path>` or `--url <git-url>`
- Lightweight, test-covered, easy to extend

---

## 🚀 Quick Start

Install:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

Analyze example repo:

```bash
explain_repo --local ./examples/sample_repo
```

Or analyze a remote repo:

```bash
explain_repo --url https://github.com/owner/repo.git
```

Tips: set `OPENAI_API_KEY` in your environment to enable summaries.

```bash
export OPENAI_API_KEY="sk-your_real_key_here"
```

---

## 📈 Make this repo discoverable (quick checklist)

- Add meaningful **GitHub topics** (e.g. `code-analysis`, `openai`, `graphviz`, `python`, `cli`) via the repo settings.
- Add a short, SEO-friendly description and a clear README hero.
- Add a short demo GIF and a social preview image (Open Graph) for better sharing.
- Add CI badges and a version badge (publish a PyPI release when ready).
- Promote on community channels (Hacker News, Reddit, Dev.to, Twitter/X) with a short, clear post and demo screenshot.

---

## 🧪 Testing & CI

We run tests on GitHub Actions via `.github/workflows/ci.yml`.

Run locally:

```bash
pytest -q
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repo
2. Create a branch for your change
3. Add tests for new behavior
4. Open a PR and reference the issue if there is one

Also consider adding a short `CONTRIBUTING.md`, `CHANGELOG.md` and an issue/PR template for better community onboarding.

---

## 📄 License

MIT © Acquibi — see `LICENSE`.

---

## 📣 Outreach notes (for maintainers)

- Create a short announcement post with a GIF (30–60s) showing the CLI and the generated summary.
- Share code samples and a brief tutorial on Dev.to / Medium.
- Submit a short demo to Hacker News and relevant subreddits (r/python, r/programming, r/opensource).
- Add the PyPI release and announce it with a changelog and release notes.

---

If you want, I can:
- create a polished demo GIF (recording + optimize),
- add social preview image and GitHub Topics via the API, and
- add a docs site (MkDocs) and GitHub Pages deployment.

Would you like me to create the demo GIF and add topics now? :rocket:


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