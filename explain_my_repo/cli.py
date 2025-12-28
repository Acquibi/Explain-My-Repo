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
@click.option("--url", "-u", "url", help="URL of a GitHub repository to clone and analyze")
@click.option("--local", "-l", "local_path", help="Local path to a repository to analyze")
@click.option("--output", "-o", "output", help="Output path for the diagram (without extension)", default="structure")
@click.option("--render/--no-render", default=False, help="Render the diagram to PNG if Graphviz is available")
def main(url, local_path, output, render):
    """explain_repo — analyze a repository and generate a summary + diagram."""
    if not url and not local_path:
        print(Panel("[red]Error[/red]: specify either --url or --local", title="explain_repo"))
        raise SystemExit(1)

    tmp_dir = None
    try:
        if url:
            print(f"Cloning repository from [blue]{url}[/blue]...")
            tmp_dir = tempfile.mkdtemp(prefix="explain_repo_")
            Repo.clone_from(url, tmp_dir)
            target = tmp_dir
        else:
            target = os.path.abspath(local_path)

        print(f"Analyzing repository: [green]{target}[/green]")
        analysis = analyze_path(target)

        print("Generating summary (via OpenAI)...")
        summary = summarize(analysis)
        print(Panel(summary, title="Repository summary"))

        print("Generating Graphviz diagram...")
        graph_path = visualize(analysis, out_path=output, render=render)
        print(f"Diagram generated: [cyan]{graph_path}[/cyan]")

    finally:
        if tmp_dir:
            # Clean up temporary clone
            shutil.rmtree(tmp_dir, ignore_errors=True)

if __name__ == "__main__":
    main()
