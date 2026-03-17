"""Abstract base class for all compliance frameworks."""
from __future__ import annotations
import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any
from ..config import EthicsCheckConfig
from ..models import CheckResult, CheckStatus, Severity


class BaseFramework(ABC):
    """Base class for all EthicsCheck compliance frameworks."""

    def __init__(self, target: str, config: EthicsCheckConfig) -> None:
        self.target = Path(target)
        self.config = config

    def run_all(self) -> list[CheckResult]:
        """Run all checks for this framework, skipping those in config.skip_checks."""
        results = []
        for meta in self.check_metadata():
            if meta["id"] in self.config.skip_checks:
                result = self._make_skipped(meta)
            else:
                result = self.run_check(meta["id"])
                if result is None:
                    result = self._make_skipped(meta)
            results.append(result)
        return results

    @abstractmethod
    def run_check(self, check_id: str) -> CheckResult | None:
        """Run a specific check by ID. Return None if ID not found."""

    @abstractmethod
    def check_metadata(self) -> list[dict[str, Any]]:
        """Return list of {id, title, ref, severity} dicts for all checks."""

    def _make_skipped(self, meta: dict[str, Any]) -> CheckResult:
        from ..models import Framework
        return CheckResult(
            check_id=meta["id"],
            title=meta["title"],
            description=meta.get("description", ""),
            status=CheckStatus.SKIP,
            severity=Severity(meta["severity"]),
            framework=Framework(meta["framework"]) if "framework" in meta else Framework.EU_AI_ACT,
            article_ref=meta.get("ref", ""),
            remediation="",
        )

    # ── Utility helpers ──────────────────────────────────────────────────────

    def _file_exists(self, *relative_paths: str) -> tuple[bool, str]:
        """Check if any of the given relative paths exist under the target."""
        for rp in relative_paths:
            candidate = self.target / rp
            if candidate.exists():
                return True, str(candidate)
        return False, ""

    def _scan_for_keywords(self, keywords: list[str], extensions: list[str] | None = None) -> list[str]:
        """Walk target directory and return files containing any of the keywords."""
        hits: list[str] = []
        exts = set(extensions or [".md", ".txt", ".rst", ".yaml", ".yml", ".json", ".toml"])
        for root, _, files in os.walk(self.target):
            for fname in files:
                if Path(fname).suffix.lower() in exts:
                    fpath = Path(root) / fname
                    try:
                        text = fpath.read_text(errors="ignore").lower()
                        if any(kw.lower() in text for kw in keywords):
                            hits.append(str(fpath))
                    except OSError:
                        pass
        return hits

    def _pass(self, check_id: str, title: str, description: str, ref: str,
              severity: Severity, framework: Any, evidence: list[str] | None = None,
              details: dict[str, Any] | None = None) -> CheckResult:
        return CheckResult(
            check_id=check_id, title=title, description=description,
            status=CheckStatus.PASS, severity=severity, framework=framework,
            article_ref=ref, evidence=evidence or [], details=details or {},
        )

    def _fail(self, check_id: str, title: str, description: str, ref: str,
              severity: Severity, framework: Any, remediation: str = "",
              details: dict[str, Any] | None = None) -> CheckResult:
        return CheckResult(
            check_id=check_id, title=title, description=description,
            status=CheckStatus.FAIL, severity=severity, framework=framework,
            article_ref=ref, remediation=remediation, details=details or {},
        )

    def _warn(self, check_id: str, title: str, description: str, ref: str,
              severity: Severity, framework: Any, evidence: list[str] | None = None,
              remediation: str = "") -> CheckResult:
        return CheckResult(
            check_id=check_id, title=title, description=description,
            status=CheckStatus.WARN, severity=severity, framework=framework,
            article_ref=ref, evidence=evidence or [], remediation=remediation,
        )
