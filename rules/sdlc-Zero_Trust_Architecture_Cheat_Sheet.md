```yaml
---
trigger: glob
globs: [.js, .ts, .java, .py, .go, .rb, .cs, .php, .swift, .kt, .scala, .sh, .yaml, .yml, .json]
---

rule:
  id: zero-trust-architecture-guidance
  message: >
    Follow Zero Trust Architecture (ZTA) best practices to protect applications and data:
    1) Never trust by default: enforce strong, context-aware authentication and authorization on every request.
    2) Integrate continuous device health and identity verification in access decisions.
    3) Encrypt all data in transit and at rest; use TLS 1.3+ for communications.
    4) Validate and sanitize all inputs and outputs rigorously.
    5) Use identity-aware proxies, WAFs, and robust API security measures.
    6) Log detailed access events for auditing and anomaly detection.
    7) Adopt open, phishing-resistant authentication standards like FIDO2, OAuth, and SAML.
    8) Incrementally roll out policies starting with critical systems; balance security with usability.
    9) Apply compensating controls for legacy systems, including proxies and strict network segmentation.
  severity: warning
  tags: [security, zero-trust, authentication, authorization, encryption, monitoring]

advise: |
  - Treat every user, device, and resource as untrusted by default; never rely solely on network location.
  - Enforce short-lived, dynamic access sessions with real-time policy evaluation including device posture.
  - Ensure all communication channels within and outside your infrastructure use strong encryption (TLS 1.3+).
  - Implement multi-factor authentication using phishing-resistant technologies (e.g. FIDO2 hardware keys).
  - Continuously monitor and verify device health, revoking access immediately upon suspicion or compromise.
  - Use identity-aware proxies and WAFs to validate and filter requests before processing.
  - Secure APIs with authentication, authorization, payload validation, and rate limiting.
  - Log all authentication and access events with sufficient detail for compliance and threat detection.
  - Phase your Zero Trust implementation: start with asset inventory and MFA, then micro-segmentation, then automated detection and response.
  - For legacy systems, add security proxies, isolate them in network segments, and monitor for anomalies.
  - Avoid vendor lock-in; prefer open standards and interoperability to maintain flexibility.
```