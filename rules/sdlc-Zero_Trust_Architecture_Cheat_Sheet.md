---
trigger: glob
globs: .js, .ts, .java, .py, .go, .rb, .cs, .php, .swift, .kt, .scala, .sh, .yaml, .yml, .json
---

## Implementing Zero Trust Architecture

As a software engineer, implementing Zero Trust Architecture (ZTA) principles in your applications is essential for modern security. This guide provides practical approaches to apply Zero Trust concepts in your development work.

### Core Zero Trust Principles

Zero Trust is built on the principle of "never trust, always verify" and assumes that threats exist both outside and inside the network. Key concepts include:

- **No implicit trust** based on network location or asset ownership
- **Continuous verification** of identity and device health
- **Least privilege access** to resources and data
- **Microsegmentation** of networks and applications
- **Continuous monitoring** and analytics for threat detection

### Authentication & Authorization

#### Implement Strong Authentication

```javascript
// Node.js example using FIDO2/WebAuthn
const fido2 = require('@simplewebauthn/server');

// Register a credential (during user enrollment)
async function registerCredential(user, challenge, deviceInfo) {
  const options = fido2.generateRegistrationOptions({
    rpName: 'Your Application',
    rpID: 'yourdomain.com',
    userID: user.id,
    userName: user.email,
    challenge: challenge,
    attestationType: 'direct'
  });
  
  return options;
}

// Verify authentication attempt
async function verifyAuthentication(credential, expectedChallenge) {
  const verification = await fido2.verifyAuthenticationResponse({
    credential: credential,
    expectedChallenge: expectedChallenge,
    expectedOrigin: 'https://yourdomain.com',
    expectedRPID: 'yourdomain.com'
  });
  
  return verification.verified;
}
```

#### Context-Aware Authorization

Implement authorization that considers multiple factors:

```java
// Java example of context-aware authorization
public class ZeroTrustAuthorizationService {
    public boolean authorizeAccess(User user, Resource resource, AccessContext context) {
        // 1. Verify user identity
        if (!identityService.verifyIdentity(user)) {
            logFailedAttempt("Identity verification failed", user, resource, context);
            return false;
        }
        
        // 2. Check device health and compliance
        if (!deviceService.isCompliant(context.getDeviceId())) {
            logFailedAttempt("Device not compliant", user, resource, context);
            return false;
        }
        
        // 3. Evaluate risk score based on multiple factors
        int riskScore = riskEngine.calculateScore(user, resource, context);
        if (riskLevel > ACCEPTABLE_THRESHOLD) {
            logFailedAttempt("Risk score too high", user, resource, context);
            return false;
        }
        
        // 4. Check if user has required permissions
        if (!permissionService.hasPermission(user, resource, context.getRequestedAction())) {
            logFailedAttempt("Insufficient permissions", user, resource, context);
            return false;
        }
        
        // 5. Log successful access
        auditLogger.logAccess(user, resource, context);
        return true;
    }
}
```

#### Short-Lived Access Tokens

Implement token-based authentication with short lifetimes:

```python
# Python example using JWT with short expiration
import jwt
from datetime import datetime, timedelta

def generate_access_token(user_id, device_id, permissions):
    # Set token to expire in 15 minutes
    expiration = datetime.utcnow() + timedelta(minutes=15)
    
    payload = {
        'sub': user_id,
        'device_id': device_id,
        'permissions': permissions,
        'exp': expiration,
        'iat': datetime.utcnow(),
        'jti': str(uuid.uuid4())  # Unique token ID
    }
    
    # Sign with appropriate algorithm and key
    token = jwt.encode(payload, SECRET_KEY, algorithm='ES256')
    
    # Store token metadata for potential revocation
    store_token_metadata(user_id, payload['jti'], device_id, expiration)
    
    return token
```

### Secure Communication

#### Enforce TLS for All Communications

```go
// Go example of configuring a server with TLS 1.3
package main

import (
    "crypto/tls"
    "net/http"
)

func main() {
    // Configure TLS settings
    tlsConfig := &tls.Config{
        MinVersion: tls.VersionTLS13,
        CipherSuites: []uint16{
            tls.TLS_AES_128_GCM_SHA256,
            tls.TLS_AES_256_GCM_SHA384,
            tls.TLS_CHACHA20_POLY1305_SHA256,
        },
    }
    
    // Create server with TLS config
    server := &http.Server{
        Addr:      ":443",
        TLSConfig: tlsConfig,
        Handler:   yourHandler,
    }
    
    // Start server with TLS
    server.ListenAndServeTLS("cert.pem", "key.pem")
}
```

#### API Security

Implement comprehensive API security measures:

```typescript
// TypeScript example of API security middleware
import express from 'express';
import rateLimit from 'express-rate-limit';
import helmet from 'helmet';

const app = express();

// Set security headers
app.use(helmet());

// Rate limiting
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  standardHeaders: true,
  legacyHeaders: false,
});
app.use('/api/', apiLimiter);

// API authentication middleware
app.use('/api/', (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  
  if (!token) {
    return res.status(401).json({ error: 'Authentication required' });
  }
  
  try {
    // Verify token and extract user info
    const user = verifyAndDecodeToken(token);
    
    // Check if token has been revoked
    if (isTokenRevoked(token)) {
      return res.status(401).json({ error: 'Token revoked' });
    }
    
    // Add user info to request for downstream handlers
    req.user = user;
    next();
  } catch (error) {
    return res.status(401).json({ error: 'Invalid token' });
  }
});

// Payload validation middleware
app.use(express.json({
  verify: (req, res, buf) => {
    try {
      // Check if JSON is valid and meets schema requirements
      validateSchema(buf.toString(), req.path);
    } catch (e) {
      throw new Error('Invalid JSON payload');
    }
  },
  limit: '100kb' // Limit payload size
}));
```

### Monitoring and Logging

#### Comprehensive Logging

```csharp
// C# example of detailed security logging
public class SecurityLogger
{
    private readonly ILogger _logger;
    
    public SecurityLogger(ILogger logger)
    {
        _logger = logger;
    }
    
    public void LogAccessAttempt(string userId, string resourceId, bool success, AccessContext context)
    {
        var logEvent = new SecurityEvent
        {
            EventType = success ? "access_granted" : "access_denied",
            Timestamp = DateTime.UtcNow,
            UserId = userId,
            ResourceId = resourceId,
            IpAddress = context.IpAddress,
            DeviceId = context.DeviceId,
            DeviceHealth = context.DeviceHealthStatus,
            Location = context.GeoLocation,
            RequestedPermissions = context.RequestedPermissions,
            RiskScore = context.RiskScore
        };
        
        // Log with appropriate level
        if (success)
        {
            _logger.LogInformation("Access granted: {Event}", JsonSerializer.Serialize(logEvent));
        }
        else
        {
            _logger.LogWarning("Access denied: {Event}", JsonSerializer.Serialize(logEvent));
        }
    }
}
```

### Microsegmentation

Implement fine-grained network and application segmentation:

```yaml
# Kubernetes Network Policy example for microsegmentation
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-backend-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: api-backend
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 443
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
  - to:
    - namespaceSelector:
        matchLabels:
          name: monitoring
      podSelector:
        matchLabels:
          app: telemetry
    ports:
    - protocol: TCP
      port: 9090
```

### Implementing Zero Trust Incrementally

1. **Start with inventory and visibility**
   * Catalog all applications, services, and data flows
   * Identify critical assets and their access patterns

2. **Implement strong authentication**
   * Deploy MFA across all applications
   * Integrate with identity providers using standards like SAML or OIDC

3. **Enhance authorization**
   * Implement role-based access control (RBAC)
   * Add context-aware policies

4. **Secure communications**
   * Enforce TLS 1.3 for all traffic
   * Implement API gateways

5. **Add microsegmentation**
   * Segment networks and applications
   * Implement least-privilege access

6. **Deploy monitoring and analytics**
   * Implement comprehensive logging
   * Set up anomaly detection

### Handling Legacy Systems

For systems that cannot be directly modified to support Zero Trust:

1. **Deploy security proxies** in front of legacy applications
2. **Implement network segmentation** to isolate legacy systems
3. **Enhance monitoring** around legacy components
4. **Use API gateways** to mediate access to legacy services

```bash
# Example of using an identity-aware proxy for a legacy application
# Using Nginx with OAuth authentication

server {
    listen 443 ssl;
    server_name legacy-app.example.com;
    
    # SSL configuration
    ssl_certificate /etc/ssl/certs/server.crt;
    ssl_certificate_key /etc/ssl/private/server.key;
    ssl_protocols TLSv1.3;
    
    # OAuth authentication
    auth_request /auth;
    auth_request_set $auth_status $upstream_status;
    
    # If authentication successful, proxy to legacy app
    location / {
        proxy_pass http://legacy-app-internal:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-User $upstream_http_x_user;
    }
    
    # Authentication endpoint
    location = /auth {
        internal;
        proxy_pass http://auth-service:8081/validate;
        proxy_pass_request_body off;
        proxy_set_header Content-Length "";
        proxy_set_header X-Original-URI $request_uri;
    }
}
```

### Key Takeaways for Software Engineers

1. **Authentication and authorization must be continuous** - verify on every request, not just at login

2. **Context matters** - use device health, location, time, and behavior in access decisions

3. **Use defense in depth** - combine multiple security controls rather than relying on a single measure

4. **Prefer open standards** - use established authentication and authorization frameworks

5. **Log everything** - comprehensive logging is essential for detecting anomalies

If applicable, always confirm that this rule has been followed.