"""ISO/IEC 42001:2023 AI Management System (AIMS) compliance checks.

Published December 2023. First certifiable AI management system standard.
Covers organisational context, leadership, planning, support, operations,
performance evaluation, and continual improvement.
"""
from __future__ import annotations

from typing import Any

from ..models import CheckResult, Framework, Severity
from .base import BaseFramework

_FW = Framework.ISO_42001


class ISO42001Framework(BaseFramework):
    """ISO/IEC 42001:2023 AI Management System compliance checks."""

    def check_metadata(self) -> list[dict[str, Any]]:
        return [
            # Clause 4 — Context
            {"id": "ISO-C4-001", "title": "Organisational context documented", "ref": "Clause 4.1", "severity": "high", "description": "The organisation's internal and external context relevant to its AI management system must be determined and documented."},
            {"id": "ISO-C4-002", "title": "Interested party needs and expectations identified", "ref": "Clause 4.2", "severity": "high", "description": "Relevant interested parties and their needs, expectations, and applicable requirements must be identified and documented."},
            {"id": "ISO-C4-003", "title": "AIMS scope defined and documented", "ref": "Clause 4.3", "severity": "critical", "description": "The scope and boundaries of the AI management system must be clearly defined and documented."},
            {"id": "ISO-C4-004", "title": "AI impact assessment criteria established", "ref": "Clause 4.4 / Annex B", "severity": "high", "description": "Criteria for assessing AI system impacts — including on individuals and society — must be established per Annex B guidance."},
            # Clause 5 — Leadership
            {"id": "ISO-C5-001", "title": "AI policy established and communicated", "ref": "Clause 5.2", "severity": "critical", "description": "Top management must establish an AI policy that is documented, communicated, and available to relevant parties."},
            {"id": "ISO-C5-002", "title": "AI roles and responsibilities assigned", "ref": "Clause 5.3", "severity": "high", "description": "Organisational roles, responsibilities, and authorities for AI management system activities must be assigned and documented."},
            {"id": "ISO-C5-003", "title": "Top management commitment demonstrated", "ref": "Clause 5.1", "severity": "medium", "description": "Evidence of top management commitment to the AI management system must exist (e.g., policy sign-off, resource allocation)."},
            # Clause 6 — Planning
            {"id": "ISO-C6-001", "title": "AI risks and opportunities assessed", "ref": "Clause 6.1", "severity": "critical", "description": "Risks and opportunities relevant to the AIMS must be determined and actions to address them planned and documented."},
            {"id": "ISO-C6-002", "title": "AI objectives defined and measurable", "ref": "Clause 6.2", "severity": "high", "description": "AI management objectives must be established, measurable where practicable, monitored, and documented."},
            {"id": "ISO-C6-003", "title": "Change planning documented", "ref": "Clause 6.3", "severity": "medium", "description": "When changes to the AIMS are planned, they must be carried out in a controlled manner with documentation."},
            # Clause 7 — Support
            {"id": "ISO-C7-001", "title": "Competence and training records maintained", "ref": "Clause 7.2", "severity": "high", "description": "The organisation must determine required competence for AI roles and maintain records of training, education, and experience."},
            {"id": "ISO-C7-002", "title": "AI awareness programme documented", "ref": "Clause 7.3", "severity": "medium", "description": "Persons performing work affecting AI system performance must be aware of the AI policy and their contribution to AIMS effectiveness."},
            {"id": "ISO-C7-003", "title": "AI documentation control procedures exist", "ref": "Clause 7.5", "severity": "high", "description": "Documented information required by the AIMS must be controlled: creation, update, version control, availability, and protection."},
            {"id": "ISO-C7-004", "title": "Internal and external communication plan exists", "ref": "Clause 7.4", "severity": "medium", "description": "The organisation must determine what, when, with whom, and how to communicate regarding the AIMS."},
            # Clause 8 — Operation
            {"id": "ISO-C8-001", "title": "Operational planning and controls documented", "ref": "Clause 8.1", "severity": "high", "description": "Processes needed to meet AIMS requirements must be planned, implemented, controlled, and documented."},
            {"id": "ISO-C8-002", "title": "AI system impact assessment performed", "ref": "Clause 8.4 / Annex B", "severity": "critical", "description": "An AI system impact assessment covering potential impacts on individuals, groups, and society must be performed per Annex B."},
            {"id": "ISO-C8-003", "title": "Supply chain and third-party AI controls documented", "ref": "Clause 8.3", "severity": "high", "description": "Controls for externally provided AI systems, components, and services must be established and documented."},
            {"id": "ISO-C8-004", "title": "AI incident management process documented", "ref": "Clause 8.5", "severity": "high", "description": "A process for managing AI incidents — including detection, response, recovery, and learning — must be documented."},
            # Clause 9 — Performance Evaluation
            {"id": "ISO-C9-001", "title": "Monitoring and measurement plan exists", "ref": "Clause 9.1", "severity": "high", "description": "What to monitor and measure, methods, timing, and who evaluates results must be determined and documented for the AIMS."},
            {"id": "ISO-C9-002", "title": "Internal audit programme documented", "ref": "Clause 9.2", "severity": "high", "description": "An internal audit programme for the AIMS must be established, implemented, and records maintained."},
            {"id": "ISO-C9-003", "title": "Management review records maintained", "ref": "Clause 9.3", "severity": "medium", "description": "Top management must review the AIMS at planned intervals; review outputs and records must be retained."},
            # Clause 10 — Improvement
            {"id": "ISO-C10-001", "title": "Nonconformity and corrective action process exists", "ref": "Clause 10.2", "severity": "high", "description": "A process for managing nonconformities and implementing corrective actions must exist with records retained."},
            {"id": "ISO-C10-002", "title": "Continual improvement objectives documented", "ref": "Clause 10.3", "severity": "medium", "description": "The organisation must continually improve the suitability, adequacy, and effectiveness of the AIMS."},
            {"id": "ISO-C10-003", "title": "Lessons learned process documented", "ref": "Clause 10.1", "severity": "medium", "description": "A process for capturing and applying lessons learned from AI incidents, near-misses, and evaluations must be documented."},
        ]

    def run_check(self, check_id: str) -> CheckResult | None:
        dispatch = {
            "ISO-C4-001": self._check_org_context,
            "ISO-C4-002": self._check_interested_parties,
            "ISO-C4-003": self._check_aims_scope,
            "ISO-C4-004": self._check_impact_criteria,
            "ISO-C5-001": self._check_ai_policy,
            "ISO-C5-002": self._check_roles_responsibilities,
            "ISO-C5-003": self._check_top_management,
            "ISO-C6-001": self._check_risks_opportunities,
            "ISO-C6-002": self._check_ai_objectives,
            "ISO-C6-003": self._check_change_planning,
            "ISO-C7-001": self._check_competence_training,
            "ISO-C7-002": self._check_awareness_programme,
            "ISO-C7-003": self._check_documentation_control,
            "ISO-C7-004": self._check_communication_plan,
            "ISO-C8-001": self._check_operational_planning,
            "ISO-C8-002": self._check_impact_assessment,
            "ISO-C8-003": self._check_supply_chain_controls,
            "ISO-C8-004": self._check_incident_management,
            "ISO-C9-001": self._check_monitoring_plan,
            "ISO-C9-002": self._check_internal_audit,
            "ISO-C9-003": self._check_management_review,
            "ISO-C10-001": self._check_corrective_actions,
            "ISO-C10-002": self._check_continual_improvement,
            "ISO-C10-003": self._check_lessons_learned,
        }
        fn = dispatch.get(check_id)
        return fn() if fn else None

    # ── Clause 4 checks ───────────────────────────────────────────────────────

    def _check_org_context(self) -> CheckResult:
        files = self._scan_for_keywords(["organisational context", "organizational context", "internal context", "external context", "business context", "operating environment"])
        if files:
            return self._pass("ISO-C4-001", "Organisational context documented",
                              "Organisational context documentation found.", "Clause 4.1", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C4-001", "Organisational context documented",
                          "No organisational context documentation found.",
                          "Clause 4.1", Severity.HIGH, _FW,
                          remediation="Document the internal and external context relevant to your AI management system (e.g., in a context statement or governance charter).")

    def _check_interested_parties(self) -> CheckResult:
        files = self._scan_for_keywords(["interested party", "stakeholder", "interested parties", "affected party", "customer requirement", "regulatory requirement"])
        if files:
            return self._pass("ISO-C4-002", "Interested party needs and expectations identified",
                              "Interested party documentation found.", "Clause 4.2", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C4-002", "Interested party needs and expectations identified",
                          "No interested party needs/expectations documentation found.",
                          "Clause 4.2", Severity.HIGH, _FW,
                          remediation="Identify and document relevant interested parties (customers, regulators, employees, affected communities) and their applicable requirements.")

    def _check_aims_scope(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/aims_scope.md", "aims_scope.md",
            "docs/scope.md", "scope.md",
            "docs/ai_management_scope.md",
        )
        if exists:
            return self._pass("ISO-C4-003", "AIMS scope defined and documented",
                              "AIMS scope document found.", "Clause 4.3", Severity.CRITICAL, _FW, evidence=[path])
        files = self._scan_for_keywords(["aims scope", "ai management system scope", "management system scope", "scope statement", "system boundary"])
        if files:
            return self._warn("ISO-C4-003", "AIMS scope defined and documented",
                              "Scope content found but no dedicated AIMS scope document.",
                              "Clause 4.3", Severity.CRITICAL, _FW, evidence=files[:3],
                              remediation="Create a dedicated AIMS scope document covering boundaries, inclusions, exclusions, and interfaces.")
        return self._fail("ISO-C4-003", "AIMS scope defined and documented",
                          "No AIMS scope definition found.",
                          "Clause 4.3", Severity.CRITICAL, _FW,
                          remediation="Define the AIMS scope: which AI systems are covered, organisational boundaries, and any exclusions with justification.")

    def _check_impact_criteria(self) -> CheckResult:
        files = self._scan_for_keywords(["impact criteria", "impact assessment criteria", "annex b", "ai impact", "impact threshold", "risk criteria"])
        if files:
            return self._pass("ISO-C4-004", "AI impact assessment criteria established",
                              "Impact assessment criteria found.", "Clause 4.4 / Annex B", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C4-004", "AI impact assessment criteria established",
                          "No AI impact assessment criteria found.",
                          "Clause 4.4 / Annex B", Severity.HIGH, _FW,
                          remediation="Establish AI impact assessment criteria per ISO/IEC 42001 Annex B, covering severity scales and assessment methodology.")

    # ── Clause 5 checks ───────────────────────────────────────────────────────

    def _check_ai_policy(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/ai_policy.md", "ai_policy.md",
            "docs/responsible_ai_policy.md", "responsible_ai_policy.md",
            "docs/ai_ethics_policy.md", "ai_ethics_policy.md",
        )
        if exists:
            return self._pass("ISO-C5-001", "AI policy established and communicated",
                              "AI policy document found.", "Clause 5.2", Severity.CRITICAL, _FW, evidence=[path])
        files = self._scan_for_keywords(["ai policy", "responsible ai", "ai principles", "ai ethics policy", "aims policy"])
        if files:
            return self._warn("ISO-C5-001", "AI policy established and communicated",
                              "AI policy content found but no dedicated policy document.",
                              "Clause 5.2", Severity.CRITICAL, _FW, evidence=files[:3],
                              remediation="Create a dedicated AI policy document that is approved by top management and communicated throughout the organisation.")
        return self._fail("ISO-C5-001", "AI policy established and communicated",
                          "No AI policy found.",
                          "Clause 5.2", Severity.CRITICAL, _FW,
                          remediation="Create an AI policy document covering: commitment to responsible AI, key principles, and how it applies to the organisation's AI activities.")

    def _check_roles_responsibilities(self) -> CheckResult:
        files = self._scan_for_keywords(["role", "responsibility", "accountability", "raci", "ai officer", "ai team", "ai governance role"])
        if files:
            return self._pass("ISO-C5-002", "AI roles and responsibilities assigned",
                              "Roles and responsibilities documentation found.", "Clause 5.3", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C5-002", "AI roles and responsibilities assigned",
                          "No AI roles and responsibilities documentation found.",
                          "Clause 5.3", Severity.HIGH, _FW,
                          remediation="Document AI management system roles and responsibilities. Include who is responsible for AI policy, risk management, and AIMS review.")

    def _check_top_management(self) -> CheckResult:
        files = self._scan_for_keywords(["management commitment", "executive", "leadership commitment", "board approval", "sign-off", "approved by", "ceo", "cto", "chief"])
        if files:
            return self._pass("ISO-C5-003", "Top management commitment demonstrated",
                              "Management commitment evidence found.", "Clause 5.1", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("ISO-C5-003", "Top management commitment demonstrated",
                          "No evidence of top management commitment to AIMS found.",
                          "Clause 5.1", Severity.MEDIUM, _FW,
                          remediation="Ensure AI policy is signed by top management and that resource allocation decisions are documented.")

    # ── Clause 6 checks ───────────────────────────────────────────────────────

    def _check_risks_opportunities(self) -> CheckResult:
        files = self._scan_for_keywords(["risk and opportunity", "risks and opportunities", "risk assessment", "opportunity assessment", "aims risk"])
        if files:
            return self._pass("ISO-C6-001", "AI risks and opportunities assessed",
                              "Risk and opportunity assessment found.", "Clause 6.1", Severity.CRITICAL, _FW, evidence=files[:3])
        return self._fail("ISO-C6-001", "AI risks and opportunities assessed",
                          "No AIMS risk and opportunity assessment found.",
                          "Clause 6.1", Severity.CRITICAL, _FW,
                          remediation="Conduct and document a risk and opportunity assessment for the AIMS, identifying threats and opportunities and planned actions to address them.")

    def _check_ai_objectives(self) -> CheckResult:
        files = self._scan_for_keywords(["ai objective", "aims objective", "ai goal", "measurable objective", "key result", "okr"])
        if files:
            return self._pass("ISO-C6-002", "AI objectives defined and measurable",
                              "AI objectives documentation found.", "Clause 6.2", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C6-002", "AI objectives defined and measurable",
                          "No AI management objectives defined.",
                          "Clause 6.2", Severity.HIGH, _FW,
                          remediation="Define measurable AI objectives aligned with the AI policy. Document what, who, how, and when for each objective.")

    def _check_change_planning(self) -> CheckResult:
        files = self._scan_for_keywords(["change management", "change planning", "change control", "change procedure", "change log", "change record"])
        if files:
            return self._pass("ISO-C6-003", "Change planning documented",
                              "Change planning documentation found.", "Clause 6.3", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("ISO-C6-003", "Change planning documented",
                          "No change planning documentation found.",
                          "Clause 6.3", Severity.MEDIUM, _FW,
                          remediation="Document how changes to the AIMS are planned, assessed for impact, approved, and communicated.")

    # ── Clause 7 checks ───────────────────────────────────────────────────────

    def _check_competence_training(self) -> CheckResult:
        files = self._scan_for_keywords(["competence", "training record", "qualification", "certification", "skill", "learning and development"])
        if files:
            return self._pass("ISO-C7-001", "Competence and training records maintained",
                              "Competence/training records found.", "Clause 7.2", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C7-001", "Competence and training records maintained",
                          "No competence or training records found.",
                          "Clause 7.2", Severity.HIGH, _FW,
                          remediation="Define required competences for AI roles and maintain records of training, certifications, and experience for relevant personnel.")

    def _check_awareness_programme(self) -> CheckResult:
        files = self._scan_for_keywords(["awareness", "ai awareness", "onboarding", "staff communication", "internal communication"])
        if files:
            return self._pass("ISO-C7-002", "AI awareness programme documented",
                              "Awareness programme documentation found.", "Clause 7.3", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("ISO-C7-002", "AI awareness programme documented",
                          "No AI awareness programme documentation found.",
                          "Clause 7.3", Severity.MEDIUM, _FW,
                          remediation="Document an AI awareness programme ensuring relevant personnel understand the AI policy and their role in AIMS effectiveness.")

    def _check_documentation_control(self) -> CheckResult:
        files = self._scan_for_keywords(["document control", "version control", "documentation procedure", "document management", "document approval", "record keeping"])
        if files:
            return self._pass("ISO-C7-003", "AI documentation control procedures exist",
                              "Documentation control procedures found.", "Clause 7.5", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C7-003", "AI documentation control procedures exist",
                          "No documentation control procedures found.",
                          "Clause 7.5", Severity.HIGH, _FW,
                          remediation="Establish documentation control procedures: version control, approval process, distribution, access controls, and retention policy.")

    def _check_communication_plan(self) -> CheckResult:
        files = self._scan_for_keywords(["communication plan", "communication procedure", "stakeholder communication", "reporting", "disclosure plan"])
        if files:
            return self._pass("ISO-C7-004", "Internal and external communication plan exists",
                              "Communication plan documentation found.", "Clause 7.4", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("ISO-C7-004", "Internal and external communication plan exists",
                          "No AIMS communication plan found.",
                          "Clause 7.4", Severity.MEDIUM, _FW,
                          remediation="Document what AIMS-related information is communicated, to whom, when, and through what channels (internal and external).")

    # ── Clause 8 checks ───────────────────────────────────────────────────────

    def _check_operational_planning(self) -> CheckResult:
        files = self._scan_for_keywords(["operational plan", "operational control", "operational procedure", "deployment procedure", "release procedure", "deployment checklist"])
        if files:
            return self._pass("ISO-C8-001", "Operational planning and controls documented",
                              "Operational planning documentation found.", "Clause 8.1", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C8-001", "Operational planning and controls documented",
                          "No operational planning or controls documentation found.",
                          "Clause 8.1", Severity.HIGH, _FW,
                          remediation="Document operational processes and controls for AI system deployment: procedures, checkpoints, approval gates, and review criteria.")

    def _check_impact_assessment(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/ai_impact_assessment.md", "ai_impact_assessment.md",
            "docs/impact_assessment.md", "impact_assessment.md",
            "docs/aia.md",
        )
        if exists:
            return self._pass("ISO-C8-002", "AI system impact assessment performed",
                              "AI impact assessment document found.", "Clause 8.4 / Annex B", Severity.CRITICAL, _FW, evidence=[path])
        files = self._scan_for_keywords(["impact assessment", "ai impact", "societal impact", "individual impact", "annex b"])
        if files:
            return self._warn("ISO-C8-002", "AI system impact assessment performed",
                              "Impact assessment content found but no dedicated document.",
                              "Clause 8.4 / Annex B", Severity.CRITICAL, _FW, evidence=files[:3],
                              remediation="Create a dedicated AI system impact assessment document per ISO/IEC 42001 Annex B.")
        return self._fail("ISO-C8-002", "AI system impact assessment performed",
                          "No AI system impact assessment found.",
                          "Clause 8.4 / Annex B", Severity.CRITICAL, _FW,
                          remediation="Conduct an AI system impact assessment per ISO/IEC 42001 Annex B, covering impacts on individuals, groups, and society.")

    def _check_supply_chain_controls(self) -> CheckResult:
        files = self._scan_for_keywords(["supply chain", "third party", "third-party", "vendor", "supplier", "external provider", "external ai"])
        if files:
            return self._pass("ISO-C8-003", "Supply chain and third-party AI controls documented",
                              "Supply chain/third-party controls found.", "Clause 8.3", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C8-003", "Supply chain and third-party AI controls documented",
                          "No supply chain or third-party AI controls documented.",
                          "Clause 8.3", Severity.HIGH, _FW,
                          remediation="Document controls for externally provided AI components: vetting criteria, contractual requirements, and ongoing monitoring.")

    def _check_incident_management(self) -> CheckResult:
        exists, path = self._file_exists(
            "docs/incident_management.md", "incident_management.md",
            "docs/incident_response.md", "incident_response.md",
        )
        if exists:
            return self._pass("ISO-C8-004", "AI incident management process documented",
                              "Incident management document found.", "Clause 8.5", Severity.HIGH, _FW, evidence=[path])
        files = self._scan_for_keywords(["incident management", "incident response", "incident procedure", "ai incident", "incident handling"])
        if files:
            return self._warn("ISO-C8-004", "AI incident management process documented",
                              "Incident management content found but no dedicated document.",
                              "Clause 8.5", Severity.HIGH, _FW, evidence=files[:3],
                              remediation="Create a dedicated AI incident management procedure document.")
        return self._fail("ISO-C8-004", "AI incident management process documented",
                          "No AI incident management process found.",
                          "Clause 8.5", Severity.HIGH, _FW,
                          remediation="Create docs/incident_management.md covering: detection, classification, response, recovery, reporting, and lessons learned.")

    # ── Clause 9 checks ───────────────────────────────────────────────────────

    def _check_monitoring_plan(self) -> CheckResult:
        files = self._scan_for_keywords(["monitoring", "measurement", "kpi", "metric", "performance indicator", "monitoring plan", "measurement plan"])
        if files:
            return self._pass("ISO-C9-001", "Monitoring and measurement plan exists",
                              "Monitoring/measurement plan found.", "Clause 9.1", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C9-001", "Monitoring and measurement plan exists",
                          "No monitoring and measurement plan found.",
                          "Clause 9.1", Severity.HIGH, _FW,
                          remediation="Create a monitoring and measurement plan: what to monitor, methods, timing, responsible parties, and how results are analysed.")

    def _check_internal_audit(self) -> CheckResult:
        files = self._scan_for_keywords(["internal audit", "audit programme", "audit plan", "audit schedule", "audit report", "aims audit"])
        if files:
            return self._pass("ISO-C9-002", "Internal audit programme documented",
                              "Internal audit documentation found.", "Clause 9.2", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C9-002", "Internal audit programme documented",
                          "No internal audit programme found.",
                          "Clause 9.2", Severity.HIGH, _FW,
                          remediation="Establish an internal audit programme for the AIMS: frequency, methodology, auditor criteria, and record-keeping requirements.")

    def _check_management_review(self) -> CheckResult:
        files = self._scan_for_keywords(["management review", "management meeting", "review meeting", "board review", "quarterly review", "aims review"])
        if files:
            return self._pass("ISO-C9-003", "Management review records maintained",
                              "Management review records found.", "Clause 9.3", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("ISO-C9-003", "Management review records maintained",
                          "No management review records found.",
                          "Clause 9.3", Severity.MEDIUM, _FW,
                          remediation="Retain records of management reviews of the AIMS, including inputs reviewed, decisions made, and action items assigned.")

    # ── Clause 10 checks ──────────────────────────────────────────────────────

    def _check_corrective_actions(self) -> CheckResult:
        files = self._scan_for_keywords(["corrective action", "nonconformity", "non-conformity", "remediation record", "corrective measure", "ncr"])
        if files:
            return self._pass("ISO-C10-001", "Nonconformity and corrective action process exists",
                              "Corrective action documentation found.", "Clause 10.2", Severity.HIGH, _FW, evidence=files[:3])
        return self._fail("ISO-C10-001", "Nonconformity and corrective action process exists",
                          "No nonconformity or corrective action process found.",
                          "Clause 10.2", Severity.HIGH, _FW,
                          remediation="Document a nonconformity and corrective action process: how to identify, classify, root-cause analyse, remediate, and verify nonconformities.")

    def _check_continual_improvement(self) -> CheckResult:
        files = self._scan_for_keywords(["continual improvement", "continuous improvement", "improvement plan", "improvement objective", "kaizen", "enhancement"])
        if files:
            return self._pass("ISO-C10-002", "Continual improvement objectives documented",
                              "Continual improvement documentation found.", "Clause 10.3", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("ISO-C10-002", "Continual improvement objectives documented",
                          "No continual improvement objectives documented.",
                          "Clause 10.3", Severity.MEDIUM, _FW,
                          remediation="Document continual improvement objectives for the AIMS and how progress is tracked and reviewed.")

    def _check_lessons_learned(self) -> CheckResult:
        files = self._scan_for_keywords(["lessons learned", "lessons learnt", "post-mortem", "retrospective", "after-action review", "incident review"])
        if files:
            return self._pass("ISO-C10-003", "Lessons learned process documented",
                              "Lessons learned documentation found.", "Clause 10.1", Severity.MEDIUM, _FW, evidence=files[:3])
        return self._warn("ISO-C10-003", "Lessons learned process documented",
                          "No lessons learned process found.",
                          "Clause 10.1", Severity.MEDIUM, _FW,
                          remediation="Document a lessons learned process: how insights from AI incidents, audits, and reviews are captured and applied to AIMS improvement.")
