"""Orchestrates compliance checks across frameworks."""
from __future__ import annotations
from typing import Any
from .config import EthicsCheckConfig
from .models import AuditReport, FrameworkResult, Framework, CheckResult
from .frameworks.eu_ai_act import EUAIActFramework
from .frameworks.nist_rmf import NISTRMFFramework
from .frameworks.iso_42001 import ISO42001Framework
from .plugins import discover_plugins

# Built-in frameworks — always present regardless of installed plugins.
_BUILTIN_FRAMEWORKS = {
    Framework.EU_AI_ACT: EUAIActFramework,
    Framework.NIST_RMF: NISTRMFFramework,
    Framework.ISO_42001: ISO42001Framework,
}


def build_framework_map() -> dict[Any, Any]:
    """Return the full framework map: built-ins merged with installed plugins.

    Built-in frameworks always take precedence — a plugin cannot override
    ``eu-ai-act``, ``nist-rmf``, or ``iso-42001``.
    """
    framework_map: dict[Any, Any] = {}
    # Load plugins first so built-ins can override if names collide.
    framework_map.update(discover_plugins())
    framework_map.update(_BUILTIN_FRAMEWORKS)
    return framework_map


def run_audit(target: str, cfg: EthicsCheckConfig) -> AuditReport:
    """Run all configured frameworks against the target.

    Built-in frameworks (eu-ai-act, nist-rmf, iso-42001) run according to
    ``cfg.frameworks``.  Installed plugin frameworks (those with string keys
    not in the built-in set) are always run automatically — opting in happens
    at install time, not at config time.
    """
    framework_map = build_framework_map()
    results: list[FrameworkResult] = []

    # 1. Run configured built-in frameworks.
    for fw_enum in cfg.frameworks:
        fw_class = framework_map.get(fw_enum)
        if fw_class is None:
            continue
        fw = fw_class(target=target, config=cfg)
        checks = fw.run_all()
        results.append(FrameworkResult(framework=fw_enum, checks=checks))

    # 2. Auto-run any installed plugin frameworks (string keys, not Framework enum).
    builtin_keys = set(_BUILTIN_FRAMEWORKS.keys())
    for fw_key, fw_class in framework_map.items():
        if fw_key not in builtin_keys:
            fw = fw_class(target=target, config=cfg)
            checks = fw.run_all()
            results.append(FrameworkResult(framework=fw_key, checks=checks))

    return AuditReport(target=target, frameworks=results)


def run_single_check(check_id: str, target: str) -> CheckResult | None:
    """Run a single check by ID across all frameworks."""
    cfg = EthicsCheckConfig()
    framework_map = build_framework_map()
    for fw_class in framework_map.values():
        fw = fw_class(target=target, config=cfg)
        result = fw.run_check(check_id)
        if result is not None:
            return result
    return None


def get_all_checks() -> list[dict[str, Any]]:
    """Return metadata for all registered checks (built-ins + plugins)."""
    cfg = EthicsCheckConfig()
    framework_map = build_framework_map()
    all_checks: list[dict[str, Any]] = []
    for fw_enum, fw_class in framework_map.items():
        fw = fw_class(target=".", config=cfg)
        for meta in fw.check_metadata():
            meta["framework"] = fw_enum if isinstance(fw_enum, str) else fw_enum.value
            all_checks.append(meta)
    return all_checks
