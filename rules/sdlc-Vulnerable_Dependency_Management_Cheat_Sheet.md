```yaml
---
trigger: glob
globs: [pom.xml, build.gradle, package.json, yarn.lock, requirements.txt, *.csproj, go.mod, vendor.json]
---

rule: "Vulnerable Dependency Management Best Practices"
summary: "Proactively detect, assess, and mitigate vulnerable dependencies to reduce security risks."
description: |
  Dependencies introduce security risks that must be managed early and continuously. Integrate automated vulnerability scanning from project inception, utilize tools covering multiple feeds (CVE and full disclosure), and ensure skilled security expertise is involved. Apply the correct mitigation approach based on patch availability, thoroughly test mitigations, and document all decisions clearly. Engage risk management for any accepted risks and prefer fixing issues at the application or dependency source.

severity: high

tags:
  - security
  - dependencies
  - supply-chain
  - vulnerability-management
  - devsecops

recommendations:
  - "Integrate automated vulnerability scanning tools (e.g., OWASP Dependency Check, NPM Audit) from project start and run scans continuously."
  - "Choose tools that aggregate multiple vulnerability feeds including CVE databases and full disclosure sources."
  - "Assign or consult with team members skilled in application security to analyze and prioritize findings."
  - "When a patched version is available, update dependencies first in test environments, verify with automated tests, resolve compatibility issues, then deploy to production promptly."
  - "If patches are delayed, apply provider workarounds or restrict vulnerable code paths with input validation or protective wrappers."
  - "In absence of fixes, consider patching internally, contribute fixes back if open source, and add compensating security controls based on vulnerability details (e.g., input sanitization)."
  - "Notify providers of unknown vulnerabilities with evidence and follow mitigation steps until fixes arrive."
  - "Identify and analyze both direct and transitive dependencies to understand exposure scope; act primarily on direct dependencies when possible."
  - "Maintain thorough automated tests covering impacted features to detect regressions during dependency updates."
  - "Document all vulnerability-related decisions, mitigations, and risk acceptances clearly for audit and knowledge sharing."
  - "Escalate any decision to accept risk to Chief Risk Officer or equivalent after detailed technical analysis including CVSS scoring."
  - "Favor mitigating vulnerabilities at the application or dependency source before relying on external security controls such as WAFs."

examples: |
  # Good practice example in CI pipeline snippet (pseudo):
  steps:
    - run: dependency-check --scan ./ --format XML --out reports/
    - run: npm audit --json > audit-report.json
    - run: ./custom-vuln-analysis script --input audit-report.json

notes: |
  Managing vulnerable dependencies is an ongoing effort combining automated tooling, skilled analysis, and clear governance to minimize security risks.
```