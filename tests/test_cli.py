# tests/test_cli.py
from click.testing import CliRunner
from explain_my_repo.cli import main
from pathlib import Path
import shutil


def test_cli_dry_run(tmp_path):
    # Copy sample repo into isolated filesystem
    repo_root = Path(__file__).resolve().parents[1]
    sample_src = repo_root / "examples" / "sample_repo"

    runner = CliRunner()
    with runner.isolated_filesystem():
        # copy sample repo into current FS
        shutil.copytree(sample_src, "sample_repo")
        result = runner.invoke(main, ["--local", "sample_repo", "--dry-run"])
        assert result.exit_code == 0
        assert "Simulated summary" in result.output
        # diagram should be generated
        assert Path("structure.gv").exists()