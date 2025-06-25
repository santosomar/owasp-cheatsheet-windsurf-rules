```yaml
---
trigger: glob
globs: [js, ts, java, py, rb, go, php, cs]
---
# OWASP Logging Best Practices

# Purpose:
# Log security-relevant events separately from business logs to support detection, auditing, and incident response.

# What to Log:
# - Validation failures (input/output)
# - Authentication and authorization events (success and failure)
# - Session anomalies (e.g., suspicious token or cookie changes)
# - App/system errors and startup/shutdown events
# - High-risk operations (user/admin changes, key usage, sensitive data access, file uploads, deserialization errors)
# - Legal consent and permission changes
# - Suspicious business logic behavior (e.g., flow bypass)

# Minimum Event Attributes (Include in every log entry):
# - When: precise timestamps, synchronized across systems
# - Where: application/server info, client IP, geolocation if applicable
# - Who: user ID, roles, source IP
# - What: event type, severity, description, action attempted, outcome, reason

# Sensitive Data Handling:
# - Never log secrets or PII in plaintext (passwords, tokens, keys, payment info)
# - Mask, sanitize, hash or encrypt sensitive data if it must be logged
# - Avoid logging source code or internal system details
# - Respect legal and user consent constraints

# Implementation:
# - Use or extend mature logging frameworks
# - Sanitize inputs to prevent log injection (strip CR, LF, delimiters)
# - Encode logs appropriately for the chosen format
# - Store logs outside web-root with strict file permissions
# - Use least privilege credentials for log storage
# - Prefer standardized log formats (syslog, CEF) for centralized integration
# - Support configurable logging levels; critical security logs must never be disabled

# Log Management:
# - Centralize log collection (e.g., SIEM) for analysis and alerting
# - Protect logs from unauthorized access, tampering, and deletion
# - Encrypt logs at rest and in transit; use secure channels
# - Audit all access to logs
# - Alert on suspicious events and detect logging failures or tampering
# - Retain logs per policy and securely dispose expired data

# Testing & Verification:
# - Validate all logging during development and security testing
# - Test for log injection vulnerabilities and resilience to log flooding
# - Ensure logging failures don’t disrupt application availability
# - Verify consistent event formatting and classification

# Developer Actions:
# - Design logs aligned with security and compliance needs—avoid under- or over-logging
# - Always include full context (who, what, when, where, outcome) in security logs
# - Sanitize or mask sensitive info before logging
# - Ensure logs are securely stored, transmitted, and accessed
# - Prevent log disabling or tampering by unauthorized users
# - Integrate logging with monitoring and incident response
# - Regularly review logging configurations, access, and retention policies

# Following these guidelines will improve security visibility, enable faster incident detection, and reduce risks from log-related attacks.
```