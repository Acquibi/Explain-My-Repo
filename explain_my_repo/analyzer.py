# explain_my_repo/analyzer.py
"""
Analyze a local repo folder:
- list files and folders
- detect languages from extensions
- for Python files: extract functions and classes (using ast)
Returns an 'analysis' dictionary summarizing findings.
"""
from collections import defaultdict
import os
import ast
from typing import Dict, Any, List

EXT_LANG_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".go": "Go",
    ".rb": "Ruby",
    ".rs": "Rust",
    ".cpp": "C++",
    ".c": "C",
    ".cs": "C#",
    ".md": "Markdown",
}


def _get_language_for_file(filename: str) -> str:
    _, ext = os.path.splitext(filename)
    return EXT_LANG_MAP.get(ext.lower(), "Other")


def _parse_python_file(path: str) -> Dict[str, List[str]]:
    """Return dict with lists of function and class names in a Python file."""
    functions = []
    classes = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            src = f.read()
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
    except Exception:
        # In case of parse error, ignore and return empty lists
        pass
    return {"functions": functions, "classes": classes}


def analyze_path(path: str) -> Dict[str, Any]:
    """
    Walk the given path and analyze files & directories.
    Returns:
    {
      "root": path,
      "files": [list of file paths],
      "languages": {lang: count},
      "python": {
          "files": {relpath: {"functions": [...], "classes":[...]}},
          "total_functions": N,
          "total_classes": M
      },
      "file_count": N
    }
    """
    files = []
    languages = defaultdict(int)
    python_files = {}
    total_functions = 0
    total_classes = 0

    for root, dirs, filenames in os.walk(path):
        for fname in filenames:
            full = os.path.join(root, fname)
            rel = os.path.relpath(full, path)
            files.append(rel)
            lang = _get_language_for_file(fname)
            languages[lang] += 1
            if lang == "Python":
                parsed = _parse_python_file(full)
                python_files[rel] = parsed
                total_functions += len(parsed["functions"])
                total_classes += len(parsed["classes"])

    analysis = {
        "root": os.path.abspath(path),
        "files": sorted(files),
        "languages": dict(languages),
        "python": {
            "files": python_files,
            "total_functions": total_functions,
            "total_classes": total_classes,
            "file_count": len(python_files),
        },
        "file_count": len(files),
    }
    return analysis
