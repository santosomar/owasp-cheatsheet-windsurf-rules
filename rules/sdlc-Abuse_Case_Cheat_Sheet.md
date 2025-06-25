```yaml
---
trigger: glob
globs: [js, ts, java, py, rb, go, cs, cpp, swift, kotlin, php, html, jsx, tsx]
---
# OWASP Abuse Case Guidance

- Deeply understand each feature’s business purpose before coding; many exploits stem from business logic misuse rather than technical flaws.
- Participate or advocate for Abuse Case workshops that include business, security, risk, QA, and technical leads to identify concrete abuse scenarios early.
- Translate identified abuse cases into precise, feature-specific security requirements and acceptance criteria for development.
- Annotate code, design docs, or infrastructure configurations with unique abuse case IDs (e.g., `@AbuseCase(ids={"ABUSE_CASE_001"})`) to maintain traceability.
- Prioritize mitigation efforts using standardized risk scores (e.g., CVSS v3) to target the highest business impact issues.
- Implement and automate validation of abuse case mitigations via tests, static/dynamic analysis, code reviews, and pen testing integrated into CI/CD pipelines.
- Maintain and contribute to a centralized knowledge base of abuse cases and countermeasures to accelerate defense in future projects.
- Collaborate cross-functionally as security is a shared responsibility involving business, risk management, development, QA, and security teams.
- Ensure both technical and business-logic abuse cases are addressed to protect application functionality and revenue streams.

# BEST PRACTICES SUMMARY

*Transform vague “secure application” goals into concrete, business-aligned security tasks by defining and integrating abuse cases throughout the SDLC. Continuous tracking and validation ensure robust, pragmatic protection tailored to your product’s real risks.*

# FOLLOW THIS RULE TO:

✔ Identify and specify concrete abuse scenarios per feature  
✔ Embed abuse case IDs and mitigations in code and documentation  
✔ Prioritize fixes based on business risk rating  
✔ Automate testing and validation of abuse mitigations  
✔ Foster cross-team collaboration for comprehensive security  
```