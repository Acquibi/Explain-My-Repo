# tests/test_summarizer.py
import os
from explain_my_repo.summarizer import summarize

class DummyResponse:
    def __init__(self, text):
        self.choices = [type("C", (), {"message": {"content": text}})]

def test_summarize_dry_run(tmp_path, monkeypatch):
    analysis = {
        "root": str(tmp_path),
        "file_count": 1,
        "languages": {"Python": 1},
        "python": {"file_count": 1, "total_functions": 0, "total_classes": 0, "files": {}},
    }
    # dry_run True should not call OpenAI
    out = summarize(analysis, dry_run=True)
    assert "Simulated summary" in out


def test_summarize_monkeypatched_openai(monkeypatch):
    # Monkeypatch the new OpenAI client (and fallback old API if present) to return a deterministic response
    import openai
    def fake_create(*args, **kwargs):
        return DummyResponse("Generated summary by test")

    class FakeClient:
        class chat:
            class completions:
                @staticmethod
                def create(*a, **kw):
                    return DummyResponse("Generated summary by test")

    # Patch the OpenAI constructor to return our fake client
    monkeypatch.setattr(openai, "OpenAI", lambda *a, **kw: FakeClient())

    # Also patch legacy ChatCompletion.create if it exists
    if hasattr(openai, "ChatCompletion"):
        monkeypatch.setattr(openai.ChatCompletion, "create", fake_create)

    analysis = {
        "root": "/repo",
        "file_count": 2,
        "languages": {"Python": 2},
        "python": {"file_count": 2, "total_functions": 1, "total_classes": 1, "files": {}},
    }
    out = summarize(analysis, dry_run=False)
    assert "Generated summary by test" in out
