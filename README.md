# EthicsCheck

AI ethics pre-deployment compliance checker for EU AI Act, NIST AI RMF, and ISO/IEC 42001.

```bash
ethicscheck audit .
ethicscheck audit . --framework eu-ai-act --fail-on high
ethicscheck audit . --output json > report.json
```
