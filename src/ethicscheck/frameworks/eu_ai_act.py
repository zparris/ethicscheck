"""EU AI Act compliance checks — Articles 8–15 and Annex IV.

Enforcement dates:
  - GPAI obligations: August 2, 2025 (already in force)
  - High-risk (Annex III): August 2, 2026
  - High-risk embedded in Annex I products: August 2, 2027
"""
from __future__ import annotations
from typing import Any
from ..models import CheckResult, Framework, Severity
from .base import BaseFramework

_FW = Framework.EU_AI_ACT


class EUAIActFramework(BaseFramework):
    """EU AI Act (Regulation EU 2024/1689) compliance checks."""

    def check_metadata(self) -> list[dict[str, Any]]:
        return [
            # Article 9 — Risk Management
            {"id": "EU-ART9-001", "title": "Risk management system documented", "ref": "Art. 9(1)", "severity": "critical", "description": "A continuous, iterative risk management system must be established and maintained throughout the AI system lifecycle."},
            {"id": "EU-ART9-002", "title": "Known and foreseeable risks identified", "ref": "Art. 9(2)(a)", "severity": "high", "description": "All known and reasonably foreseeable risks associated with the AI system must be identified and documented."},
            {"id": "EU-ART9-003", "title": "Risk estimation under foreseeable misuse", "ref": "Art. 9(2)(b)", "severity": "high", "description": "Risks must be estimated under both intended use and reasonably foreseeable misuse conditions."},
            {"id": "EU-ART9-004", "title": "Risk mitigation measures adopted", "ref": "Art. 9(2)(d)", "severity": "high", "description": "Appropriate risk mitigation and control measures must be adopted and documented."},
            {"id": "EU-ART9-005", "title": "Pre-deployment testing against defined thresholds", "ref": "Art. 9(6)–(7)", "severity": "critical", "description": "Testing must be performed against prior-defined metrics and probabilistic thresholds before deployment and under real-world conditions."},
            # Article 10 — Data Governance
            {"id": "EU-ART10-001", "title": "Data governance practices documented", "ref": "Art. 10(2)", "severity": "high", "description": "Data governance covering collection processes, data origin, and preparation operations must be documented."},
            {"id": "EU-ART10-002", "title": "Training data relevance and representativeness", "ref": "Art. 10(2)(f)", "severity": "high", "description": "Training, validation, and testing datasets must be relevant, representative, and free of errors to the best extent possible."},
            {"id": "EU-ART10-003", "title": "Bias examination performed", "ref": "Art. 10(2)(f)", "severity": "critical", "description": "Datasets must be examined for possible biases that could affect health, safety, and fundamental rights."},
            {"id": "EU-ART10-004", "title": "Data gap identification documented", "ref": "Art. 10(2)(g)", "severity": "medium", "description": "Any gaps in the data and how those gaps are addressed must be documented."},
            # Article 11 — Technical Documentation
            {"id": "EU-ART11-001", "title": "Technical documentation exists (Annex IV)", "ref": "Art. 11(1)", "severity": "critical", "description": "Comprehensive technical documentation per Annex IV must be drawn up before market placement."},
            {"id": "EU-ART11-002", "title": "General system description present", "ref": "Annex IV §1", "severity": "high", "description": "Documentation must include intended purpose, provider identity, version, hardware/software interactions, and UI description."},
            {"id": "EU-ART11-003", "title": "Development process documented", "ref": "Annex IV §2", "severity": "high", "description": "Design specifications, architecture, data requirements, validation and testing procedures with signed test logs must be present."},
            {"id": "EU-ART11-004", "title": "Performance metrics and limitations documented", "ref": "Annex IV §3", "severity": "medium", "description": "Performance capabilities and limitations, foreseeable unintended outcomes, and human oversight measures must be documented."},
            {"id": "EU-ART11-005", "title": "Lifecycle changes documented", "ref": "Annex IV §6", "severity": "medium", "description": "All changes throughout the AI system lifecycle must be described and documented."},
            # Article 12 — Logging
            {"id": "EU-ART12-001", "title": "Automatic logging capability implemented", "ref": "Art. 12(1)", "severity": "high", "description": "AI systems must automatically record events throughout their operational lifetime to enable monitoring."},
            {"id": "EU-ART12-002", "title": "Logging system documented and verified", "ref": "Art. 12, Annex IV §2", "severity": "high", "description": "The logging system must be documented, tested, and its functionality verified before deployment."},
            # Article 13 — Transparency
            {"id": "EU-ART13-001", "title": "Instructions for use documented", "ref": "Art. 13(1)", "severity": "high", "description": "Clear instructions for use must accompany the AI system, covering intended purpose, accuracy levels, and known risks."},
            {"id": "EU-ART13-002", "title": "Accuracy and robustness metrics declared", "ref": "Art. 13(3)(b)(ii)", "severity": "high", "description": "Accuracy levels, robustness, and cybersecurity measures must be declared with reference to appropriate metrics."},
            {"id": "EU-ART13-003", "title": "Known risks and limitations disclosed", "ref": "Art. 13(3)(b)(iii)", "severity": "high", "description": "Known and foreseeable risks and limitations must be disclosed in user-facing documentation."},
            # Article 14 — Human Oversight
            {"id": "EU-ART14-001", "title": "Human oversight mechanism designed and documented", "ref": "Art. 14(1)", "severity": "critical", "description": "High-risk AI systems must be designed to enable effective human oversight during operation."},
            {"id": "EU-ART14-002", "title": "Override/stop capability implemented", "ref": "Art. 14(4)(e)", "severity": "critical", "description": "Oversight personnel must have the ability to override, reverse, or stop the AI system."},
            {"id": "EU-ART14-003", "title": "Automation bias awareness documented", "ref": "Art. 14(4)(b)", "severity": "medium", "description": "Human overseers must be informed about automation bias risks and how to mitigate them."},
            # Article 15 — Accuracy, Robustness, Cybersecurity
            {"id": "EU-ART15-001", "title": "Accuracy metrics declared with specific values", "ref": "Art. 15(1)", "severity": "high", "description": "Declared accuracy levels with specified metrics relevant to the intended purpose must be documented."},
            {"id": "EU-ART15-002", "title": "Robustness testing performed", "ref": "Art. 15(3)–(4)", "severity": "high", "description": "Testing for resilience against errors, faults, and inconsistencies must be performed and documented."},
            {"id": "EU-ART15-003", "title": "Cybersecurity measures documented", "ref": "Art. 15(5)", "severity": "high", "description": "Technical measures against data poisoning, adversarial attacks, model extraction/inversion must be documented."},
            {"id": "EU-ART15-004", "title": "Feedback loop mitigations for continually learning systems", "ref": "Art. 15(4)", "severity": "medium", "description": "For continually learning AI systems, technical measures against undesirable feedback loops must be implemented."},
            # Annex IV — Declaration of Conformity
            {"id": "EU-ANNIV-001", "title": "EU Declaration of Conformity prepared", "ref": "Art. 47, Annex IV §8", "severity": "critical", "description": "An EU Declaration of Conformity per Article 47 must be prepared before market placement."},
            {"id": "EU-ANNIV-002", "title": "Post-market monitoring plan in place", "ref": "Art. 72, Annex IV §9", "severity": "high", "description": "A post-market monitoring system per Article 72 must be established and documented."},
            # GPAI provisions (in force Aug 2, 2025)
            {"id": "EU-GPAI-001", "title": "GPAI technical documentation maintained (Annex XI)", "ref": "Art. 53(1)(a), Annex XI", "severity": "high", "description": "For general-purpose AI models, technical documentation per Annex XI must be maintained and kept up to date."},
            {"id": "EU-GPAI-002", "title": "GPAI training data summary published (Annex XII)", "ref": "Art. 53(1)(d), Annex XII", "severity": "high", "description": "A summary about training data content used to train the GPAI model must be made publicly available."},
            {"id": "EU-GPAI-003", "title": "GPAI copyright compliance policy documented", "ref": "Art. 53(1)(c)", "severity": "high", "description": "A policy for complying with EU copyright law, including text and data mining opt-outs, must be documented."},
        ]

    def run_check(self, check_id: str) -> CheckResult | None:  # noqa: PLR0911
        """Dispatch to individual check methods."""
        dispatch = {
            # Art. 9
            "EU-ART9-001": self._check_risk_management_system,
            "EU-ART9-002": self._check_risks_identified,
            "EU-ART9-003": self._check_misuse_estimation,
            "EU-ART9-004": self._check_mitigation_measures,
            "EU-ART9-005": self._check_pre_deployment_testing,
            # Art. 10
            "EU-ART10-001": self._check_data_governance_docs,
            "EU-ART10-002": self._check_data_representativeness,
            "EU-ART10-003": self._check_bias_examination,
            "EU-ART10-004": self._check_data_gap_identification,
            # Art. 11 / Annex IV
            "EU-ART11-001": self._check_technical_documentation,
            "EU-ART11-002": self._check_system_description,
            "EU-ART11-003": self._check_development_process_docs,
            "EU-ART11-004": self._check_performance_metrics_docs,
            "EU-ART11-005": self._check_lifecycle_changes_docs,
            # Art. 12
            "EU-ART12-001": self._check_logging_capability,
            "EU-ART12-002": self._check_logging_verified,
            # Art. 13
            "EU-ART13-001": self._check_instructions_for_use,
            "EU-ART13-002": self._check_accuracy_declared,
            "EU-ART13-003": self._check_risks_disclosed,
            # Art. 14
            "EU-ART14-001": self._check_human_oversight_mechanism,
            "EU-ART14-002": self._check_override_capability,
            "EU-ART14-003": self._check_automation_bias_awareness,
            # Art. 15
            "EU-ART15-001": self._check_accuracy_metrics,
            "EU-ART15-002": self._check_robustness_testing,
            "EU-ART15-003": self._check_cybersecurity_measures,
            "EU-ART15-004": self._check_feedback_loop_mitigations,
            # Annex IV
            "EU-ANNIV-001": self._check_declaration_of_conformity,
            "EU-ANNIV-002": self._check_post_market_monitoring,
            # GPAI
            "EU-GPAI-001": self._check_gpai_technical_docs,
            "EU-GPAI-002": self._check_gpai_training_summary,
            "EU-GPAI-003": self._check_gpai_copyright_policy,
        }
        fn = dispatch.get(check_id)
        return fn() if fn else None

    # ── Article 9 checks ─────────────────────────────────────────────────────

    def _check_risk_management_system(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/risk_assessment.md", "risk_assessment.md",
            "docs/risk_management.md", "risk_management.md",
            "docs/risk_management.yaml", "risk_management.yaml",
        )
        if not exists:
            files = self._scan_for_keywords(["risk management", "risk assessment", "risk identification"])
            if files:
                return self._warn(
                    "EU-ART9-001", "Risk management system documented",
                    "Risk management content found in project files but no dedicated risk assessment document.",
                    "Art. 9(1)", Severity.CRITICAL, _FW,
                    evidence=files[:3],
                    remediation="Create a dedicated risk_assessment.md or risk_management.yaml document covering all Art. 9 requirements.",
                )
            return self._fail(
                "EU-ART9-001", "Risk management system documented",
                "No risk management system documentation found.",
                "Art. 9(1)", Severity.CRITICAL, _FW,
                remediation="Create docs/risk_assessment.md covering: risk identification, estimation under misuse, mitigation measures, and testing thresholds.",
            )
        return self._pass(
            "EU-ART9-001", "Risk management system documented",
            "Risk management documentation found.",
            "Art. 9(1)", Severity.CRITICAL, _FW, evidence=[path],
        )

    def _check_risks_identified(self) -> CheckResult:
        files = self._scan_for_keywords(["foreseeable risk", "known risk", "risk identification", "risk catalogue", "risk register"])
        if files:
            return self._pass("EU-ART9-002", "Known and foreseeable risks identified",
                              "Risk identification documentation found.", "Art. 9(2)(a)", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART9-002", "Known and foreseeable risks identified",
                          "No evidence of systematic risk identification found.",
                          "Art. 9(2)(a)", Severity.HIGH, _FW,
                          remediation="Document all known and reasonably foreseeable risks in your risk register.")

    def _check_misuse_estimation(self) -> CheckResult:
        files = self._scan_for_keywords(["misuse", "foreseeable misuse", "unintended use", "off-label"])
        if files:
            return self._pass("EU-ART9-003", "Risk estimation under foreseeable misuse",
                              "Misuse scenarios found in documentation.", "Art. 9(2)(b)", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART9-003", "Risk estimation under foreseeable misuse",
                          "No foreseeable misuse scenarios documented.",
                          "Art. 9(2)(b)", Severity.HIGH, _FW,
                          remediation="Add a 'Foreseeable Misuse' section to your risk assessment documenting potential misuse scenarios and their risk estimates.")

    def _check_mitigation_measures(self) -> CheckResult:
        files = self._scan_for_keywords(["mitigation", "risk control", "safeguard", "countermeasure"])
        if files:
            return self._pass("EU-ART9-004", "Risk mitigation measures adopted",
                              "Mitigation measures found in documentation.", "Art. 9(2)(d)", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART9-004", "Risk mitigation measures adopted",
                          "No risk mitigation measures documented.",
                          "Art. 9(2)(d)", Severity.HIGH, _FW,
                          remediation="Document concrete mitigation measures for each identified risk.")

    def _check_pre_deployment_testing(self) -> CheckResult:
        files = self._scan_for_keywords(["test log", "test results", "validation results", "threshold", "pre-deployment test"])
        if files:
            return self._pass("EU-ART9-005", "Pre-deployment testing against defined thresholds",
                              "Testing documentation found.", "Art. 9(6)–(7)", Severity.CRITICAL, _FW, evidence=files[:3])
        return self._fail("EU-ART9-005", "Pre-deployment testing against defined thresholds",
                          "No pre-deployment testing records found.",
                          "Art. 9(6)–(7)", Severity.CRITICAL, _FW,
                          remediation="Create signed/dated test logs showing testing against prior-defined metrics and thresholds under real-world conditions.")

    # ── Article 10 checks ────────────────────────────────────────────────────

    def _check_data_governance_docs(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/data_governance.md", "data_governance.md",
            "docs/data_card.md", "data_card.md",
            "docs/datasheet.md", "datasheet.md",
        )
        if exists:
            return self._pass("EU-ART10-001", "Data governance practices documented",
                              "Data governance document found.", "Art. 10(2)", Severity.HIGH, _FW, evidence=[path])
        files = self._scan_for_keywords(["data governance", "data provenance", "data collection", "data origin"])
        if files:
            return self._warn("EU-ART10-001", "Data governance practices documented",
                              "Data governance content found but no dedicated document.",
                              "Art. 10(2)", Severity.HIGH, _FW, evidence=files[:3],
                              remediation="Create a dedicated data governance document (e.g., docs/data_governance.md or a datasheet).")
        return self._fail("EU-ART10-001", "Data governance practices documented",
                          "No data governance documentation found.",
                          "Art. 10(2)", Severity.HIGH, _FW,
                          remediation="Create docs/data_governance.md covering: data origin, collection process, labelling procedures, and quality assessment.")

    def _check_data_representativeness(self) -> CheckResult:
        files = self._scan_for_keywords(["representative", "training data", "validation data", "test data", "data distribution"])
        if files:
            return self._pass("EU-ART10-002", "Training data relevance and representativeness",
                              "Data representativeness documentation found.", "Art. 10(2)(f)", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART10-002", "Training data relevance and representativeness",
                          "No documentation of training data relevance or representativeness found.",
                          "Art. 10(2)(f)", Severity.HIGH, _FW,
                          remediation="Document how training/validation/test datasets are relevant and representative for the intended use case.")

    def _check_bias_examination(self) -> CheckResult:
        files = self._scan_for_keywords(["bias", "fairness", "demographic parity", "disparate impact", "protected attribute", "subgroup"])
        if files:
            return self._pass("EU-ART10-003", "Bias examination performed",
                              "Bias examination evidence found.", "Art. 10(2)(f)", Severity.CRITICAL, _FW, evidence=files[:3])
        return self._fail("EU-ART10-003", "Bias examination performed",
                          "No bias examination documentation found.",
                          "Art. 10(2)(f)", Severity.CRITICAL, _FW,
                          remediation="Conduct and document a bias examination covering relevant demographic sub-groups. Consider tools like IBM AI Fairness 360 or Fairlearn.")

    def _check_data_gap_identification(self) -> CheckResult:
        files = self._scan_for_keywords(["data gap", "missing data", "data limitation", "coverage gap"])
        if files:
            return self._pass("EU-ART10-004", "Data gap identification documented",
                              "Data gap documentation found.", "Art. 10(2)(g)", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("EU-ART10-004", "Data gap identification documented",
                          "No explicit data gap documentation found.",
                          "Art. 10(2)(g)", Severity.MEDIUM, _FW,
                          remediation="Add a 'Data Gaps and Limitations' section to your data governance documentation.")

    # ── Article 11 / Annex IV checks ─────────────────────────────────────────

    def _check_technical_documentation(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/technical_documentation.md", "technical_documentation.md",
            "docs/technical_doc.md", "technical_doc.md",
            "docs/annex_iv.md", "annex_iv.md",
        )
        if exists:
            return self._pass("EU-ART11-001", "Technical documentation exists (Annex IV)",
                              "Technical documentation found.", "Art. 11(1)", Severity.CRITICAL, _FW, evidence=[path])
        files = self._scan_for_keywords(["technical documentation", "annex iv", "system description", "intended purpose"])
        if files:
            return self._warn("EU-ART11-001", "Technical documentation exists (Annex IV)",
                              "Some technical documentation content found but no dedicated Annex IV document.",
                              "Art. 11(1)", Severity.CRITICAL, _FW, evidence=files[:3],
                              remediation="Create a comprehensive technical documentation file covering all nine Annex IV categories.")
        return self._fail("EU-ART11-001", "Technical documentation exists (Annex IV)",
                          "No Annex IV technical documentation found.",
                          "Art. 11(1)", Severity.CRITICAL, _FW,
                          remediation="Create docs/technical_documentation.md with all nine Annex IV sections: general description, development process, monitoring, performance metrics, risk management, lifecycle changes, harmonised standards, Declaration of Conformity, and post-market monitoring.")

    def _check_system_description(self) -> CheckResult:
        files = self._scan_for_keywords(["intended purpose", "intended use", "system description", "provider", "version"])
        if files:
            return self._pass("EU-ART11-002", "General system description present",
                              "System description found.", "Annex IV §1", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART11-002", "General system description present",
                          "No general system description found.",
                          "Annex IV §1", Severity.HIGH, _FW,
                          remediation="Document: intended purpose, provider identity, version number, hardware/software requirements, and user interface description.")

    def _check_development_process_docs(self) -> CheckResult:
        files = self._scan_for_keywords(["architecture", "algorithm", "design specification", "training procedure", "validation procedure", "test log"])
        if files:
            return self._pass("EU-ART11-003", "Development process documented",
                              "Development process documentation found.", "Annex IV §2", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART11-003", "Development process documented",
                          "No development process documentation found.",
                          "Annex IV §2", Severity.HIGH, _FW,
                          remediation="Document design specifications, system architecture, training methodology, and include dated/signed test logs.")

    def _check_performance_metrics_docs(self) -> CheckResult:
        files = self._scan_for_keywords(["accuracy", "precision", "recall", "f1", "auc", "performance metric", "benchmark"])
        if files:
            return self._pass("EU-ART11-004", "Performance metrics and limitations documented",
                              "Performance metrics found.", "Annex IV §3", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._fail("EU-ART11-004", "Performance metrics and limitations documented",
                          "No performance metrics documentation found.",
                          "Annex IV §3", Severity.MEDIUM, _FW,
                          remediation="Document performance metrics by sub-group, limitations, and known failure modes.")

    def _check_lifecycle_changes_docs(self) -> CheckResult:
        exists, path = self._file_exists("CHANGELOG.md", "CHANGELOG", "CHANGES.md", "docs/changelog.md")
        if exists:
            return self._pass("EU-ART11-005", "Lifecycle changes documented",
                              "Changelog found.", "Annex IV §6", Severity.MEDIUM, _FW, evidence=[path])
        return self._fail("EU-ART11-005", "Lifecycle changes documented",
                          "No CHANGELOG or lifecycle changes documentation found.",
                          "Annex IV §6", Severity.MEDIUM, _FW,
                          remediation="Create a CHANGELOG.md documenting all changes to the AI system throughout its lifecycle.")

    # ── Article 12 checks ────────────────────────────────────────────────────

    def _check_logging_capability(self) -> CheckResult:
        files = self._scan_for_keywords(["logging", "audit log", "event log", "log record"])
        if files:
            return self._pass("EU-ART12-001", "Automatic logging capability implemented",
                              "Logging capability evidence found.", "Art. 12(1)", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART12-001", "Automatic logging capability implemented",
                          "No logging capability documentation found.",
                          "Art. 12(1)", Severity.HIGH, _FW,
                          remediation="Implement and document automatic event logging covering the AI system's operational lifetime.")

    def _check_logging_verified(self) -> CheckResult:
        files = self._scan_for_keywords(["logging test", "log verification", "log system test", "logging verified"])
        if files:
            return self._pass("EU-ART12-002", "Logging system documented and verified",
                              "Logging verification found.", "Art. 12, Annex IV §2", Severity.HIGH, _FW, evidence=files[:3])
        return self._warn("EU-ART12-002", "Logging system documented and verified",
                          "No evidence of logging system verification found.",
                          "Art. 12, Annex IV §2", Severity.HIGH, _FW,
                          remediation="Add logging system verification to your test suite and include test results in technical documentation.")

    # ── Article 13 checks ────────────────────────────────────────────────────

    def _check_instructions_for_use(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/instructions_for_use.md", "instructions_for_use.md",
            "docs/user_guide.md", "user_guide.md",
            "README.md",
        )
        if exists:
            return self._pass("EU-ART13-001", "Instructions for use documented",
                              "Instructions for use found.", "Art. 13(1)", Severity.HIGH, _FW, evidence=[path])
        return self._fail("EU-ART13-001", "Instructions for use documented",
                          "No instructions for use found.",
                          "Art. 13(1)", Severity.HIGH, _FW,
                          remediation="Create user-facing documentation covering: intended purpose, accuracy levels, known risks, computational requirements, and human oversight measures.")

    def _check_accuracy_declared(self) -> CheckResult:
        files = self._scan_for_keywords(["accuracy", "robustness", "cybersecurity level", "declared performance"])
        if files:
            return self._pass("EU-ART13-002", "Accuracy and robustness metrics declared",
                              "Accuracy declarations found.", "Art. 13(3)(b)(ii)", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART13-002", "Accuracy and robustness metrics declared",
                          "No declared accuracy or robustness metrics found.",
                          "Art. 13(3)(b)(ii)", Severity.HIGH, _FW,
                          remediation="Declare specific accuracy metrics with numerical values in your technical documentation and instructions for use.")

    def _check_risks_disclosed(self) -> CheckResult:
        files = self._scan_for_keywords(["known risk", "known limitation", "risk disclosure", "limitation", "caveat"])
        if files:
            return self._pass("EU-ART13-003", "Known risks and limitations disclosed",
                              "Risk disclosure found.", "Art. 13(3)(b)(iii)", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART13-003", "Known risks and limitations disclosed",
                          "No risk or limitation disclosure found.",
                          "Art. 13(3)(b)(iii)", Severity.HIGH, _FW,
                          remediation="Add an explicit 'Known Risks and Limitations' section to user-facing documentation.")

    # ── Article 14 checks ────────────────────────────────────────────────────

    def _check_human_oversight_mechanism(self) -> CheckResult:
        files = self._scan_for_keywords(["human oversight", "human-in-the-loop", "hitl", "human review", "oversight mechanism"])
        if files:
            return self._pass("EU-ART14-001", "Human oversight mechanism designed and documented",
                              "Human oversight documentation found.", "Art. 14(1)", Severity.CRITICAL, _FW, evidence=files[:3])
        return self._fail("EU-ART14-001", "Human oversight mechanism designed and documented",
                          "No human oversight mechanism documentation found.",
                          "Art. 14(1)", Severity.CRITICAL, _FW,
                          remediation="Document the human oversight mechanism: who oversees the system, how they are trained, and what actions they can take.")

    def _check_override_capability(self) -> CheckResult:
        files = self._scan_for_keywords(["override", "stop", "halt", "interrupt", "kill switch", "human control"])
        if files:
            return self._pass("EU-ART14-002", "Override/stop capability implemented",
                              "Override capability documentation found.", "Art. 14(4)(e)", Severity.CRITICAL, _FW, evidence=files[:3])
        return self._fail("EU-ART14-002", "Override/stop capability implemented",
                          "No documentation of override or stop capability found.",
                          "Art. 14(4)(e)", Severity.CRITICAL, _FW,
                          remediation="Implement and document the ability for human overseers to override, reverse, or stop the AI system.")

    def _check_automation_bias_awareness(self) -> CheckResult:
        files = self._scan_for_keywords(["automation bias", "over-reliance", "algorithmic bias awareness", "human override training"])
        if files:
            return self._pass("EU-ART14-003", "Automation bias awareness documented",
                              "Automation bias awareness found.", "Art. 14(4)(b)", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("EU-ART14-003", "Automation bias awareness documented",
                          "No automation bias awareness documentation found.",
                          "Art. 14(4)(b)", Severity.MEDIUM, _FW,
                          remediation="Add guidance on automation bias risks to oversight personnel training materials.")

    # ── Article 15 checks ────────────────────────────────────────────────────

    def _check_accuracy_metrics(self) -> CheckResult:
        files = self._scan_for_keywords(["accuracy:", "accuracy =", "f1 score", "precision:", "recall:", "auc:", "rmse:", "mae:"])
        if files:
            return self._pass("EU-ART15-001", "Accuracy metrics declared with specific values",
                              "Specific accuracy metric values found.", "Art. 15(1)", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART15-001", "Accuracy metrics declared with specific values",
                          "No specific accuracy metric values found in documentation.",
                          "Art. 15(1)", Severity.HIGH, _FW,
                          remediation="Declare specific numerical accuracy values (e.g., 'accuracy: 94.2% on test set') in your technical documentation.")

    def _check_robustness_testing(self) -> CheckResult:
        files = self._scan_for_keywords(["robustness", "adversarial", "edge case", "stress test", "fault tolerance", "resilience"])
        if files:
            return self._pass("EU-ART15-002", "Robustness testing performed",
                              "Robustness testing documentation found.", "Art. 15(3)–(4)", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART15-002", "Robustness testing performed",
                          "No robustness testing documentation found.",
                          "Art. 15(3)–(4)", Severity.HIGH, _FW,
                          remediation="Conduct and document robustness testing including adversarial examples, edge cases, and error/fault scenarios.")

    def _check_cybersecurity_measures(self) -> CheckResult:
        files = self._scan_for_keywords(["data poisoning", "adversarial attack", "model poisoning", "model extraction", "model inversion", "cybersecurity"])
        if files:
            return self._pass("EU-ART15-003", "Cybersecurity measures documented",
                              "Cybersecurity measure documentation found.", "Art. 15(5)", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ART15-003", "Cybersecurity measures documented",
                          "No cybersecurity measures documentation found.",
                          "Art. 15(5)", Severity.HIGH, _FW,
                          remediation="Document technical measures protecting against: data poisoning, adversarial attacks, model extraction, and model inversion attacks.")

    def _check_feedback_loop_mitigations(self) -> CheckResult:
        files = self._scan_for_keywords(["feedback loop", "continual learning", "online learning", "distribution shift", "concept drift"])
        if files:
            return self._pass("EU-ART15-004", "Feedback loop mitigations documented",
                              "Feedback loop mitigation documentation found.", "Art. 15(4)", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("EU-ART15-004", "Feedback loop mitigations for continually learning systems",
                          "No feedback loop mitigation documentation found (may not apply if system does not continually learn).",
                          "Art. 15(4)", Severity.MEDIUM, _FW,
                          remediation="If the system continually learns in production, document measures to prevent undesirable feedback loops.")

    # ── Annex IV checks ──────────────────────────────────────────────────────

    def _check_declaration_of_conformity(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/declaration_of_conformity.md", "declaration_of_conformity.md",
            "docs/eu_doc.md", "docs/conformity.md",
        )
        if exists:
            return self._pass("EU-ANNIV-001", "EU Declaration of Conformity prepared",
                              "Declaration of Conformity document found.", "Art. 47, Annex IV §8", Severity.CRITICAL, _FW, evidence=[path])
        return self._fail("EU-ANNIV-001", "EU Declaration of Conformity prepared",
                          "No EU Declaration of Conformity found.",
                          "Art. 47, Annex IV §8", Severity.CRITICAL, _FW,
                          remediation="Prepare an EU Declaration of Conformity per Article 47 before placing the system on the EU market.")

    def _check_post_market_monitoring(self) -> CheckResult:
        files = self._scan_for_keywords(["post-market monitoring", "post market monitoring", "market surveillance", "incident reporting"])
        if files:
            return self._pass("EU-ANNIV-002", "Post-market monitoring plan in place",
                              "Post-market monitoring documentation found.", "Art. 72, Annex IV §9", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("EU-ANNIV-002", "Post-market monitoring plan in place",
                          "No post-market monitoring plan found.",
                          "Art. 72, Annex IV §9", Severity.HIGH, _FW,
                          remediation="Create a post-market monitoring plan per Article 72 covering: data collection, evaluation periods, and serious incident reporting procedures.")

    # ── GPAI checks ──────────────────────────────────────────────────────────

    def _check_gpai_technical_docs(self) -> CheckResult:
        files = self._scan_for_keywords(["gpai", "general purpose ai", "foundation model", "large language model", "annex xi"])
        if files:
            return self._pass("EU-GPAI-001", "GPAI technical documentation maintained (Annex XI)",
                              "GPAI documentation found.", "Art. 53(1)(a), Annex XI", Severity.HIGH, _FW, evidence=files[:3])
        return self._warn("EU-GPAI-001", "GPAI technical documentation maintained (Annex XI)",
                          "No GPAI-specific documentation found (may not apply if not a GPAI model provider).",
                          "Art. 53(1)(a), Annex XI", Severity.HIGH, _FW,
                          remediation="If providing a GPAI model, maintain technical documentation per Annex XI (in force August 2, 2025).")

    def _check_gpai_training_summary(self) -> CheckResult:
        files = self._scan_for_keywords(["training data summary", "training data content", "data summary", "annex xii"])
        if files:
            return self._pass("EU-GPAI-002", "GPAI training data summary published (Annex XII)",
                              "Training data summary found.", "Art. 53(1)(d), Annex XII", Severity.HIGH, _FW, evidence=files[:3])
        return self._warn("EU-GPAI-002", "GPAI training data summary published (Annex XII)",
                          "No GPAI training data summary found (may not apply if not a GPAI model provider).",
                          "Art. 53(1)(d), Annex XII", Severity.HIGH, _FW,
                          remediation="If providing a GPAI model, publish a training data content summary per Annex XII.")

    def _check_gpai_copyright_policy(self) -> CheckResult:
        files = self._scan_for_keywords(["copyright", "text and data mining", "tdm opt-out", "copyright compliance", "intellectual property"])
        if files:
            return self._pass("EU-GPAI-003", "GPAI copyright compliance policy documented",
                              "Copyright policy documentation found.", "Art. 53(1)(c)", Severity.HIGH, _FW, evidence=files[:3])
        return self._warn("EU-GPAI-003", "GPAI copyright compliance policy documented",
                          "No copyright compliance policy found (may not apply if not a GPAI model provider).",
                          "Art. 53(1)(c)", Severity.HIGH, _FW,
                          remediation="If providing a GPAI model, document your EU copyright compliance policy including text and data mining opt-out procedures.")
