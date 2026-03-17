"""Tests for EU AI Act compliance framework."""
from __future__ import annotations
from pathlib import Path
import pytest
from ethicscheck.frameworks.eu_ai_act import EUAIActFramework
from ethicscheck.config import EthicsCheckConfig
from ethicscheck.models import CheckStatus, FrameworkResult, Framework


def make_fw(tmp_path: Path) -> EUAIActFramework:
    return EUAIActFramework(target=str(tmp_path), config=EthicsCheckConfig())


def test_run_all_returns_30_checks(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    results = fw.run_all()
    assert len(results) == 31


def test_risk_management_pass(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "risk_assessment.md").write_text("# Risk Management System\nrisk management system documented here.")
    fw = make_fw(tmp_path)
    result = fw.run_check("EU-ART9-001")
    assert result is not None
    assert result.status == CheckStatus.PASS
    assert result.check_id == "EU-ART9-001"


def test_risk_management_fail(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    result = fw.run_check("EU-ART9-001")
    assert result is not None
    assert result.status == CheckStatus.FAIL
    assert result.remediation != ""


def test_bias_examination_pass(tmp_path: Path) -> None:
    (tmp_path / "bias_report.md").write_text("# Bias Report\nDemographic parity analysis performed on protected attributes.")
    fw = make_fw(tmp_path)
    result = fw.run_check("EU-ART10-003")
    assert result is not None
    assert result.status == CheckStatus.PASS


def test_bias_examination_fail(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    result = fw.run_check("EU-ART10-003")
    assert result is not None
    assert result.status == CheckStatus.FAIL


def test_technical_documentation_pass(tmp_path: Path) -> None:
    (tmp_path / "technical_documentation.md").write_text("# Technical Documentation\nintended purpose: fraud detection.")
    fw = make_fw(tmp_path)
    result = fw.run_check("EU-ART11-001")
    assert result is not None
    assert result.status == CheckStatus.PASS
    assert len(result.evidence) > 0


def test_human_oversight_fail(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    result = fw.run_check("EU-ART14-001")
    assert result is not None
    assert result.status == CheckStatus.FAIL


def test_skip_check(tmp_path: Path) -> None:
    cfg = EthicsCheckConfig(skip_checks=["EU-ART9-001"])
    fw = EUAIActFramework(target=str(tmp_path), config=cfg)
    results = fw.run_all()
    skipped = [r for r in results if r.check_id == "EU-ART9-001"]
    assert len(skipped) == 1
    assert skipped[0].status == CheckStatus.SKIP


def test_unknown_check_returns_none(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    result = fw.run_check("EU-DOES-NOT-EXIST")
    assert result is None


def test_framework_result_score(tmp_path: Path) -> None:
    """Score should be between 0.0 and 1.0 and computed from passed/total."""
    fw = make_fw(tmp_path)
    checks = fw.run_all()
    result = FrameworkResult(framework=Framework.EU_AI_ACT, checks=checks)
    assert 0.0 <= result.score <= 1.0
    non_skipped = [c for c in checks if c.status not in (CheckStatus.SKIP,)]
    if non_skipped:
        passed = sum(1 for c in non_skipped if c.status == CheckStatus.PASS)
        expected_score = passed / len(non_skipped)
        assert abs(result.score - expected_score) < 0.01


def test_declaration_of_conformity_pass(tmp_path: Path) -> None:
    (tmp_path / "declaration_of_conformity.md").write_text("EU Declaration of Conformity per Article 47.")
    fw = make_fw(tmp_path)
    result = fw.run_check("EU-ANNIV-001")
    assert result is not None
    assert result.status == CheckStatus.PASS


def test_check_metadata_ids_unique(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    ids = [m["id"] for m in fw.check_metadata()]
    assert len(ids) == len(set(ids)), "Duplicate check IDs in EU AI Act metadata"
