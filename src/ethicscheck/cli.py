"""EthicsCheck CLI - AI ethics pre-deployment compliance checker."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console

from . import __version__
from .config import load_config
from .models import Framework, Severity

app = typer.Typer(
    name="ethicscheck",
    help="AI ethics pre-deployment compliance checker for EU AI Act, NIST AI RMF, and ISO/IEC 42001.",
    rich_markup_mode="rich",
    no_args_is_help=True,
)
console = Console()
err_console = Console(stderr=True)


def version_callback(value: bool) -> None:
    if value:
        console.print(f"EthicsCheck v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        Optional[bool],
        typer.Option("--version", "-v", callback=version_callback, is_eager=True, help="Show version."),
    ] = None,
) -> None:
    """[bold green]EthicsCheck[/] - AI ethics pre-deployment compliance checker.\n
    Supports EU AI Act, NIST AI RMF, and ISO/IEC 42001 frameworks.\n
    [dim]Designed for CI/CD pipelines and developer workflows.[/dim]"""


@app.command()
def audit(
    target: Annotated[str, typer.Argument(help="Path to model file, directory, or project root to audit.")] = ".",
    framework: Annotated[
        Optional[list[str]],
        typer.Option("--framework", "-f", help="Frameworks to check (eu-ai-act, nist-rmf, iso-42001). Repeatable."),
    ] = None,
    config_file: Annotated[
        Optional[Path],
        typer.Option("--config", "-c", help="Path to .ethicscheck.yaml config file."),
    ] = None,
    fail_on: Annotated[
        str,
        typer.Option("--fail-on", help="Minimum severity to trigger non-zero exit (critical|high|medium|low)."),
    ] = "high",
    output: Annotated[
        str,
        typer.Option("--output", "-o", help="Output format: terminal, json, sarif."),
    ] = "terminal",
    quiet: Annotated[bool, typer.Option("--quiet", "-q", help="Suppress output, only set exit code.")] = False,
) -> None:
    """Run a full compliance audit against one or more frameworks.

    Examples:

      [cyan]ethicscheck audit .[/]
      [cyan]ethicscheck audit ./model.pkl --framework eu-ai-act --framework nist-rmf[/]
      [cyan]ethicscheck audit . --output json > report.json[/]
      [cyan]ethicscheck audit . --fail-on critical[/]
    """
    from .output.formats import to_json, to_sarif
    from .output.terminal import print_report
    from .runner import run_audit

    cfg = load_config(config_file)

    # CLI flags override config
    if framework:
        try:
            cfg.frameworks = [Framework(f) for f in framework]
        except ValueError as e:
            err_console.print(f"[red]Invalid framework: {e}[/]")
            raise typer.Exit(2)
    cfg.fail_on = Severity(fail_on)
    cfg.output_format = output

    if not quiet:
        console.print(f"\n[bold]EthicsCheck[/] [dim]v{__version__}[/]")
        console.print(f"  Target  : [cyan]{target}[/]")
        console.print(f"  Frameworks: [cyan]{', '.join(f.value for f in cfg.frameworks)}[/]")
        console.print(f"  Fail-on : [cyan]{cfg.fail_on.value}[/]\n")

    report = run_audit(target, cfg)

    if output == "json":
        print(to_json(report))
    elif output == "sarif":
        print(to_sarif(report))
    else:
        if not quiet:
            print_report(report, console)

    sys.exit(report.exit_code(fail_on))


@app.command()
def check(
    check_id: Annotated[str, typer.Argument(help="Specific check ID to run (e.g. EU-ART9-001).")],
    target: Annotated[str, typer.Argument(help="Path to audit.")] = ".",
) -> None:
    """Run a single named check by ID."""
    from .runner import run_single_check
    result = run_single_check(check_id, target)
    if result is None:
        err_console.print(f"[red]Unknown check ID: {check_id}[/]")
        raise typer.Exit(2)
    from .output.terminal import print_single_check
    print_single_check(result, console)
    sys.exit(0 if result.status.value in ("pass", "warn", "skip", "not_applicable") else 1)


@app.command()
def init(
    output_path: Annotated[
        Path,
        typer.Option("--output", "-o", help="Where to write the config file."),
    ] = Path(".ethicscheck.yaml"),
) -> None:
    """Scaffold a .ethicscheck.yaml configuration file in the current project."""
    template = """\
# EthicsCheck configuration
# See: https://ethicscheck.dev/docs/config

# Compliance frameworks to check against
frameworks:
  - eu-ai-act
  - nist-rmf
  # - iso-42001

# Minimum severity to fail CI/CD pipeline (critical | high | medium | low)
fail_on: high

# Output format: terminal | json | sarif
output_format: terminal

# Optional: paths to required documentation
# model_card_path: ./docs/model_card.md
# technical_docs_path: ./docs/technical_documentation.md
# risk_assessment_path: ./docs/risk_assessment.md
# data_governance_path: ./docs/data_governance.md

# Check IDs to skip (use with caution — document the reason)
skip_checks: []
"""
    if output_path.exists():
        overwrite = typer.confirm(f"{output_path} already exists. Overwrite?", default=False)
        if not overwrite:
            raise typer.Exit()
    output_path.write_text(template)
    console.print(f"[green]✓[/] Created {output_path}")
    console.print("  Edit the file to customise your compliance targets.")


@app.command(name="list-checks")
def list_checks(
    framework: Annotated[
        Optional[str],
        typer.Option("--framework", "-f", help="Filter by framework (eu-ai-act, nist-rmf, iso-42001)."),
    ] = None,
) -> None:
    """List all available compliance checks."""
    from rich.table import Table

    from .runner import get_all_checks

    checks = get_all_checks()
    if framework:
        checks = [c for c in checks if c["framework"] == framework]

    table = Table(title="Available Checks", show_lines=True)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Framework", style="magenta")
    table.add_column("Article/Ref", style="yellow")
    table.add_column("Title")
    table.add_column("Severity", style="red")

    for c in checks:
        table.add_row(c["id"], c["framework"], c["ref"], c["title"], c["severity"])

    console.print(table)
