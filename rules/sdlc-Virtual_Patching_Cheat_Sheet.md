```yaml
---
trigger: glob
globs: [.js, .java, .py, .php, .rb, .go, .cs, .ts, .html, .xml, .json]
---

# OWASP Virtual Patching - Developer Security Guidance

# 1. Prioritize fixing vulnerabilities in your application code first. Virtual patching is a temporary mitigation layer, not a substitute for secure coding.

# 2. Prepare your environment before incidents happen:
#    - Deploy a Web Application Firewall (WAF), IPS, or ModSecurity early.
#    - Enable detailed HTTP request/response logging for incident analysis.
#    - Subscribe to and act on vulnerability advisories promptly.

# 3. When using virtual patches:
#    - Prefer positive security (allow-list) controls that strictly define expected input formats for parameters.
#      Example: Restrict IDs to digits only, enforce strict length and character rules.
#    - Use negative security (block-list) cautiously—avoid relying solely on blocking known malicious payloads.
#    - Design patches to minimize false positives (blocking legit users) and false negatives (missing attacks).

# 4. Follow the structured workflow:
#    identify → analyze → create virtual patch → test in "Log Only" mode → implement blocking → actively monitor → remove once code is fixed.

# 5. Collaborate closely with security teams to document virtual patches, handle exceptions, and review logs for attack trends and evasion attempts.

# 6. Automate patch creation where possible using integration tools that convert vulnerability scan outputs into virtual patch rules.

# By integrating virtual patching responsibly, you reduce your attack surface and safeguard users during vulnerability windows without waiting for full code remediation.
```