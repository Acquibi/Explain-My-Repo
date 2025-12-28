# explain_my_repo/cli.py
"""
Command-line interface for the Explain My Repo tool.
Provides:
  - --local <path>
  - --url <git repo url>
"""
import os
import shutil
import tempfile
import click
from rich import print
from rich.panel import Panel
from git import Repo

from .analyzer import analyze_path
from .summarizer import summarize
from .visualizer import visualize

@click.command()
@click.option("--url", "-u", "url", help="URL d'un dépôt GitHub à cloner et analyser")
@click.option("--local", "-l", "local_path", help="Chemin local vers un dépôt à analyser")
@click.option("--output", "-o", "output", help="Chemin de sortie pour le diagramme (sans extension)", default="structure")
@click.option("--render/--no-render", default=False, help="Renderer le diagramme en PNG si graphviz est disponible")
def main(url, local_path, output, render):
    """explain_repo — analyse un dépôt et génère un résumé + diagramme."""
    if not url and not local_path:
        print(Panel("[red]Erreur[/red] : spécifiez soit --url soit --local", title="explain_repo"))
        raise SystemExit(1)

    tmp_dir = None
    try:
        if url:
            print(f"Clonage du dépôt depuis [blue]{url}[/blue]...")
            tmp_dir = tempfile.mkdtemp(prefix="explain_repo_")
            Repo.clone_from(url, tmp_dir)
            target = tmp_dir
        else:
            target = os.path.abspath(local_path)

        print(f"Analyse du dépôt : [green]{target}[/green]")
        analysis = analyze_path(target)

        print("Génération du résumé (via OpenAI)...")
        summary = summarize(analysis)
        print(Panel(summary, title="Résumé du dépôt"))

        print("Génération du diagramme Graphviz...")
        graph_path = visualize(analysis, out_path=output, render=render)
        print(f"Diagramme généré : [cyan]{graph_path}[/cyan]")

    finally:
        if tmp_dir:
            # Clean up temporary clone
            shutil.rmtree(tmp_dir, ignore_errors=True)

if __name__ == "__main__":
    main()
