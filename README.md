# Explain My Repo

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)

Beautiful, lightweight tool to quickly analyze any Git repository (local or remote) and produce:
- A human-friendly natural language summary (via OpenAI)
- A visual diagram of the project structure (Graphviz)

Whether you're onboarding, auditing, or exploring unfamiliar code, Explain My Repo gives you a quick overview so you can get productive faster. 🚀

---

## 🔍 Key Features

- Detect files, folders and programming languages used in a repository
- Identify Python functions and classes (using Python AST)
- Generate concise, readable summaries via OpenAI (secure: API key via env var)
- Visualize file → class relationships with Graphviz (.gv, PNG)
- Simple CLI: `explain_repo --local <path>` or `--url <git-url>`
- Includes an example repository for quick testing

---

## 🔐 Security & API Key

**Never commit your OpenAI API key to a public repo.** Store it in an environment variable named `OPENAI_API_KEY`:

```bash
export OPENAI_API_KEY="sk-your_real_key_here"
```

> The repository contains an example key string in the documentation for demonstration only — **do not publish or commit any real keys**. Revoke any exposed keys immediately.

---

## ⚙️ Installation (Local)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## 🚀 Quick Start

Analyze a local example repo:

```bash
explain_repo --local ./examples/sample_repo
```

Analyze a remote Git repository (clones temporarily):

```bash
explain_repo --url https://github.com/owner/repo.git
```

Example output includes:
- A nice text summary printed to the terminal
- A Graphviz file: `structure.gv` (or PNG if rendered with `--render`)

---

## 🛠 CLI Options

- `--local <path>` : Analyze a local repository
- `--url <git-url>` : Clone and analyze a remote repository
- `--output <name>` : Base name for the generated Graphviz file (default: `structure`)
- `--render` : Attempt to render the graph to a PNG (if Graphviz is installed)

---

## ✅ Testing

Run the test suite with pytest:

```bash
pytest -q
```

The tests include:
- `tests/test_analyzer.py` — verifies detection of Python files, functions and classes
- `tests/test_summarizer.py` — checks summarizer behavior and avoids calling OpenAI in CI

---

## 🧩 Example Repository

`examples/sample_repo/` is a tiny example project included so you can try out the CLI without providing your own repository.

---

## 📦 Packaging

This project includes a `setup.py` so you can install it in editable mode (`pip install -e .`) and use the console script `explain_repo`.

---

## 🤝 Contributing

Contributions and improvements are welcome! Please open an issue or a PR with a clear description of changes.

---

## 📄 License

This project is provided under the MIT License. See `LICENSE` for details.

---

If you'd like, I can also add a `LICENSE` file (MIT), GitHub Actions CI for tests, or internationalized README variants. Would you like me to add any of those? ✨


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