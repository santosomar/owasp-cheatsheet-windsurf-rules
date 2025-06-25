```yaml
---
trigger: glob
globs: [java, py, cs, js, php, rb, pl, cfg, conf, ini, yaml, yml]
---

rule: Legacy Application Management Best Practices

description: >
  Legacy applications pose significant security risks due to outdated technology and lack of vendor support.
  Developers must implement robust controls to minimize exposure and prepare for migration.

severity: high

message: >
  Legacy app detected: ensure comprehensive documentation, enforce strict authentication and least privilege access,
  conduct regular vulnerability scans, encrypt data in transit and at rest,
  restrict network exposure, maintain institutional knowledge, plan phased migration,
  and implement continuous monitoring with incident preparedness.

recommendation:
  - Maintain an up-to-date inventory of legacy apps including versions, configurations, and hosting details.
  - Conduct risk assessments and prioritize remediation using established frameworks like NIST RMF.
  - Enforce least privilege access; restrict network access via IP allow-listing, subnet isolation, and by closing unused ports.
  - Require strong authentication at both network and application layers (e.g., VPN, Identity Providers).
  - Disable or limit high-risk features, especially administrative functions.
  - Where possible, implement intermediary services to avoid direct user access to legacy apps.
  - Perform automated vulnerability scans regularly (Nessus, Qualys) and static/dynamic code analysis.
  - Prioritize patching vulnerabilities based on severity and exploitability; if patching is impossible, increase access controls and monitoring.
  - Encrypt sensitive data both at rest and in transit; isolate legacy apps if encryption support is lacking.
  - Train multiple team members on legacy technologies and document troubleshooting and failure resolution processes.
  - Develop a phased migration plan to modern platforms with stakeholder engagement and clear business justification.
  - Monitor legacy application logs closely; build custom adapters if needed for integration with SIEMs.
  - Establish and document incident response and escalation procedures tailored for legacy systems and include them in business continuity plans.
```