---
trigger: glob
globs: .js, .ts, .java, .py, .rb, .go, .cs, .php, .swift, .kt
---

## Standardized Security Event Logging Vocabulary

As a software engineer, using consistent terminology and structure in your security logs is crucial for effective monitoring, alerting, and incident response. This guide provides a standardized vocabulary for security event logging to ensure clarity and consistency across your applications.

### Event Categorization

Use these standard prefixes to categorize security events in your logs:

| Event Prefix | Description | Examples |
|-------------|-------------|----------|
| `authn_` | Authentication events | `authn_success`, `authn_failure`, `authn_lockout` |
| `authz_` | Authorization events | `authz_denied`, `authz_granted`, `authz_elevation` |
| `session_` | Session management | `session_created`, `session_expired`, `session_invalidated` |
| `token_` | Token lifecycle events | `token_issued`, `token_refreshed`, `token_revoked` |
| `user_` | User account actions | `user_created`, `user_modified`, `user_deleted` |
| `privilege_` | Privilege changes | `privilege_granted`, `privilege_revoked`, `privilege_modified` |
| `fileupload_` | File upload operations | `fileupload_success`, `fileupload_rejected`, `fileupload_scanned` |
| `validation_` | Input validation events | `validation_failure`, `validation_bypass_attempt` |
| `system_` | System-level events | `system_startup`, `system_shutdown`, `system_error` |
| `malicious_` | Detected attack attempts | `malicious_injection`, `malicious_scanning`, `malicious_payload` |

### Log Structure

Implement structured logging with these standard fields for all security events:

```javascript
// Example structured security event log (JSON format)
{
  "datetime": "2025-06-25T14:30:45.123Z",  // ISO8601 with UTC timezone
  "appid": "payment-service",              // Application identifier
  "event": "authn_failure",               // Event using standard prefix
  "level": "WARN",                       // Severity level
  "message": "Failed login attempt for user",  // Human-readable description
  
  // Context - include as appropriate while respecting privacy
  "context": {
    "user_id": "u123456",                // User identifier (anonymized if needed)
    "source_ip": "192.168.1.1",          // Origin IP address
    "user_agent": "Mozilla/5.0...",      // Browser/client information
    "request_id": "req-abc-123",         // Request correlation ID
    "attempt_count": 3                    // Additional relevant metadata
  },
  
  // Optional additional data specific to the event type
  "details": {
    "failure_reason": "invalid_credentials",
    "account_status": "active"
  }
}
```

### Severity Levels

Use consistent severity levels to enable proper alerting and prioritization:

* **INFO**: Normal but security-relevant operations
  * Successful authentication
  * Standard permission grants
  * Session creation/normal expiration

* **WARN**: Suspicious or potentially problematic events
  * Failed authentication attempts
  * Permission denials
  * Input validation failures
  * Unusual patterns of behavior

* **CRITICAL**: Confirmed security incidents or high-risk events
  * Multiple authentication failures from same source
  * Privilege escalation attempts
  * Detection of known attack patterns
  * Security control bypasses

### Implementation Examples

#### Node.js Example

```javascript
// Using structured logging with Winston
const winston = require('winston');

const logger = winston.createLogger({
  format: winston.format.json(),
  transports: [new winston.transports.Console()]
});

function logSecurityEvent(eventType, level, message, context = {}, details = {}) {
  // Validate that eventType uses standard prefix
  const validPrefixes = ['authn_', 'authz_', 'session_', 'user_', 'token_', 
                         'privilege_', 'fileupload_', 'validation_', 
                         'system_', 'malicious_'];
                         
  const hasValidPrefix = validPrefixes.some(prefix => eventType.startsWith(prefix));
  if (!hasValidPrefix) {
    console.warn(`Warning: Security event type '${eventType}' does not use standard prefix`);  
  }
  
  // Log with standardized structure
  logger.log({
    level,
    datetime: new Date().toISOString(),
    appid: process.env.APP_ID || 'unknown-app',
    event: eventType,
    message,
    context,
    details
  });
}

// Usage example
function handleLoginAttempt(username, success, req) {
  const eventType = success ? 'authn_success' : 'authn_failure';
  const level = success ? 'info' : 'warn';
  
  logSecurityEvent(
    eventType,
    level,
    success ? 'Successful login' : 'Failed login attempt',
    {
      user_id: anonymizeUser(username),
      source_ip: req.ip,
      user_agent: req.headers['user-agent']
    },
    success ? {} : { failure_reason: 'invalid_credentials' }
  );
}
```

#### Java Example

```java
// Using SLF4J with structured logging
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import net.logstash.logback.argument.StructuredArguments;

public class SecurityEventLogger {
    private static final Logger logger = LoggerFactory.getLogger(SecurityEventLogger.class);
    private final String appId;
    
    public SecurityEventLogger(String appId) {
        this.appId = appId;
    }
    
    public void logSecurityEvent(String eventType, String level, String message, 
                               Map<String, Object> context, Map<String, Object> details) {
        // Build event data
        Map<String, Object> eventData = new HashMap<>();
        eventData.put("datetime", Instant.now().toString());
        eventData.put("appid", appId);
        eventData.put("event", eventType);
        eventData.put("message", message);
        
        if (context != null) {
            eventData.put("context", context);
        }
        
        if (details != null) {
            eventData.put("details", details);
        }
        
        // Log with appropriate level
        switch(level.toUpperCase()) {
            case "INFO":
                logger.info(message, StructuredArguments.entries(eventData));
                break;
            case "WARN":
                logger.warn(message, StructuredArguments.entries(eventData));
                break;
            case "CRITICAL":
                logger.error(message, StructuredArguments.entries(eventData));
                break;
            default:
                logger.info(message, StructuredArguments.entries(eventData));
        }
    }
}
```

### Best Practices

1. **Consistency is key**: Use the standardized vocabulary across all applications in your organization

2. **Privacy by design**: Anonymize or pseudonymize personal data in logs according to privacy regulations

3. **Correlation**: Include request IDs or trace IDs to correlate events across distributed systems

4. **Automation**: Design logs to be easily parsed by security monitoring tools (SIEM, log analyzers)

5. **Collaboration**: Work with security teams to ensure logs contain the information needed for incident response

6. **Evolution**: Regularly review and update your logging vocabulary as new threat patterns emerge

By implementing this standardized security event logging vocabulary, you'll create logs that are more useful for security monitoring, incident response, and compliance reporting.
