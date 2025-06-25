```yaml
---
trigger: glob
globs: [js, ts, java, py, rb, go, cs, php, swift, kt]
---

rule: enforce_standardized_security_logging
message: >
  Use standardized, structured logging for critical security events with consistent vocabulary,
  severity levels, and privacy-aware contextual metadata.
severity: warning
languages: [js, ts, java, py, rb, go, cs, php, swift, kt]
patterns:
  - pattern-either:
      - pattern: |
          log(ANY*, { event: /^authn_/, level: /INFO|WARN|CRITICAL/, datetime: /.+/, appid: /.+/, message: /.+/ })
      - pattern: |
          log(ANY*, { event: /^authz_/, level: /INFO|WARN|CRITICAL/, datetime: /.+/, appid: /.+/, message: /.+/ })
      - pattern: |
          log(ANY*, { event: /^session_/, level: /INFO|WARN|CRITICAL/, datetime: /.+/, appid: /.+/, message: /.+/ })
      - pattern: |
          log(ANY*, { event: /^fileupload_/, level: /INFO|WARN|CRITICAL/, datetime: /.+/, appid: /.+/, message: /.+/ })
      - pattern: |
          log(ANY*, { event: /^user_/, level: /INFO|WARN|CRITICAL/, datetime: /.+/, appid: /.+/, message: /.+/ })
      - pattern: |
          log(ANY*, { event: /^privilege_/, level: /INFO|WARN|CRITICAL/, datetime: /.+/, appid: /.+/, message: /.+/ })
      - pattern: |
          log(ANY*, { event: /^token_/, level: /INFO|WARN|CRITICAL/, datetime: /.+/, appid: /.+/, message: /.+/ })
      - pattern: |
          log(ANY*, { event: /^validation_/, level: /INFO|WARN|CRITICAL/, datetime: /.+/, appid: /.+/, message: /.+/ })
      - pattern: |
          log(ANY*, { event: /^system_/, level: /INFO|WARN|CRITICAL/, datetime: /.+/, appid: /.+/, message: /.+/ })
      - pattern: |
          log(ANY*, { event: /^malicious_/, level: /WARN|CRITICAL/, datetime: /.+/, appid: /.+/, message: /.+/ })
actions:
  - detect: |
      # Detect logging calls capturing security events
      # Validate presence of standardized event prefixes (authn_, authz_, session_, etc.)
      # Ensure logs contain ISO8601 datetime, appid, event, level, and descriptive message
      # Confirm severity levels consistent with event criticality (INFO, WARN, CRITICAL)
      # Check no direct logging of sensitive info like passwords or secrets
      # Recommend inclusion of contextual metadata (user IP, user agent), respecting privacy
  - suggest: |
      - Standardize your security event logging vocabulary (use prefixes like authn_, authz_)
      - Always log critical security events including successes, failures, authorization issues, session and token lifecycle, file uploads, validations, and system events
      - Structure logs in consistent JSON format containing datetime (ISO8601+UTC), appid, event, level, and message
      - Use severity levels to prioritize alerts: INFO for important actions, WARN for suspicious behavior, and CRITICAL for confirmed attacks
      - Avoid logging sensitive data such as passwords, secret keys, or PII beyond what is necessary and compliant with privacy regulations
      - Include contextual data (e.g., user IP, user agent) thoughtfully to facilitate investigations without compromising privacy
      - Ensure your code traps errors to reliably generate logs for security-relevant conditions
      - Collaborate with observability and incident response teams to automate ingestion and alerting based on these logs
      - Review and update logging continuously with application changes, especially in security-critical workflows
      - Incorporate threat modeling during design to identify security events requiring logging
```