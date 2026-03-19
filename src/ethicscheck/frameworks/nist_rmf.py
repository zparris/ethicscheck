"""NIST AI Risk Management Framework 1.0 compliance checks.

Published January 2023. Four core functions: Govern, Map, Measure, Manage.
Quasi-mandatory for US federal AI deployments under EO 14110 and OMB M-24-10.
"""
from __future__ import annotations

from typing import Any

from ..models import CheckResult, Framework, Severity
from .base import BaseFramework

_FW = Framework.NIST_RMF


class NISTRMFFramework(BaseFramework):
    """NIST AI RMF 1.0 compliance checks."""

    def check_metadata(self) -> list[dict[str, Any]]:
        return [
            # GOVERN
            {"id": "NIST-GOV-001", "title": "AI governance policy documented", "ref": "GOVERN 1.1", "severity": "critical", "description": "An organisational AI policy or governance framework must be established, documented, and communicated to relevant personnel."},
            {"id": "NIST-GOV-002", "title": "AI risk appetite and tolerance defined", "ref": "GOVERN 1.2", "severity": "high", "description": "Organisational risk appetite and tolerance thresholds for AI systems must be defined and documented."},
            {"id": "NIST-GOV-003", "title": "Roles and accountability assigned", "ref": "GOVERN 1.4", "severity": "high", "description": "Clear roles, responsibilities, and accountability structures for AI risk management must be assigned and documented."},
            {"id": "NIST-GOV-004", "title": "Workforce AI risk training documented", "ref": "GOVERN 4.1", "severity": "medium", "description": "Training and awareness programmes on AI risk for relevant workforce members must be documented."},
            {"id": "NIST-GOV-005", "title": "Organisational AI oversight structure exists", "ref": "GOVERN 2.2", "severity": "high", "description": "An organisational structure for AI oversight, including escalation paths, must be established and documented."},
            {"id": "NIST-GOV-006", "title": "Policies address legal, regulatory, and compliance requirements", "ref": "GOVERN 1.7", "severity": "high", "description": "AI governance policies must explicitly address applicable legal, regulatory, and compliance requirements."},
            # MAP
            {"id": "NIST-MAP-001", "title": "Intended use and deployment context documented", "ref": "MAP 1.1", "severity": "critical", "description": "The intended purpose, use cases, and deployment context of the AI system must be clearly documented."},
            {"id": "NIST-MAP-002", "title": "Stakeholder impact assessment performed", "ref": "MAP 1.5", "severity": "high", "description": "An assessment of potential impacts on relevant stakeholders — including affected individuals and communities — must be performed and documented."},
            {"id": "NIST-MAP-003", "title": "AI risk categories identified and catalogued", "ref": "MAP 2.2", "severity": "high", "description": "Risk types relevant to the AI system (e.g., bias, security, explainability, privacy) must be identified and catalogued."},
            {"id": "NIST-MAP-004", "title": "Data provenance and lineage documented", "ref": "MAP 3.5", "severity": "high", "description": "Data provenance, lineage, and quality characteristics relevant to AI system risk must be documented."},
            {"id": "NIST-MAP-005", "title": "Third-party and supply chain AI risks assessed", "ref": "MAP 5.1", "severity": "medium", "description": "Risks associated with third-party AI components, APIs, and supply chain dependencies must be identified and assessed."},
            {"id": "NIST-MAP-006", "title": "Foreseeable negative impacts documented", "ref": "MAP 2.3", "severity": "high", "description": "Foreseeable negative impacts of the AI system on individuals, groups, and society must be documented."},
            # MEASURE
            {"id": "NIST-MEA-001", "title": "Trustworthiness metrics defined and documented", "ref": "MEASURE 1.1", "severity": "high", "description": "Metrics for evaluating AI system trustworthiness characteristics (accuracy, robustness, fairness, explainability) must be defined and documented."},
            {"id": "NIST-MEA-002", "title": "Bias and fairness evaluation performed", "ref": "MEASURE 2.5", "severity": "critical", "description": "Systematic evaluation for bias and fairness across relevant demographic groups must be performed and results documented."},
            {"id": "NIST-MEA-003", "title": "Explainability and interpretability assessed", "ref": "MEASURE 2.6", "severity": "high", "description": "The explainability and interpretability of AI system outputs must be assessed and documented for the deployment context."},
            {"id": "NIST-MEA-004", "title": "Uncertainty and confidence quantified", "ref": "MEASURE 2.3", "severity": "medium", "description": "Quantification of AI system uncertainty, confidence intervals, and known limitations must be documented."},
            {"id": "NIST-MEA-005", "title": "Privacy risk evaluation documented", "ref": "MEASURE 2.10", "severity": "high", "description": "Privacy risks associated with the AI system — including training data, inferences, and outputs — must be evaluated and documented."},
            {"id": "NIST-MEA-006", "title": "Performance against benchmarks documented", "ref": "MEASURE 2.1", "severity": "high", "description": "AI system performance must be measured against relevant benchmarks and evaluation datasets, with results documented."},
            {"id": "NIST-MEA-007", "title": "Ongoing performance monitoring plan documented", "ref": "MEASURE 4.1", "severity": "high", "description": "A plan for ongoing monitoring of AI system performance in deployment — including drift detection and alert thresholds — must be documented."},
            # MANAGE
            {"id": "NIST-MAN-001", "title": "Risk response plan documented", "ref": "MANAGE 1.1", "severity": "high", "description": "A risk response plan covering risk prioritisation, treatment options, and decision criteria must be documented."},
            {"id": "NIST-MAN-002", "title": "Incident tracking and reporting mechanism exists", "ref": "MANAGE 2.2", "severity": "high", "description": "A mechanism for tracking, reporting, and responding to AI-related incidents must be implemented and documented."},
            {"id": "NIST-MAN-003", "title": "Model decommissioning and sunset criteria defined", "ref": "MANAGE 4.1", "severity": "medium", "description": "Criteria for decommissioning, retiring, or replacing the AI system must be defined and documented."},
            {"id": "NIST-MAN-004", "title": "Continuous monitoring implemented and documented", "ref": "MANAGE 2.4", "severity": "high", "description": "Continuous monitoring of the AI system in operation — covering performance, safety, and risk — must be implemented and documented."},
            {"id": "NIST-MAN-005", "title": "Residual risk accepted and documented", "ref": "MANAGE 1.3", "severity": "medium", "description": "Residual risks after mitigation must be explicitly accepted, signed off, and documented by an appropriate authority."},
            {"id": "NIST-MAN-006", "title": "Human fallback and escalation procedure documented", "ref": "MANAGE 2.1", "severity": "critical", "description": "A human fallback procedure — including escalation paths and override capabilities — must be documented for situations where the AI system fails or produces uncertain outputs."},
        ]

    def run_check(self, check_id: str) -> CheckResult | None:
        dispatch = {
            "NIST-GOV-001": self._check_governance_policy,
            "NIST-GOV-002": self._check_risk_appetite,
            "NIST-GOV-003": self._check_roles_accountability,
            "NIST-GOV-004": self._check_workforce_training,
            "NIST-GOV-005": self._check_oversight_structure,
            "NIST-GOV-006": self._check_legal_compliance_policy,
            "NIST-MAP-001": self._check_intended_use,
            "NIST-MAP-002": self._check_stakeholder_impact,
            "NIST-MAP-003": self._check_risk_categories,
            "NIST-MAP-004": self._check_data_provenance,
            "NIST-MAP-005": self._check_third_party_risks,
            "NIST-MAP-006": self._check_negative_impacts,
            "NIST-MEA-001": self._check_trustworthiness_metrics,
            "NIST-MEA-002": self._check_bias_fairness,
            "NIST-MEA-003": self._check_explainability,
            "NIST-MEA-004": self._check_uncertainty,
            "NIST-MEA-005": self._check_privacy_risk,
            "NIST-MEA-006": self._check_benchmarks,
            "NIST-MEA-007": self._check_monitoring_plan,
            "NIST-MAN-001": self._check_risk_response_plan,
            "NIST-MAN-002": self._check_incident_tracking,
            "NIST-MAN-003": self._check_decommissioning_criteria,
            "NIST-MAN-004": self._check_continuous_monitoring,
            "NIST-MAN-005": self._check_residual_risk,
            "NIST-MAN-006": self._check_human_fallback,
        }
        fn = dispatch.get(check_id)
        return fn() if fn else None

    # ── GOVERN checks ─────────────────────────────────────────────────────────

    def _check_governance_policy(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/ai_governance.md", "ai_governance.md",
            "docs/ai_policy.md", "ai_policy.md",
            "docs/governance.md", "governance.md",
        )
        if exists:
            return self._pass("NIST-GOV-001", "AI governance policy documented",
                              "AI governance policy document found.", "GOVERN 1.1", Severity.CRITICAL, _FW, evidence=[path])
        files = self._scan_for_keywords(["ai governance", "ai policy", "governance policy", "responsible ai policy"])
        if files:
            return self._warn("NIST-GOV-001", "AI governance policy documented",
                              "Governance content found but no dedicated policy document.",
                              "GOVERN 1.1", Severity.CRITICAL, _FW, evidence=files[:3],
                              remediation="Create a dedicated AI governance policy document (e.g., docs/ai_governance.md).")
        return self._fail("NIST-GOV-001", "AI governance policy documented",
                          "No AI governance policy found.",
                          "GOVERN 1.1", Severity.CRITICAL, _FW,
                          remediation="Create docs/ai_governance.md covering: policy scope, principles, risk appetite, accountability structure, and regulatory commitments.")

    def _check_risk_appetite(self) -> CheckResult:
        files = self._scan_for_keywords(["risk appetite", "risk tolerance", "acceptable risk", "risk threshold"])
        if files:
            return self._pass("NIST-GOV-002", "AI risk appetite and tolerance defined",
                              "Risk appetite/tolerance documentation found.", "GOVERN 1.2", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-GOV-002", "AI risk appetite and tolerance defined",
                          "No risk appetite or tolerance thresholds defined.",
                          "GOVERN 1.2", Severity.HIGH, _FW,
                          remediation="Define and document organisational risk appetite and tolerance thresholds for AI systems in your governance policy.")

    def _check_roles_accountability(self) -> CheckResult:
        files = self._scan_for_keywords(["responsible", "accountable", "raci", "role", "ai owner", "model owner", "ai risk owner"])
        exists, path = self._file_exists("docs/raci.md", "raci.md", "docs/roles.md", "roles.md")
        if exists:
            return self._pass("NIST-GOV-003", "Roles and accountability assigned",
                              "Roles and accountability document found.", "GOVERN 1.4", Severity.HIGH, _FW, evidence=[path])
        if files:
            return self._warn("NIST-GOV-003", "Roles and accountability assigned",
                              "Role/accountability content found but no dedicated document.",
                              "GOVERN 1.4", Severity.HIGH, _FW, evidence=files[:3],
                              remediation="Create a dedicated roles and accountability document (RACI matrix or equivalent).")
        return self._fail("NIST-GOV-003", "Roles and accountability assigned",
                          "No role or accountability documentation found.",
                          "GOVERN 1.4", Severity.HIGH, _FW,
                          remediation="Document AI risk management roles: who owns the model, who owns risk decisions, who escalates incidents.")

    def _check_workforce_training(self) -> CheckResult:
        files = self._scan_for_keywords(["training", "awareness", "education", "ai literacy", "risk training", "workforce"])
        if files:
            return self._pass("NIST-GOV-004", "Workforce AI risk training documented",
                              "Training/awareness documentation found.", "GOVERN 4.1", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("NIST-GOV-004", "Workforce AI risk training documented",
                          "No workforce AI risk training documentation found.",
                          "GOVERN 4.1", Severity.MEDIUM, _FW,
                          remediation="Document AI risk training programme for relevant staff, including completion tracking.")

    def _check_oversight_structure(self) -> CheckResult:
        files = self._scan_for_keywords(["oversight", "ai committee", "ai board", "review board", "escalation", "governance committee"])
        if files:
            return self._pass("NIST-GOV-005", "Organisational AI oversight structure exists",
                              "Oversight structure documentation found.", "GOVERN 2.2", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-GOV-005", "Organisational AI oversight structure exists",
                          "No AI oversight structure or escalation path documented.",
                          "GOVERN 2.2", Severity.HIGH, _FW,
                          remediation="Document the organisational AI oversight structure: committee or review board, escalation paths, and decision authority.")

    def _check_legal_compliance_policy(self) -> CheckResult:
        files = self._scan_for_keywords(["regulatory", "compliance", "legal requirement", "eu ai act", "nist", "regulation", "gdpr"])
        if files:
            return self._pass("NIST-GOV-006", "Policies address legal, regulatory, and compliance requirements",
                              "Legal/regulatory compliance references found.", "GOVERN 1.7", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-GOV-006", "Policies address legal, regulatory, and compliance requirements",
                          "No regulatory or legal compliance coverage found in AI policies.",
                          "GOVERN 1.7", Severity.HIGH, _FW,
                          remediation="Update AI governance documentation to explicitly reference applicable regulations (EU AI Act, GDPR, sector-specific laws).")

    # ── MAP checks ────────────────────────────────────────────────────────────

    def _check_intended_use(self) -> CheckResult:
        files = self._scan_for_keywords(["intended use", "intended purpose", "use case", "deployment context", "operational context", "use scenario"])
        if files:
            return self._pass("NIST-MAP-001", "Intended use and deployment context documented",
                              "Intended use documentation found.", "MAP 1.1", Severity.CRITICAL, _FW, evidence=files[:3])
        return self._fail("NIST-MAP-001", "Intended use and deployment context documented",
                          "No intended use or deployment context documentation found.",
                          "MAP 1.1", Severity.CRITICAL, _FW,
                          remediation="Document: intended purpose, target users, deployment environment, and out-of-scope uses.")

    def _check_stakeholder_impact(self) -> CheckResult:
        files = self._scan_for_keywords(["stakeholder", "affected", "impacted", "community", "impact assessment", "end user impact"])
        if files:
            return self._pass("NIST-MAP-002", "Stakeholder impact assessment performed",
                              "Stakeholder impact documentation found.", "MAP 1.5", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MAP-002", "Stakeholder impact assessment performed",
                          "No stakeholder impact assessment found.",
                          "MAP 1.5", Severity.HIGH, _FW,
                          remediation="Conduct and document a stakeholder impact assessment identifying affected individuals, groups, and potential harms.")

    def _check_risk_categories(self) -> CheckResult:
        files = self._scan_for_keywords(["risk category", "risk type", "bias risk", "security risk", "explainability risk", "privacy risk", "risk catalogue", "risk register"])
        if files:
            return self._pass("NIST-MAP-003", "AI risk categories identified and catalogued",
                              "Risk category documentation found.", "MAP 2.2", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MAP-003", "AI risk categories identified and catalogued",
                          "No AI risk category catalogue found.",
                          "MAP 2.2", Severity.HIGH, _FW,
                          remediation="Create a risk register cataloguing relevant risk types: bias, security, explainability, privacy, reliability, and operational risks.")

    def _check_data_provenance(self) -> CheckResult:
        files = self._scan_for_keywords(["provenance", "lineage", "data origin", "data source", "data quality", "data pipeline"])
        if files:
            return self._pass("NIST-MAP-004", "Data provenance and lineage documented",
                              "Data provenance documentation found.", "MAP 3.5", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MAP-004", "Data provenance and lineage documented",
                          "No data provenance or lineage documentation found.",
                          "MAP 3.5", Severity.HIGH, _FW,
                          remediation="Document data origins, collection methods, transformations, and quality characteristics for all datasets used.")

    def _check_third_party_risks(self) -> CheckResult:
        files = self._scan_for_keywords(["third party", "third-party", "supply chain", "vendor", "api dependency", "external model", "open source model"])
        if files:
            return self._pass("NIST-MAP-005", "Third-party and supply chain AI risks assessed",
                              "Third-party risk documentation found.", "MAP 5.1", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("NIST-MAP-005", "Third-party and supply chain AI risks assessed",
                          "No third-party or supply chain risk assessment found.",
                          "MAP 5.1", Severity.MEDIUM, _FW,
                          remediation="Assess and document risks from third-party AI components, APIs, pre-trained models, and open-source dependencies.")

    def _check_negative_impacts(self) -> CheckResult:
        files = self._scan_for_keywords(["negative impact", "potential harm", "unintended consequence", "adverse impact", "societal impact", "foreseeable harm"])
        if files:
            return self._pass("NIST-MAP-006", "Foreseeable negative impacts documented",
                              "Negative impact documentation found.", "MAP 2.3", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MAP-006", "Foreseeable negative impacts documented",
                          "No foreseeable negative impact documentation found.",
                          "MAP 2.3", Severity.HIGH, _FW,
                          remediation="Document foreseeable negative impacts on individuals, groups, and society including discriminatory outcomes and misuse scenarios.")

    # ── MEASURE checks ────────────────────────────────────────────────────────

    def _check_trustworthiness_metrics(self) -> CheckResult:
        files = self._scan_for_keywords(["trustworthiness", "reliability metric", "safety metric", "accuracy metric", "robustness metric", "evaluation metric"])
        if files:
            return self._pass("NIST-MEA-001", "Trustworthiness metrics defined and documented",
                              "Trustworthiness metrics found.", "MEASURE 1.1", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MEA-001", "Trustworthiness metrics defined and documented",
                          "No trustworthiness evaluation metrics defined.",
                          "MEASURE 1.1", Severity.HIGH, _FW,
                          remediation="Define metrics covering NIST AI RMF trustworthiness characteristics: accuracy, reliability, explainability, privacy, security, and fairness.")

    def _check_bias_fairness(self) -> CheckResult:
        files = self._scan_for_keywords(["fairness", "bias evaluation", "demographic", "subgroup", "disparate impact", "equal opportunity", "fairness metric", "bias audit"])
        if files:
            return self._pass("NIST-MEA-002", "Bias and fairness evaluation performed",
                              "Bias/fairness evaluation found.", "MEASURE 2.5", Severity.CRITICAL, _FW, evidence=files[:3])
        return self._fail("NIST-MEA-002", "Bias and fairness evaluation performed",
                          "No bias or fairness evaluation documentation found.",
                          "MEASURE 2.5", Severity.CRITICAL, _FW,
                          remediation="Conduct systematic fairness evaluation across relevant demographic groups. Document methodology, metrics, and results.")

    def _check_explainability(self) -> CheckResult:
        files = self._scan_for_keywords(["explainability", "interpretability", "shap", "lime", "feature importance", "model explanation", "xai"])
        if files:
            return self._pass("NIST-MEA-003", "Explainability and interpretability assessed",
                              "Explainability assessment found.", "MEASURE 2.6", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MEA-003", "Explainability and interpretability assessed",
                          "No explainability or interpretability assessment found.",
                          "MEASURE 2.6", Severity.HIGH, _FW,
                          remediation="Assess and document AI system explainability for the deployment context. Consider SHAP, LIME, or model cards.")

    def _check_uncertainty(self) -> CheckResult:
        files = self._scan_for_keywords(["uncertainty", "confidence interval", "confidence score", "prediction interval", "epistemic", "aleatoric"])
        if files:
            return self._pass("NIST-MEA-004", "Uncertainty and confidence quantified",
                              "Uncertainty quantification documentation found.", "MEASURE 2.3", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("NIST-MEA-004", "Uncertainty and confidence quantified",
                          "No uncertainty quantification documentation found.",
                          "MEASURE 2.3", Severity.MEDIUM, _FW,
                          remediation="Document how the system quantifies and communicates uncertainty or confidence in its outputs.")

    def _check_privacy_risk(self) -> CheckResult:
        files = self._scan_for_keywords(["privacy", "personal data", "pii", "gdpr", "data protection", "privacy risk", "privacy impact"])
        if files:
            return self._pass("NIST-MEA-005", "Privacy risk evaluation documented",
                              "Privacy risk evaluation found.", "MEASURE 2.10", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MEA-005", "Privacy risk evaluation documented",
                          "No privacy risk evaluation found.",
                          "MEASURE 2.10", Severity.HIGH, _FW,
                          remediation="Conduct and document a privacy risk evaluation covering training data, inferences, and output disclosures. Consider a DPIA if GDPR applies.")

    def _check_benchmarks(self) -> CheckResult:
        files = self._scan_for_keywords(["benchmark", "baseline", "evaluation dataset", "test set performance", "performance comparison"])
        if files:
            return self._pass("NIST-MEA-006", "Performance against benchmarks documented",
                              "Benchmark results found.", "MEASURE 2.1", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MEA-006", "Performance against benchmarks documented",
                          "No benchmark performance documentation found.",
                          "MEASURE 2.1", Severity.HIGH, _FW,
                          remediation="Document AI system performance against established benchmarks or evaluation datasets relevant to the task.")

    def _check_monitoring_plan(self) -> CheckResult:
        files = self._scan_for_keywords(["monitoring", "drift detection", "performance monitoring", "alert threshold", "model monitoring", "production monitoring"])
        if files:
            return self._pass("NIST-MEA-007", "Ongoing performance monitoring plan documented",
                              "Monitoring plan documentation found.", "MEASURE 4.1", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MEA-007", "Ongoing performance monitoring plan documented",
                          "No ongoing performance monitoring plan found.",
                          "MEASURE 4.1", Severity.HIGH, _FW,
                          remediation="Create a monitoring plan covering: metrics to track, alert thresholds, drift detection approach, and review cadence.")

    # ── MANAGE checks ─────────────────────────────────────────────────────────

    def _check_risk_response_plan(self) -> CheckResult:
        files = self._scan_for_keywords(["risk response", "risk treatment", "mitigation plan", "risk remediation", "risk prioritisation"])
        if files:
            return self._pass("NIST-MAN-001", "Risk response plan documented",
                              "Risk response plan found.", "MANAGE 1.1", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MAN-001", "Risk response plan documented",
                          "No risk response plan found.",
                          "MANAGE 1.1", Severity.HIGH, _FW,
                          remediation="Document risk response strategies: for each identified risk, specify treatment (accept/mitigate/transfer/avoid) and owner.")

    def _check_incident_tracking(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/incident_response.md", "incident_response.md",
            "docs/incident_management.md", "incident_management.md",
        )
        if exists:
            return self._pass("NIST-MAN-002", "Incident tracking and reporting mechanism exists",
                              "Incident management document found.", "MANAGE 2.2", Severity.HIGH, _FW, evidence=[path])
        files = self._scan_for_keywords(["incident", "incident report", "incident tracking", "issue reporting", "event report"])
        if files:
            return self._warn("NIST-MAN-002", "Incident tracking and reporting mechanism exists",
                              "Incident tracking references found but no dedicated procedure.",
                              "MANAGE 2.2", Severity.HIGH, _FW, evidence=files[:3],
                              remediation="Create a dedicated incident management procedure document.")
        return self._fail("NIST-MAN-002", "Incident tracking and reporting mechanism exists",
                          "No incident tracking or reporting mechanism documented.",
                          "MANAGE 2.2", Severity.HIGH, _FW,
                          remediation="Create docs/incident_response.md covering: incident definition, reporting process, escalation path, and resolution tracking.")

    def _check_decommissioning_criteria(self) -> CheckResult:
        files = self._scan_for_keywords(["decommission", "sunset", "retirement", "end of life", "deprecation", "model retirement"])
        if files:
            return self._pass("NIST-MAN-003", "Model decommissioning and sunset criteria defined",
                              "Decommissioning criteria found.", "MANAGE 4.1", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("NIST-MAN-003", "Model decommissioning and sunset criteria defined",
                          "No model decommissioning criteria documented.",
                          "MANAGE 4.1", Severity.MEDIUM, _FW,
                          remediation="Define criteria for when the AI system should be retired, replaced, or significantly updated.")

    def _check_continuous_monitoring(self) -> CheckResult:
        files = self._scan_for_keywords(["continuous monitoring", "ongoing monitoring", "real-time monitoring", "operational monitoring", "production monitoring"])
        if files:
            return self._pass("NIST-MAN-004", "Continuous monitoring implemented and documented",
                              "Continuous monitoring documentation found.", "MANAGE 2.4", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("NIST-MAN-004", "Continuous monitoring implemented and documented",
                          "No continuous monitoring implementation documented.",
                          "MANAGE 2.4", Severity.HIGH, _FW,
                          remediation="Document how the AI system is continuously monitored in production for performance degradation, safety issues, and fairness drift.")

    def _check_residual_risk(self) -> CheckResult:
        files = self._scan_for_keywords(["residual risk", "accepted risk", "risk acceptance", "risk sign-off", "tolerated risk"])
        if files:
            return self._pass("NIST-MAN-005", "Residual risk accepted and documented",
                              "Residual risk acceptance documentation found.", "MANAGE 1.3", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("NIST-MAN-005", "Residual risk accepted and documented",
                          "No residual risk acceptance documentation found.",
                          "MANAGE 1.3", Severity.MEDIUM, _FW,
                          remediation="Document residual risks remaining after mitigation and record formal acceptance by an appropriate authority.")

    def _check_human_fallback(self) -> CheckResult:
        files = self._scan_for_keywords(["human fallback", "fallback procedure", "escalation procedure", "human override", "manual override", "human-in-the-loop fallback"])
        if files:
            return self._pass("NIST-MAN-006", "Human fallback and escalation procedure documented",
                              "Human fallback procedure found.", "MANAGE 2.1", Severity.CRITICAL, _FW, evidence=files[:3])
        return self._fail("NIST-MAN-006", "Human fallback and escalation procedure documented",
                          "No human fallback or escalation procedure documented.",
                          "MANAGE 2.1", Severity.CRITICAL, _FW,
                          remediation="Document human fallback procedures: when to escalate, who to escalate to, how to override the AI system, and recovery steps.")
