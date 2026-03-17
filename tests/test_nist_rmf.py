"""Tests for NIST AI RMF compliance framework."""
from __future__ import annotations
from pathlib import Path
import pytest
from ethicscheck.frameworks.nist_rmf import NISTRMFFramework
from ethicscheck.config import EthicsCheckConfig
from ethicscheck.models import CheckStatus


def make_fw(tmp_path: Path) -> NISTRMFFramework:
    return NISTRMFFramework(target=str(tmp_path), config=EthicsCheckConfig())


def test_run_all_returns_25_checks(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    results = fw.run_all()
    assert len(results) == 25


def test_governance_policy_pass(tmp_path: Path) -> None:
    (tmp_path / "ai_policy.md").write_text("# AI Governance Policy\nAI governance policy for responsible deployment.")
    fw = make_fw(tmp_path)
    result = fw.run_check("NIST-GOV-001")
    assert result is not None
    assert result.status == CheckStatus.PASS


def test_governance_policy_fail(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    result = fw.run_check("NIST-GOV-001")
    assert result is not None
    assert result.status in (CheckStatus.FAIL, CheckStatus.WARN)


def test_bias_fairness_pass(tmp_path: Path) -> None:
    (tmp_path / "fairness_report.md").write_text("Bias evaluation: fairness metrics measured across demographic subgroups. Disparate impact analysis complete.")
    fw = make_fw(tmp_path)
    result = fw.run_check("NIST-MEA-002")
    assert result is not None
    assert result.status == CheckStatus.PASS


def test_bias_fairness_fail(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    result = fw.run_check("NIST-MEA-002")
    assert result is not None
    assert result.status == CheckStatus.FAIL


def test_human_fallback_fail(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    result = fw.run_check("NIST-MAN-006")
    assert result is not None
    assert result.status == CheckStatus.FAIL
    assert result.remediation != ""


def test_human_fallback_pass(tmp_path: Path) -> None:
    (tmp_path / "fallback.md").write_text("Human fallback procedure: if system fails, escalate to on-call engineer. Human override capability documented.")
    fw = make_fw(tmp_path)
    result = fw.run_check("NIST-MAN-006")
    assert result is not None
    assert result.status == CheckStatus.PASS


def test_intended_use_pass(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# Model Card\nIntended use: credit risk assessment. Deployment context: internal banking operations.")
    fw = make_fw(tmp_path)
    result = fw.run_check("NIST-MAP-001")
    assert result is not None
    assert result.status == CheckStatus.PASS


def test_unknown_check_returns_none(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    assert fw.run_check("NIST-DOES-NOT-EXIST") is None


def test_check_metadata_ids_unique(tmp_path: Path) -> None:
    fw = make_fw(tmp_path)
    ids = [m["id"] for m in fw.check_metadata()]
    assert len(ids) == len(set(ids)), "Duplicate check IDs in NIST RMF metadata"
