"""Orchestrates compliance checks across frameworks."""
from __future__ import annotations
from typing import Any
from .config import EthicsCheckConfig
from .models import AuditReport, FrameworkResult, Framework, CheckResult
from .frameworks.eu_ai_act import EUAIActFramework
from .frameworks.nist_rmf import NISTRMFFramework
from .frameworks.iso_42001 import ISO42001Framework


FRAMEWORK_MAP = {
    Framework.EU_AI_ACT: EUAIActFramework,
    Framework.NIST_RMF: NISTRMFFramework,
    Framework.ISO_42001: ISO42001Framework,
}


def run_audit(target: str, cfg: EthicsCheckConfig) -> AuditReport:
    """Run all configured frameworks against the target."""
    results: list[FrameworkResult] = []
    for fw_enum in cfg.frameworks:
        fw_class = FRAMEWORK_MAP.get(fw_enum)
        if fw_class is None:
            continue
        fw = fw_class(target=target, config=cfg)
        checks = fw.run_all()
        result = FrameworkResult(framework=fw_enum, checks=checks)
        results.append(result)
    return AuditReport(target=target, frameworks=results)


def run_single_check(check_id: str, target: str) -> CheckResult | None:
    """Run a single check by ID across all frameworks."""
    cfg = EthicsCheckConfig()
    for fw_class in FRAMEWORK_MAP.values():
        fw = fw_class(target=target, config=cfg)
        result = fw.run_check(check_id)
        if result is not None:
            return result
    return None


def get_all_checks() -> list[dict[str, Any]]:
    """Return metadata for all registered checks."""
    cfg = EthicsCheckConfig()
    all_checks: list[dict[str, Any]] = []
    for fw_enum, fw_class in FRAMEWORK_MAP.items():
        fw = fw_class(target=".", config=cfg)
        for meta in fw.check_metadata():
            meta["framework"] = fw_enum.value
            all_checks.append(meta)
    return all_checks
