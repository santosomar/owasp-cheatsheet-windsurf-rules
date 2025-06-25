---
trigger: glob
globs: .js, .ts, .java, .py, .rb, .go, .php, .cs
---

## Secure Logging Best Practices

As a software engineer, implementing proper logging is essential for security monitoring, troubleshooting, and compliance. This guide covers best practices for implementing secure, effective logging in your applications.

### What to Log

Separate security-relevant events from regular business logs to support detection, auditing, and incident response:

#### Security Events

* **Validation failures:** Both input and output validation issues
* **Authentication events:** Login attempts (successful and failed), password changes, MFA events
* **Authorization events:** Access control decisions, permission changes, privilege escalations
* **Session management:** Creation, expiration, and anomalies (suspicious token/cookie changes)
* **System events:** Application startup/shutdown, configuration changes, errors

#### High-Risk Operations

* Administrative actions and user account changes
* Cryptographic key usage and rotation
* Access to sensitive data or PII
* File uploads and downloads
* Deserialization operations
* Legal consent and permission changes
* Suspicious business logic behavior (e.g., workflow bypasses)

### Log Entry Structure

Each log entry should include these key attributes:

```javascript
// Example structured log entry (JSON format)
{
  "timestamp": "2025-06-25T14:22:33.456Z",  // When: ISO 8601 format with milliseconds
  "level": "WARNING",                      // Severity
  "event_id": "AUTH_FAILURE_005",          // Unique identifier for event type
  "source": {                             // Where
    "service": "user-auth-service",
    "instance": "auth-server-03",
    "environment": "production"
  },
  "client": {                             // Client information
    "ip": "192.168.1.10",
    "user_agent": "Mozilla/5.0...",
    "geo_location": "US-NY"
  },
  "user": {                               // Who
    "id": "user123",                      // Anonymized if needed
    "roles": ["standard_user"],
    "session_id": "sess_12345"
  },
  "action": {                             // What
    "type": "authentication",
    "operation": "login",
    "status": "failure",
    "reason": "invalid_credentials"
  },
  "details": {                            // Additional context
    "attempt_count": 3,
    "account_status": "active"
  }
}
```

### Sensitive Data Protection

* **Never log sensitive data in plaintext:**
  * Passwords or password hashes
  * Authentication tokens or session identifiers
  * API keys or encryption keys
  * Payment information (credit card numbers, etc.)
  * Personal identifiable information (PII)

* **When sensitive data must be logged:**
  * Mask or truncate values (e.g., `"cc": "XXXX-XXXX-XXXX-1234"`)
  * Hash identifiers that need correlation but not exposure
  * Use encryption for logs containing sensitive data

```java
// Example of proper PII handling in logs (Java)
public void logUserAction(User user, String action) {
    logger.info(
        "User action performed: action={}, userId={}, userType={}",
        action,
        anonymizeUserId(user.getId()),  // Hash or tokenize user ID
        user.getType()                  // Non-sensitive information
    );
    
    // NEVER do this:
    // logger.info("User {} ({}, {}) performed {}", 
    //     user.getName(), user.getEmail(), user.getSsn(), action);
}
```

### Implementation Guidelines

#### Use Established Logging Frameworks

* **Java:** SLF4J with Logback or Log4j2
* **JavaScript/Node.js:** Winston or Bunyan
* **Python:** Logging module or Structlog
* **Go:** Zap or Logrus
* **.NET:** Serilog or NLog

#### Prevent Log Injection

Sanitize inputs to prevent attackers from injecting malicious content into logs:

```python
# Python example of log sanitization
def sanitize_for_logging(input_string):
    if input_string is None:
        return None
    # Remove CR, LF and other control characters that could break log structure
    sanitized = re.sub(r'[\r\n\t\f\v]', ' ', str(input_string))
    # If using a structured format like JSON, escape accordingly
    return sanitized

def log_user_action(user_input, user_id):
    logger.info({
        "action": "user_input_received",
        "user_id": user_id,
        "input": sanitize_for_logging(user_input)
    })
```

#### Log Storage and Protection

* Store logs outside the web root directory
* Apply strict file permissions (e.g., read-only for application user)
* Use least privilege service accounts for log writing
* Implement log rotation to manage file sizes

### Log Management

#### Centralized Collection

* Forward logs to a centralized logging system (ELK Stack, Splunk, Graylog)
* Use standard formats like syslog, CEF, or JSON for easier integration
* Ensure secure transmission of logs (TLS/HTTPS)

```javascript
// Node.js example with Winston and centralized logging
const winston = require('winston');
require('winston-syslog');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    // Console for local development
    new winston.transports.Console(),
    // Local file for backup
    new winston.transports.File({ filename: 'application.log' }),
    // Remote syslog for centralized collection
    new winston.transports.Syslog({
      host: 'logserver.example.com',
      port: 514,
      protocol: 'tls4',
      app_name: 'my-service',
      facility: 'local0'
    })
  ]
});
```

#### Retention and Security

* Define and enforce log retention policies based on compliance requirements
* Implement secure log disposal procedures
* Encrypt logs at rest for sensitive environments
* Monitor and alert on logging failures or tampering

### Testing and Verification

* Include logging verification in your test suite
* Test for log injection vulnerabilities
* Verify that logging failures don't impact application availability
* Ensure consistent formatting across all log entries

By implementing these logging best practices, you'll create a robust audit trail that supports security monitoring, troubleshooting, and compliance requirements while protecting sensitive information.

Developer Actions:
- Design logs aligned with security and compliance needs—avoid under- or over-logging
- Always include full context (who, what, when, where, outcome) in security logs
- Sanitize or mask sensitive info before logging
- Ensure logs are securely stored, transmitted, and accessed
- Prevent log disabling or tampering by unauthorized users
- Integrate logging with monitoring and incident response
- Regularly review logging configurations, access, and retention policies

Following these guidelines will improve security visibility, enable faster incident detection, and reduce risks from log-related attacks.
```