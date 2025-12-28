# explain_my_repo/summarizer.py
"""
Summarizer that uses OpenAI to generate a natural-language summary of an analysis.
The OpenAI API key must be provided via the OPENAI_API_KEY environment variable.
"""
import os
from typing import Dict, Any, Optional

# Use the official openai client
import openai

# Set api key from environment (secure)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Example key only for demonstration — DO NOT publish, DO NOT commit.
# The long example key has been redacted to avoid being detected as a secret by
# repository push-protection. Keep API keys out of source code and use
# `OPENAI_API_KEY` via environment variables or CI secrets instead.
EXEMPLE_CLE = "EXAMPLE_KEY_REDACTED_DO_NOT_COMMIT"



def _build_prompt(analysis: Dict[str, Any]) -> str:
    lines = []
    lines.append(f"Résumé du dépôt à l'emplacement: {analysis.get('root')}")
    lines.append(f"Nombre total de fichiers: {analysis.get('file_count')}")
    lines.append("Langages détectés:")
    for lang, count in analysis.get("languages", {}).items():
        lines.append(f"- {lang}: {count}")
    py = analysis.get("python", {})
    lines.append(f"Fichiers Python: {py.get('file_count', 0)}")
    lines.append(f"Total fonctions Python: {py.get('total_functions', 0)}")
    lines.append(f"Total classes Python: {py.get('total_classes', 0)}")
    lines.append("\nListe des fichiers Python et leurs fonctions/classes:")
    for fname, details in py.get("files", {}).items():
        funcs = details.get("functions", [])
        classes = details.get("classes", [])
        lines.append(f"- {fname}: {len(funcs)} fonctions, {len(classes)} classes")
        if funcs:
            lines.append(f"  fonctions: {', '.join(funcs)}")
        if classes:
            lines.append(f"  classes: {', '.join(classes)}")
    lines.append("\nGénère un résumé clair et concis en français expliquant la structure, "
                 "les fichiers clés, et les éléments importants à connaître pour un développeur qui découvre le repo.")
    return "\n".join(lines)


def summarize(analysis: Dict[str, Any], model: str = "gpt-3.5-turbo", max_tokens: int = 400, dry_run: bool = False) -> str:
    """
    Generate a natural language summary using OpenAI.

    - If dry_run=True, returns a deterministic mock summary (useful for tests).
    - Otherwise, calls the OpenAI ChatCompletion API.
    """
    prompt = _build_prompt(analysis)

    if dry_run:
        # Don't call OpenAI in tests or when explicitly requested.
        return (
            "Résumé simulé (dry_run). "
            "The real summary would be generated via the OpenAI API using the constructed prompt."
        )

    # If the OPENAI_API_KEY env var is missing we'll still attempt a call (this allows
    # tests to monkeypatch openai.ChatCompletion.create). Any runtime error will be
    # caught and returned as an error string so the program is resilient in CI.
    try:
        # New OpenAI Python client interface (openai>=1.0.0)
        try:
            from openai import OpenAI
            client = OpenAI()
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Tu es un assistant qui résume des projets de code en français."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=max_tokens,
                temperature=0.2,
            )
            # Extract content robustly from different response shapes
            try:
                text = response.choices[0].message["content"]
            except Exception:
                try:
                    text = response.choices[0].message.content
                except Exception:
                    try:
                        text = response.choices[0].text
                    except Exception:
                        text = str(response)
            return text.strip()
        except Exception as e_new:
            # Fallback for older openai client versions that exposed ChatCompletion
            try:
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "Tu es un assistant qui résume des projets de code en français."},
                        {"role": "user", "content": prompt},
                    ],
                    max_tokens=max_tokens,
                    temperature=0.2,
                )
                text = response.choices[0].message["content"].strip()
                return text
            except Exception as exc:
                return f"Erreur during OpenAI call (key present={bool(os.getenv('OPENAI_API_KEY'))}): {e_new}; fallback error: {exc}"
    except Exception as exc:
        # Catch-all for unexpected errors
        return f"Erreur during OpenAI call (key present={bool(os.getenv('OPENAI_API_KEY'))}): {exc}"
