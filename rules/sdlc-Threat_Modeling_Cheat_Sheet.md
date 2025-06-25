```yaml
---
trigger: glob
globs: [.js,.ts,.java,.py,.rb,.go,.cs,.php,.swift,.kt,.scala,.cpp,.c,.h]
---
id: owasp-threat-modeling-best-practices
name: OWASP Threat Modeling Best Practices
description: |
  Ensure proactive security by integrating threat modeling early and continuously in your development process.
  Use visual system modeling and systematic threat identification (e.g., STRIDE) to prioritize and mitigate risks effectively.
  Collaborate cross-functionally, document thoroughly, and validate models regularly.

tags: [security, threat modeling, architecture, design, STRIDE, DFD]

severity: INFO

patterns:
  - pattern-either:
      - pattern: |
          // Reminder: Have you created or updated a threat model for this feature/component?
      - pattern: |
          /* Have you modeled this system with Data Flow Diagrams (DFDs) to visualize trust boundaries and data flows? */
      - pattern: |
          // Use STRIDE to identify threats: Spoofing, Tampering, Repudiation, Information Disclosure, DoS, Elevation of Privilege
      - pattern: |
          /* Prioritize threats based on likelihood, impact, and cost-to-fix. */
      - pattern: |
          // Define actionable mitigation steps you can implement and test
      - pattern: |
          /* Collaborate with security experts and stakeholders; validate and document threat models */

message: |
  ⚠️ Security Best Practice: Threat modeling is essential to build secure systems proactively.
  - Start threat modeling early in design and update it continuously as your system evolves.
  - Clearly model your system using Data Flow Diagrams (DFDs) to understand trust boundaries and data flows.
  - Identify threats systematically using STRIDE categories.
  - Prioritize threats realistically based on likelihood and impact.
  - Develop concrete, testable mitigation plans informed by standards like OWASP ASVS.
  - Collaborate with your security team and stakeholders for review and validation.
  - Document your threat models and store artifacts accessibly for future reference.
  Neglecting threat modeling risks introducing preventable vulnerabilities.

help: |
  To improve your threat modeling process:
  1. Integrate threat modeling as a regular part of your design and development lifecycle.
  2. Use tools such as OWASP Threat Dragon, Microsoft Threat Modeling Tool, or code-based tools like pytm.
  3. Involve security experts and encourage developer training to foster a strong security culture.
  4. Prioritize and mitigate threats with actionable requirements that can be verified by testing.
  5. Keep documentation current to ensure ongoing security posture maintenance.

references:
  - https://owasp.org/www-project-threat-modeling/
  - https://owasp.org/www-project-threat-modeling-cheat-sheet/
  - https://owasp.org/www-project-application-security-verification-standard/
```