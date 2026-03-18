"""Machine-readable output formats: JSON and SARIF 2.1.0."""
from __future__ import annotations
import json
from ..models import AuditReport, CheckStatus


def _fw_str(fw: object) -> str:
    """Return the framework identifier as a plain string.

    Works for both built-in Framework enum values and plugin-defined strings.
    """
    return fw.value if hasattr(fw, "value") else str(fw)  # type: ignore[union-attr]


def to_json(report: AuditReport) -> str:
    """Serialise an AuditReport to a JSON string."""
    data = report.model_dump(mode="json")
    return json.dumps(data, indent=2, default=str)


def to_sarif(report: AuditReport) -> str:
    """Serialise an AuditReport to SARIF 2.1.0 JSON.

    Spec: https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html
    One SARIF run per compliance framework. Only FAIL and WARN checks emit
    SARIF results; PASS/SKIP checks appear only in the rules list.
    """
    runs = []
    for fr in report.frameworks:
        rules = []
        results = []

        for check in fr.checks:
            # Build rule entry for every check
            rule = {
                "id": check.check_id,
                "name": check.title.replace(" ", "").replace("/", "").replace("-", ""),
                "shortDescription": {"text": check.title},
                "fullDescription": {"text": check.description},
                "help": {"text": check.remediation or check.description},
                "properties": {
                    "severity": check.severity.value,
                    "framework": _fw_str(check.framework),
                    "article_ref": check.article_ref,
                    "tags": [_fw_str(check.framework), check.article_ref],
                },
            }
            rules.append(rule)

            # Only FAIL and WARN produce SARIF result entries
            if check.status in (CheckStatus.FAIL, CheckStatus.WARN):
                level = "error" if check.status == CheckStatus.FAIL else "warning"
                message_text = check.description
                if check.remediation:
                    message_text += f" Remediation: {check.remediation}"

                result = {
                    "ruleId": check.check_id,
                    "level": level,
                    "message": {"text": message_text},
                    "locations": [
                        {
                            "physicalLocation": {
                                "artifactLocation": {
                                    "uri": report.target,
                                    "uriBaseId": "%SRCROOT%",
                                }
                            }
                        }
                    ],
                    "properties": {
                        "severity": check.severity.value,
                        "article_ref": check.article_ref,
                    },
                }
                if check.evidence:
                    result["properties"]["evidence"] = check.evidence
                results.append(result)

        run = {
            "tool": {
                "driver": {
                    "name": "EthicsCheck",
                    "version": report.version,
                    "informationUri": "https://ethicscheck.dev",
                    "rules": rules,
                }
            },
            "results": results,
            "properties": {
                "framework": _fw_str(fr.framework),
                "passed": fr.passed,
                "failed": fr.failed,
                "warnings": fr.warnings,
                "score": round(fr.score, 4),
            },
        }
        runs.append(run)

    sarif_doc = {
        "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
        "version": "2.1.0",
        "runs": runs,
    }
    return json.dumps(sarif_doc, indent=2)
