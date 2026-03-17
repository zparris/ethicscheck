"""Shared data models for EthicsCheck compliance results."""
from __future__ import annotations
from enum import Enum
from typing import Any
from pydantic import BaseModel, Field
import datetime


class Severity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class CheckStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    WARN = "warn"
    SKIP = "skip"
    NOT_APPLICABLE = "not_applicable"


class Framework(str, Enum):
    EU_AI_ACT = "eu-ai-act"
    NIST_RMF = "nist-rmf"
    ISO_42001 = "iso-42001"


class CheckResult(BaseModel):
    check_id: str
    title: str
    description: str
    status: CheckStatus
    severity: Severity
    framework: Framework
    article_ref: str  # e.g. "Art. 9", "GOVERN 1.1", "Clause 6.1"
    evidence: list[str] = Field(default_factory=list)
    remediation: str = ""
    details: dict[str, Any] = Field(default_factory=dict)


class FrameworkResult(BaseModel):
    framework: Framework
    checks: list[CheckResult]
    passed: int = 0
    failed: int = 0
    warnings: int = 0
    skipped: int = 0
    score: float = 0.0  # 0.0–1.0

    def model_post_init(self, __context: Any) -> None:
        self.passed = sum(1 for c in self.checks if c.status == CheckStatus.PASS)
        self.failed = sum(1 for c in self.checks if c.status == CheckStatus.FAIL)
        self.warnings = sum(1 for c in self.checks if c.status == CheckStatus.WARN)
        self.skipped = sum(1 for c in self.checks if c.status in (CheckStatus.SKIP, CheckStatus.NOT_APPLICABLE))
        total = len(self.checks) - self.skipped
        self.score = self.passed / total if total > 0 else 0.0


class AuditReport(BaseModel):
    tool: str = "EthicsCheck"
    version: str = "0.1.0"
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    target: str  # path/name of what was audited
    frameworks: list[FrameworkResult]
    overall_status: CheckStatus = CheckStatus.PASS
    critical_count: int = 0
    high_count: int = 0
    summary: str = ""

    def model_post_init(self, __context: Any) -> None:
        all_checks = [c for fr in self.frameworks for c in fr.checks]
        self.critical_count = sum(1 for c in all_checks if c.severity == Severity.CRITICAL and c.status == CheckStatus.FAIL)
        self.high_count = sum(1 for c in all_checks if c.severity == Severity.HIGH and c.status == CheckStatus.FAIL)
        any_fail = any(c.status == CheckStatus.FAIL for c in all_checks)
        self.overall_status = CheckStatus.FAIL if any_fail else CheckStatus.PASS

    def exit_code(self, fail_on: str = "high") -> int:
        """Return 0 for success, 1 for failure based on --fail-on threshold."""
        severity_order = [s.value for s in Severity]
        threshold_idx = severity_order.index(fail_on) if fail_on in severity_order else 1
        all_checks = [c for fr in self.frameworks for c in fr.checks]
        for check in all_checks:
            if check.status == CheckStatus.FAIL:
                check_idx = severity_order.index(check.severity.value)
                if check_idx <= threshold_idx:
                    return 1
        return 0
