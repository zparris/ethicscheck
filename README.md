# EthicsCheck

[![CI](https://github.com/zparris/ethicscheck/actions/workflows/ci.yml/badge.svg)](https://github.com/zparris/ethicscheck/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/downloads/)

**The Snyk for AI ethics.** CLI-first compliance checking for the EU AI Act, NIST AI RMF, and ISO/IEC 42001 — designed for developers and CI/CD pipelines, not GRC officers.

```
$ ethicscheck audit .

EthicsCheck v0.1.0
  Target    : .
  Frameworks: eu-ai-act, nist-rmf
  Fail-on   : high

EU AI Act ─────────────────────────────────────────────────────
  ✗ CRITICAL  EU-ART9-001   Art. 9(1)       Risk management system documented
  ✗ CRITICAL  EU-ART10-003  Art. 10(2)(f)   Bias examination performed
  ✓ HIGH      EU-ART13-001  Art. 13(1)      Instructions for use documented
  ...

Overall: FAIL — 8 critical, 14 high-severity gaps found
```

---

## Why EthicsCheck?

- **Regulatory deadline is real.** The EU AI Act's high-risk system obligations become enforceable on **August 2, 2026**. Penalties reach €15M or 3% of global turnover. GPAI model obligations are already in force (August 2, 2025).
- **No open-source CLI competitor exists.** Enterprise platforms (Credo AI, Holistic AI) cost $50–200K/year and target compliance teams. Academic libraries (IBM AIF360, Fairlearn) target notebook data scientists. No tool serves the CI/CD developer — until now.
- **Developer-first design.** Point it at a directory. Get pass/fail exit codes. Pipe JSON into your pipeline. Integrate in under 5 minutes.

---

## Installation

**Recommended — install as a global tool with [uv](https://docs.astral.sh/uv/):**

```bash
uv tool install ethicscheck
```

**With pip:**

```bash
pip install ethicscheck
```

**From source:**

```bash
git clone https://github.com/zparris/ethicscheck
cd ethicscheck
uv tool install .
```

Requires Python 3.10+.

---

## Quick Start

```bash
# Initialise a config file in your project
ethicscheck init

# Run a full audit against the default frameworks (EU AI Act + NIST AI RMF)
ethicscheck audit .

# Audit against a specific framework
ethicscheck audit . --framework eu-ai-act

# Get a machine-readable JSON report
ethicscheck audit . --output json > ethics-report.json

# Gate your CI pipeline — exits 1 if any HIGH or CRITICAL checks fail
ethicscheck audit . --fail-on high
```

---

## Commands

### `ethicscheck audit [TARGET]`

Run a full compliance audit against one or more frameworks.

```
Arguments:
  TARGET              Path to audit (file, directory, or project root). [default: .]

Options:
  -f, --framework     Framework to check. Repeatable. Choices: eu-ai-act, nist-rmf, iso-42001
  -c, --config        Path to .ethicscheck.yaml config file
  --fail-on           Severity threshold for non-zero exit. Choices: critical|high|medium|low [default: high]
  -o, --output        Output format. Choices: terminal|json|sarif [default: terminal]
  -q, --quiet         Suppress output; only set exit code
```

**Examples:**

```bash
ethicscheck audit .
ethicscheck audit ./my-model --framework eu-ai-act --framework nist-rmf
ethicscheck audit . --output json > report.json
ethicscheck audit . --output sarif > results.sarif
ethicscheck audit . --fail-on critical --quiet
```

---

### `ethicscheck check [CHECK_ID] [TARGET]`

Run a single named check by ID and get a detailed result.

```bash
ethicscheck check EU-ART9-001 .
ethicscheck check NIST-MEA-002 ./my-project
```

---

### `ethicscheck init`

Scaffold a `.ethicscheck.yaml` configuration file in the current directory.

```bash
ethicscheck init
ethicscheck init --output ./config/.ethicscheck.yaml
```

---

### `ethicscheck list-checks`

Display all 80 available checks with IDs, framework references, and severities.

```bash
ethicscheck list-checks
ethicscheck list-checks --framework eu-ai-act
ethicscheck list-checks --framework nist-rmf
```

---

## Frameworks

EthicsCheck covers **80 checks** across three globally adopted frameworks.

---

### EU AI Act — 31 checks

Regulation (EU) 2024/1689, the world's first binding, comprehensive AI law with extraterritorial reach. Penalties up to €15M or 3% of global turnover for high-risk violations.

- **High-risk obligations:** Enforceable **August 2, 2026**
- **GPAI model obligations:** Already in force since **August 2, 2025**

<details>
<summary>View all 31 EU AI Act checks</summary>

| Check ID | Article/Ref | Title | Severity |
|---|---|---|---|
| EU-ART9-001 | Art. 9(1) | Risk management system documented | 🔴 critical |
| EU-ART9-002 | Art. 9(2)(a) | Known and foreseeable risks identified | 🟠 high |
| EU-ART9-003 | Art. 9(2)(b) | Risk estimation under foreseeable misuse | 🟠 high |
| EU-ART9-004 | Art. 9(2)(d) | Risk mitigation measures adopted | 🟠 high |
| EU-ART9-005 | Art. 9(6)–(7) | Pre-deployment testing against defined thresholds | 🔴 critical |
| EU-ART10-001 | Art. 10(2) | Data governance practices documented | 🟠 high |
| EU-ART10-002 | Art. 10(2)(f) | Training data relevance and representativeness | 🟠 high |
| EU-ART10-003 | Art. 10(2)(f) | Bias examination performed | 🔴 critical |
| EU-ART10-004 | Art. 10(2)(g) | Data gap identification documented | 🟡 medium |
| EU-ART11-001 | Art. 11(1) | Technical documentation exists (Annex IV) | 🔴 critical |
| EU-ART11-002 | Annex IV §1 | General system description present | 🟠 high |
| EU-ART11-003 | Annex IV §2 | Development process documented | 🟠 high |
| EU-ART11-004 | Annex IV §3 | Performance metrics and limitations documented | 🟡 medium |
| EU-ART11-005 | Annex IV §6 | Lifecycle changes documented | 🟡 medium |
| EU-ART12-001 | Art. 12(1) | Automatic logging capability implemented | 🟠 high |
| EU-ART12-002 | Art. 12, Annex IV §2 | Logging system documented and verified | 🟠 high |
| EU-ART13-001 | Art. 13(1) | Instructions for use documented | 🟠 high |
| EU-ART13-002 | Art. 13(3)(b)(ii) | Accuracy and robustness metrics declared | 🟠 high |
| EU-ART13-003 | Art. 13(3)(b)(iii) | Known risks and limitations disclosed | 🟠 high |
| EU-ART14-001 | Art. 14(1) | Human oversight mechanism designed and documented | 🔴 critical |
| EU-ART14-002 | Art. 14(4)(e) | Override/stop capability implemented | 🔴 critical |
| EU-ART14-003 | Art. 14(4)(b) | Automation bias awareness documented | 🟡 medium |
| EU-ART15-001 | Art. 15(1) | Accuracy metrics declared with specific values | 🟠 high |
| EU-ART15-002 | Art. 15(3)–(4) | Robustness testing performed | 🟠 high |
| EU-ART15-003 | Art. 15(5) | Cybersecurity measures documented | 🟠 high |
| EU-ART15-004 | Art. 15(4) | Feedback loop mitigations for continually learning systems | 🟡 medium |
| EU-ANNIV-001 | Art. 47, Annex IV §8 | EU Declaration of Conformity prepared | 🔴 critical |
| EU-ANNIV-002 | Art. 72, Annex IV §9 | Post-market monitoring plan in place | 🟠 high |
| EU-GPAI-001 | Art. 53(1)(a), Annex XI | GPAI technical documentation maintained | 🟠 high |
| EU-GPAI-002 | Art. 53(1)(d), Annex XII | GPAI training data summary published | 🟠 high |
| EU-GPAI-003 | Art. 53(1)(c) | GPAI copyright compliance policy documented | 🟠 high |

</details>

---

### NIST AI RMF — 25 checks

NIST AI Risk Management Framework 1.0 (January 2023). Quasi-mandatory for US federal AI deployments under Executive Order 14110 and OMB M-24-10. The four functions — Govern, Map, Measure, Manage — are the de facto vocabulary for US enterprise AI risk.

<details>
<summary>View all 25 NIST AI RMF checks</summary>

| Check ID | Reference | Title | Severity |
|---|---|---|---|
| NIST-GOV-001 | GOVERN 1.1 | AI governance policy documented | 🔴 critical |
| NIST-GOV-002 | GOVERN 1.2 | AI risk appetite and tolerance defined | 🟠 high |
| NIST-GOV-003 | GOVERN 1.4 | Roles and accountability assigned | 🟠 high |
| NIST-GOV-004 | GOVERN 4.1 | Workforce AI risk training documented | 🟡 medium |
| NIST-GOV-005 | GOVERN 2.2 | Organisational AI oversight structure exists | 🟠 high |
| NIST-GOV-006 | GOVERN 1.7 | Policies address legal, regulatory, and compliance requirements | 🟠 high |
| NIST-MAP-001 | MAP 1.1 | Intended use and deployment context documented | 🔴 critical |
| NIST-MAP-002 | MAP 1.5 | Stakeholder impact assessment performed | 🟠 high |
| NIST-MAP-003 | MAP 2.2 | AI risk categories identified and catalogued | 🟠 high |
| NIST-MAP-004 | MAP 3.5 | Data provenance and lineage documented | 🟠 high |
| NIST-MAP-005 | MAP 5.1 | Third-party and supply chain AI risks assessed | 🟡 medium |
| NIST-MAP-006 | MAP 2.3 | Foreseeable negative impacts documented | 🟠 high |
| NIST-MEA-001 | MEASURE 1.1 | Trustworthiness metrics defined and documented | 🟠 high |
| NIST-MEA-002 | MEASURE 2.5 | Bias and fairness evaluation performed | 🔴 critical |
| NIST-MEA-003 | MEASURE 2.6 | Explainability and interpretability assessed | 🟠 high |
| NIST-MEA-004 | MEASURE 2.3 | Uncertainty and confidence quantified | 🟡 medium |
| NIST-MEA-005 | MEASURE 2.10 | Privacy risk evaluation documented | 🟠 high |
| NIST-MEA-006 | MEASURE 2.1 | Performance against benchmarks documented | 🟠 high |
| NIST-MEA-007 | MEASURE 4.1 | Ongoing performance monitoring plan documented | 🟠 high |
| NIST-MAN-001 | MANAGE 1.1 | Risk response plan documented | 🟠 high |
| NIST-MAN-002 | MANAGE 2.2 | Incident tracking and reporting mechanism exists | 🟠 high |
| NIST-MAN-003 | MANAGE 4.1 | Model decommissioning and sunset criteria defined | 🟡 medium |
| NIST-MAN-004 | MANAGE 2.4 | Continuous monitoring implemented and documented | 🟠 high |
| NIST-MAN-005 | MANAGE 1.3 | Residual risk accepted and documented | 🟡 medium |
| NIST-MAN-006 | MANAGE 2.1 | Human fallback and escalation procedure documented | 🔴 critical |

</details>

---

### ISO/IEC 42001 — 24 checks

ISO/IEC 42001:2023, the first certifiable AI management system standard. Compatible with the ISO 27001 audit process and expected to become the primary pathway to demonstrating EU AI Act compliance.

<details>
<summary>View all 24 ISO/IEC 42001 checks</summary>

| Check ID | Reference | Title | Severity |
|---|---|---|---|
| ISO-C4-001 | Clause 4.1 | Organisational context documented | 🟠 high |
| ISO-C4-002 | Clause 4.2 | Interested party needs and expectations identified | 🟠 high |
| ISO-C4-003 | Clause 4.3 | AIMS scope defined and documented | 🔴 critical |
| ISO-C4-004 | Clause 4.4 / Annex B | AI impact assessment criteria established | 🟠 high |
| ISO-C5-001 | Clause 5.2 | AI policy established and communicated | 🔴 critical |
| ISO-C5-002 | Clause 5.3 | AI roles and responsibilities assigned | 🟠 high |
| ISO-C5-003 | Clause 5.1 | Top management commitment demonstrated | 🟡 medium |
| ISO-C6-001 | Clause 6.1 | AI risks and opportunities assessed | 🔴 critical |
| ISO-C6-002 | Clause 6.2 | AI objectives defined and measurable | 🟠 high |
| ISO-C6-003 | Clause 6.3 | Change planning documented | 🟡 medium |
| ISO-C7-001 | Clause 7.2 | Competence and training records maintained | 🟠 high |
| ISO-C7-002 | Clause 7.3 | AI awareness programme documented | 🟡 medium |
| ISO-C7-003 | Clause 7.5 | AI documentation control procedures exist | 🟠 high |
| ISO-C7-004 | Clause 7.4 | Internal and external communication plan exists | 🟡 medium |
| ISO-C8-001 | Clause 8.1 | Operational planning and controls documented | 🟠 high |
| ISO-C8-002 | Clause 8.4 / Annex B | AI system impact assessment performed | 🔴 critical |
| ISO-C8-003 | Clause 8.3 | Supply chain and third-party AI controls documented | 🟠 high |
| ISO-C8-004 | Clause 8.5 | AI incident management process documented | 🟠 high |
| ISO-C9-001 | Clause 9.1 | Monitoring and measurement plan exists | 🟠 high |
| ISO-C9-002 | Clause 9.2 | Internal audit programme documented | 🟠 high |
| ISO-C9-003 | Clause 9.3 | Management review records maintained | 🟡 medium |
| ISO-C10-001 | Clause 10.2 | Nonconformity and corrective action process exists | 🟠 high |
| ISO-C10-002 | Clause 10.3 | Continual improvement objectives documented | 🟡 medium |
| ISO-C10-003 | Clause 10.1 | Lessons learned process documented | 🟡 medium |

</details>

---

## Output Formats

### Terminal (default)

Rich-formatted output with colour-coded results, per-framework summaries, and remediation hints for every failure.

### JSON

```bash
ethicscheck audit . --output json
```

```json
{
  "tool": "EthicsCheck",
  "version": "0.1.0",
  "timestamp": "2026-03-17T10:00:00",
  "target": ".",
  "overall_status": "fail",
  "critical_count": 4,
  "high_count": 11,
  "frameworks": [
    {
      "framework": "eu-ai-act",
      "passed": 6,
      "failed": 20,
      "warnings": 5,
      "score": 0.23,
      "checks": [...]
    }
  ]
}
```

### SARIF 2.1.0

```bash
ethicscheck audit . --output sarif > results.sarif
```

SARIF output is compatible with GitHub Advanced Security, Azure DevOps, and any SARIF-aware platform. Upload to GitHub to see compliance findings inline in pull requests:

```yaml
- name: Upload SARIF
  uses: github/codeql-action/upload-sarif@v3
  with:
    sarif_file: results.sarif
```

---

## CI/CD Integration

### GitHub Actions

```yaml
name: AI Ethics Check

on: [push, pull_request]

jobs:
  ethics:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install EthicsCheck
        run: pip install ethicscheck

      - name: Run compliance audit
        run: ethicscheck audit . --framework eu-ai-act --fail-on high

      - name: Upload SARIF report
        if: always()
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: ethics.sarif
        env:
          ETHICSCHECK_OUTPUT: sarif
```

### Exit codes

| Code | Meaning |
|---|---|
| `0` | All checks at or above the `--fail-on` threshold passed |
| `1` | One or more checks at or above the `--fail-on` threshold failed |
| `2` | Invalid arguments (unknown framework, bad config) |

The `--fail-on` flag sets the severity threshold:

```bash
--fail-on critical   # Only fail on critical gaps (most permissive)
--fail-on high       # Fail on critical or high (default, recommended)
--fail-on medium     # Fail on critical, high, or medium
--fail-on low        # Fail on anything (strictest)
```

### Environment variable overrides

```bash
ETHICSCHECK_FRAMEWORKS=eu-ai-act,nist-rmf ethicscheck audit .
ETHICSCHECK_FAIL_ON=critical ethicscheck audit .
```

---

## Configuration

Run `ethicscheck init` to scaffold a `.ethicscheck.yaml` in your project root. EthicsCheck walks up the directory tree to find it automatically.

```yaml
# .ethicscheck.yaml

# Frameworks to check against
frameworks:
  - eu-ai-act
  - nist-rmf
  # - iso-42001

# Minimum severity to fail the pipeline
# Choices: critical | high | medium | low
fail_on: high

# Output format for ethicscheck audit
# Choices: terminal | json | sarif
output_format: terminal

# Optional: tell EthicsCheck where your documentation lives
# Speeds up checks that look for specific files
model_card_path: ./docs/model_card.md
technical_docs_path: ./docs/technical_documentation.md
risk_assessment_path: ./docs/risk_assessment.md
data_governance_path: ./docs/data_governance.md

# Check IDs to skip — document the reason in a comment
skip_checks:
  # EU-ART15-004: System does not use continual learning
  - EU-ART15-004
```

---

## How checks work

EthicsCheck does not run your model or inspect model weights. It audits your **project's documentation and governance artefacts** — the same things a compliance auditor would look for. Each check:

1. **Looks for dedicated documentation files** (e.g. `docs/risk_assessment.md`, `risk_management.yaml`)
2. **Scans all Markdown, YAML, TOML, and text files** for required keywords (e.g. "bias examination", "human oversight", "foreseeable misuse")
3. **Returns PASS** if evidence is found, **WARN** if partial evidence exists, or **FAIL** with a specific remediation action if nothing is found

This means the more documentation your project has, the better your score. EthicsCheck is a documentation compliance checker — its job is to surface what's missing and tell you exactly how to fix it.

---

## Plugins

EthicsCheck is extensible. Any package can add new framework checks by registering an entry point in the `ethicscheck.frameworks` group — the same mechanism used by `pytest` plugins.

### Official plugin: `ethicscheck-plugin-callchain`

Detects AI framework imports in your Python code and maps them to the governance obligations they trigger.

```bash
pip install ethicscheck-plugin-callchain
```

Once installed, `ethicscheck audit .` automatically runs five additional checks:

| Check ID | Title | Severity |
|---|---|---|
| CC-IMPORT-001 | AI framework imports documented in technical docs | 🟠 high |
| CC-IMPORT-002 | Risk management plan exists for AI-integrated system | 🔴 critical |
| CC-BRANCH-001 | Human oversight mechanism present for AI-controlled branches | 🔴 critical |
| CC-DATA-001 | Data provenance documented for AI training/fine-tuning imports | 🟠 high |
| CC-SCOPE-001 | AI system boundary and scope documented | 🟡 medium |

Detects usage of: `openai`, `anthropic`, `langchain`, `transformers`, `torch`, `tensorflow`, `keras`, `sklearn`, `xgboost`, `lightgbm`, `cohere`, `mistralai`, `groq`, `together`, `replicate`, `diffusers`, `sentence_transformers`, `peft`, `trl`, and more.

Source: [github.com/zparris/ethicscheck-plugin-callchain](https://github.com/zparris/ethicscheck-plugin-callchain)

### Writing your own plugin

1. Create a class that extends `BaseFramework` from `ethicscheck.frameworks.base`
2. Implement `check_metadata()` and `run_check()`
3. Register the entry point in your `pyproject.toml`:

```toml
[project.entry-points."ethicscheck.frameworks"]
my-framework = "my_package:MyFrameworkClass"
```

EthicsCheck will discover and run it automatically at audit time. See `src/ethicscheck/frameworks/base.py` for the full `BaseFramework` API.

---

## Contributing

Contributions welcome — especially new checks, additional framework coverage, and improved keyword detection.

### Adding a new check

1. Pick the framework file: `src/ethicscheck/frameworks/eu_ai_act.py`, `nist_rmf.py`, or `iso_42001.py`
2. Add an entry to `check_metadata()`:
   ```python
   {"id": "EU-ART9-006", "title": "My new check", "ref": "Art. 9(X)", "severity": "high",
    "description": "What this check verifies."},
   ```
3. Add a dispatch entry in `run_check()`:
   ```python
   "EU-ART9-006": self._check_my_new_check,
   ```
4. Implement the check method using `_file_exists()`, `_scan_for_keywords()`, and the `_pass()` / `_warn()` / `_fail()` helpers from `BaseFramework` (`src/ethicscheck/frameworks/base.py`)
5. Add a test in `tests/test_eu_ai_act.py`
6. Submit a PR

### Development setup

```bash
git clone https://github.com/zparris/ethicscheck
cd ethicscheck
uv sync --extra dev
uv run pytest -v
uv run ruff check src/
```

---

## License

Apache-2.0 — see [LICENSE](LICENSE) for details.

Free to use, modify, and distribute. Contributions back to the project are welcome but not required.
