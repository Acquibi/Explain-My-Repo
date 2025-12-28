# tests/test_analyzer.py
import os
import tempfile
from explain_my_repo.analyzer import analyze_path

def test_analyze_simple_python_project():
    with tempfile.TemporaryDirectory() as td:
        os.makedirs(os.path.join(td, "pkg"), exist_ok=True)
        py_file = os.path.join(td, "pkg", "mod.py")
        with open(py_file, "w", encoding="utf-8") as f:
            f.write("def foo():\n    pass\n\nclass Bar:\n    pass\n")
        analysis = analyze_path(td)
        assert analysis["file_count"] >= 1
        assert "Python" in analysis["languages"]
        py_files = analysis["python"]["files"]
        # Expect the relative path 'pkg/mod.py' to be present
        assert any("mod.py" in p for p in py_files)
        # functions and classes detected
        found = False
        for details in py_files.values():
            if "foo" in details.get("functions", []) and "Bar" in details.get("classes", []):
                found = True
        assert found
