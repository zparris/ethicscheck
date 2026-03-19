"""Rich terminal output for EthicsCheck compliance reports."""
from __future__ import annotations

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from ..models import AuditReport, CheckResult, CheckStatus, FrameworkResult

_SEVERITY_STYLE: dict[str, str] = {
    "critical": "bold red",
    "high": "red",
    "medium": "yellow",
    "low": "blue",
    "info": "dim",
}

_STATUS_ICON: dict[str, str] = {
    "pass": "[green]✓[/green]",
    "fail": "[red]✗[/red]",
    "warn": "[yellow]⚠[/yellow]",
    "skip": "[dim]–[/dim]",
    "not_applicable": "[dim]n/a[/dim]",
}

_STATUS_STYLE: dict[str, str] = {
    "pass": "green",
    "fail": "red",
    "warn": "yellow",
    "skip": "dim",
    "not_applicable": "dim",
}

_FRAMEWORK_LABEL: dict[str, str] = {
    "eu-ai-act": "EU AI Act",
    "nist-rmf": "NIST AI RMF",
    "iso-42001": "ISO/IEC 42001",
}


def _fw_str(fw: object) -> str:
    """Return the framework identifier as a plain string.

    Works for both built-in :class:`~ethicscheck.models.Framework` enum values
    and plain strings registered by third-party plugins.
    """
    return fw.value if hasattr(fw, "value") else str(fw)  # type: ignore[union-attr]


def _severity_text(severity: str) -> Text:
    t = Text(severity.upper())
    t.stylize(_SEVERITY_STYLE.get(severity, ""))
    return t


def _status_text(status: str) -> Text:
    icon = _STATUS_ICON.get(status, status)
    t = Text.from_markup(f"{icon} {status.upper()}")
    return t


def _print_framework_table(fr: FrameworkResult, console: Console) -> None:
    label = _FRAMEWORK_LABEL.get(_fw_str(fr.framework), _fw_str(fr.framework).replace("-", " ").title())
    score_pct = f"{fr.score * 100:.0f}%"
    console.print(f"\n[bold]{label}[/bold]  [dim]{score_pct} compliant[/dim]")

    table = Table(box=box.ROUNDED, show_header=True, header_style="bold", expand=True)
    table.add_column("", width=3, no_wrap=True)          # icon
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Ref", style="yellow", no_wrap=True)
    table.add_column("Title", ratio=3)
    table.add_column("Sev", no_wrap=True)

    for c in fr.checks:
        icon = _STATUS_ICON.get(c.status.value, "?")
        sev_text = _severity_text(c.severity.value)
        table.add_row(
            Text.from_markup(icon),
            c.check_id,
            c.article_ref,
            c.title,
            sev_text,
            style="" if c.status.value == "fail" else ("dim" if c.status.value in ("skip", "not_applicable") else ""),
        )

    console.print(table)

    # Per-framework summary
    parts = []
    if fr.passed:
        parts.append(f"[green]{fr.passed} passed[/green]")
    if fr.failed:
        parts.append(f"[red]{fr.failed} failed[/red]")
    if fr.warnings:
        parts.append(f"[yellow]{fr.warnings} warnings[/yellow]")
    if fr.skipped:
        parts.append(f"[dim]{fr.skipped} skipped[/dim]")
    console.print("  " + "  ·  ".join(parts))


def print_report(report: AuditReport, console: Console) -> None:
    """Print a full compliance audit report to the Rich console."""
    # Per-framework tables
    for fr in report.frameworks:
        _print_framework_table(fr, console)

    # Overall summary panel
    all_checks = [c for fr in report.frameworks for c in fr.checks]
    total = len(all_checks)
    passed = sum(1 for c in all_checks if c.status == CheckStatus.PASS)
    failed = sum(1 for c in all_checks if c.status == CheckStatus.FAIL)
    warned = sum(1 for c in all_checks if c.status == CheckStatus.WARN)
    skipped = sum(1 for c in all_checks if c.status.value in ("skip", "not_applicable"))

    status_style = "green" if report.overall_status.value == "pass" else "bold red"
    status_label = "PASS" if report.overall_status.value == "pass" else "FAIL"

    lines: list[str] = [
        f"[{status_style}]● {status_label}[/{status_style}]   "
        f"[green]{passed}✓[/green]  [red]{failed}✗[/red]  [yellow]{warned}⚠[/yellow]  [dim]{skipped} skipped[/dim]  of {total} checks",
    ]
    if report.critical_count:
        lines.append(f"[bold red]  {report.critical_count} CRITICAL failure(s)[/bold red]")
    if report.high_count:
        lines.append(f"[red]  {report.high_count} HIGH failure(s)[/red]")

    # Top 3 remediations
    failures = [c for c in all_checks if c.status == CheckStatus.FAIL and c.remediation]
    # Sort: critical first, then high
    sev_order = ["critical", "high", "medium", "low", "info"]
    failures.sort(key=lambda c: sev_order.index(c.severity.value))
    if failures:
        lines.append("")
        lines.append("[bold]Top remediation actions:[/bold]")
        for c in failures[:3]:
            sev_style = _SEVERITY_STYLE.get(c.severity.value, "")
            lines.append(f"  [{sev_style}]{c.severity.value.upper()}[/{sev_style}] [{c.check_id}] {c.remediation}")

    panel_content = "\n".join(lines)
    panel = Panel(panel_content, title="[bold]Audit Summary[/bold]", border_style=status_style, padding=(0, 1))
    console.print()
    console.print(panel)
    console.print()


def print_single_check(result: CheckResult, console: Console) -> None:
    """Print a single check result to the Rich console."""
    fw_label = _FRAMEWORK_LABEL.get(_fw_str(result.framework), _fw_str(result.framework).replace("-", " ").title())
    status_style = _STATUS_STYLE.get(result.status.value, "")
    icon = _STATUS_ICON.get(result.status.value, "")
    sev_style = _SEVERITY_STYLE.get(result.severity.value, "")

    lines = [
        f"{icon} [{status_style}]{result.status.value.upper()}[/{status_style}]"
        f"  [{sev_style}]{result.severity.value.upper()}[/{sev_style}]"
        f"  [dim]{fw_label}[/dim]  [yellow]{result.article_ref}[/yellow]",
        "",
        f"[dim]{result.description}[/dim]",
    ]
    if result.evidence:
        lines.append("")
        lines.append("[bold]Evidence:[/bold]")
        for e in result.evidence:
            lines.append(f"  [cyan]{e}[/cyan]")
    if result.remediation:
        lines.append("")
        lines.append(f"[bold]Remediation:[/bold] {result.remediation}")

    panel = Panel(
        "\n".join(lines),
        title=f"[bold cyan]{result.check_id}[/bold cyan]  {result.title}",
        border_style=status_style or "default",
        padding=(0, 1),
    )
    console.print(panel)
