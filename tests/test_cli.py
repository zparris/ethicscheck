"""CLI integration tests for EthicsCheck."""
from __future__ import annotations
import json
from pathlib import Path
import pytest
from typer.testing import CliRunner
from ethicscheck.cli import app

runner = CliRunner()


def test_version() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "EthicsCheck" in result.output


def test_help() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "audit" in result.output


def test_audit_help() -> None:
    result = runner.invoke(app, ["audit", "--help"])
    assert result.exit_code == 0
    assert "--framework" in result.output
    assert "--fail-on" in result.output


def test_audit_empty_dir_exits_nonzero(tmp_path: Path) -> None:
    """An empty project directory should fail many checks and exit 1."""
    result = runner.invoke(app, ["audit", str(tmp_path), "--framework", "eu-ai-act"])
    # Should exit 1 because many HIGH/CRITICAL checks will fail on empty dir
    assert result.exit_code == 1


def test_audit_json_output(tmp_path: Path) -> None:
    result = runner.invoke(app, ["audit", str(tmp_path), "--framework", "nist-rmf", "--output", "json", "--quiet"])
    # exit code may be non-zero (failures), but output should be valid JSON
    try:
        data = json.loads(result.output)
    except json.JSONDecodeError:
        pytest.fail(f"Output is not valid JSON. Output was:\n{result.output}")
    assert data.get("tool") == "EthicsCheck"
    assert "frameworks" in data


def test_audit_sarif_output(tmp_path: Path) -> None:
    result = runner.invoke(app, ["audit", str(tmp_path), "--framework", "eu-ai-act", "--output", "sarif", "--quiet"])
    try:
        data = json.loads(result.output)
    except json.JSONDecodeError:
        pytest.fail(f"Output is not valid SARIF JSON. Output was:\n{result.output}")
    assert data.get("version") == "2.1.0"
    assert "runs" in data


def test_audit_fail_on_critical_passes_with_only_low(tmp_path: Path) -> None:
    """With --fail-on critical, a project with only low/medium failures should exit 0."""
    # Create enough docs to pass all critical checks but not all medium ones
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "risk_assessment.md").write_text("risk management system: continuous iterative risk management.")
    (tmp_path / "technical_documentation.md").write_text("intended purpose: fraud detection system. version 1.0.")
    (tmp_path / "bias_report.md").write_text("bias examination: demographic parity and disparate impact analysis.")
    (tmp_path / "README.md").write_text("human oversight: human-in-the-loop with override capability. known risk: edge cases.")
    (docs / "test_log.md").write_text("pre-deployment test log: validation results against threshold. test results signed.")
    (docs / "declaration_of_conformity.md").write_text("EU Declaration of Conformity per Article 47.")
    result = runner.invoke(app, [
        "audit", str(tmp_path),
        "--framework", "eu-ai-act",
        "--fail-on", "critical",
    ])
    # With critical docs in place, should not fail on critical severity
    # Exit code should be 0 if no critical failures remain
    assert result.exit_code == 0


def test_init_creates_config(tmp_path: Path) -> None:
    config_path = tmp_path / ".ethicscheck.yaml"
    result = runner.invoke(app, ["init", "--output", str(config_path)])
    assert result.exit_code == 0
    assert config_path.exists()
    content = config_path.read_text()
    assert "frameworks" in content
    assert "fail_on" in content


def test_list_checks_shows_eu_checks() -> None:
    result = runner.invoke(app, ["list-checks"])
    assert result.exit_code == 0
    assert "EU-ART9-001" in result.output


def test_list_checks_filter_by_framework() -> None:
    result = runner.invoke(app, ["list-checks", "--framework", "eu-ai-act"])
    assert result.exit_code == 0
    assert "EU-ART9-001" in result.output
    assert "NIST-GOV-001" not in result.output


def test_check_invalid_id_exits_2(tmp_path: Path) -> None:
    result = runner.invoke(app, ["check", "EU-DOES-NOT-EXIST", str(tmp_path)])
    assert result.exit_code == 2


def test_audit_invalid_framework_exits_2(tmp_path: Path) -> None:
    result = runner.invoke(app, ["audit", str(tmp_path), "--framework", "not-a-framework"])
    assert result.exit_code == 2
