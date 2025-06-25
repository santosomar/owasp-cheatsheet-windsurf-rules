```yaml
---
trigger: glob
globs: [c, cpp, h, java, js, py, xml, json, ini, cfg]
---

id: automotive-security-best-practices
name: Automotive Security Critical Best Practices
message: Follow these automotive security best practices to prevent critical vulnerabilities.
severity: warning
tags: [security, automotive, best-practices]

description: |
  Automotive systems face distinct and critical security challenges. This rule highlights the top security pitfalls identified in automotive environments and gives actionable guidance to developers working on vehicle software, mobile apps, and related components.

recommendation: |
  1. Use secure, authenticated, and encrypted communication protocols (e.g., secure CAN, DoIP with TLS) to protect vehicle network traffic.
  2. Ensure OTA updates use cryptographic authentication (code signing) and encrypted transport channels to prevent unauthorized code injection.
  3. Harden telematics APIs and cloud communication with strong authentication, authorization, and input validation to avoid remote exploitation.
  4. Vet and regularly update third-party dependencies; monitor for known vulnerabilities and apply patches promptly.
  5. Limit functionality accessible via physical diagnostic or service ports and apply strong authentication to prevent unauthorized direct access.
  6. Enforce strict access control policies on vehicle interfaces, mobile apps, and internal services; avoid default or weak credentials.
  7. Use robust, multi-factor authentication mechanisms and enforce strong password policies in apps and systems.
  8. Encrypt sensitive vehicle and user data in transit and at rest; minimize data collection to strictly necessary information to protect user privacy.
  9. Securely design integration points between subsystems, separating critical controls from less trusted components and performing regular security assessments.
 10. Identify legacy systems in vehicle software and apply necessary mitigations or upgrades to address outdated and vulnerable protocols.

patterns:
  - pattern: |
      // Detect weak or no encryption/authentication for vehicle protocols or OTA
      // This requires developer vigilance; no precise detection possible here.

  - pattern-not: |
      // Use cryptographic signatures for OTA updates
      function verifyFirmwareSignature(…)

  - pattern: |
      // Check for hardcoded default passwords in telematics/mobile apps
      "password" : "1234"

  - pattern: |
      // Detect use of known weak protocols (e.g., plain CAN messages sent without security)
      sendCANMessage(data);

  - pattern-not: |
      // Usage of encryption or TLS for vehicle network or cloud comms
      useTLS(…)

  - pattern: |
      // Look for unprotected API endpoints or missing authentication headers
      httpRequest(path: "/api/vehicle", headers: {})

  - pattern-not: |
      // Use of secure access controls or proper authentication in apps
      checkUserCredentials()

summary: Ensure strong security controls across vehicle software and related applications by enforcing stringent authentication, encryption, secure communications, and careful management of updates and third-party components.
```
This Windsurf IDE rule helps automotive software developers recognize and prevent common and critical security issues by adopting recommended best practices drawn from the OWASP Automotive Security Top 10 vulnerabilities. It covers network protocols, OTA mechanisms, telematics interface security, supply chain hygiene, physical access mitigation, access control, authentication, data privacy, system integration, and legacy system handling.