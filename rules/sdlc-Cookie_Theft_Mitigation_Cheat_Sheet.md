---
trigger: glob
globs: .js, .ts, .jsx, .tsx, .java, .py, .rb, .php
---

## Cookie Theft Mitigation: Detecting and Preventing Session Hijacking

As a software engineer, you need to be aware that even with secure cookie settings (HttpOnly, Secure, SameSite), cookies can still be stolen through various attacks like XSS, malware, or physical access. Implementing server-side detection mechanisms is crucial to mitigate the impact of stolen session cookies.

### 1. Session Fingerprinting

When a user establishes a new session, capture and store a fingerprint of their environment:

```javascript
// Example in Express.js
app.post('/login', (req, res) => {
  // Authenticate user...
  
  // After successful authentication, save session fingerprint
  req.session.fingerprint = {
    ip: req.ip,
    userAgent: req.headers['user-agent'],
    acceptLanguage: req.headers['accept-language'],
    timestamp: new Date().toISOString(),
    // Optional additional headers
    acceptEncoding: req.headers['accept-encoding'],
    secFetchSite: req.headers['sec-fetch-site'], // Modern browsers only
    secChUa: req.headers['sec-ch-ua']            // Modern browsers only
  };
  
  // Continue with login process...
});
```

### 2. Continuous Validation

On subsequent requests, compare the current request context with the stored fingerprint:

```javascript
// Middleware for validating session fingerprint
function validateSessionFingerprint(req, res, next) {
  if (!req.session || !req.session.fingerprint) {
    return next(); // No session or fingerprint, let the auth middleware handle it
  }
  
  const fp = req.session.fingerprint;
  let suspiciousChanges = 0;
  
  // IP check (allow for some network changes)
  if (!isSameIpRange(fp.ip, req.ip)) {
    suspiciousChanges++;
  }
  
  // User-Agent check (allow for minor variations like browser updates)
  if (!isSimilarUserAgent(fp.userAgent, req.headers['user-agent'])) {
    suspiciousChanges++;
  }
  
  // Accept-Language check
  if (fp.acceptLanguage !== req.headers['accept-language']) {
    suspiciousChanges++;
  }
  
  // If multiple suspicious changes are detected
  if (suspiciousChanges >= 2) {
    // For sensitive operations, require additional verification
    if (isHighRiskEndpoint(req.path)) {
      return handleSuspiciousSession(req, res, next);
    }
  }
  
  next();
}
```

### 3. Responding to Suspicious Activity

When suspicious changes are detected, implement graduated responses based on risk:

```javascript
function handleSuspiciousSession(req, res, next) {
  // Log the suspicious activity
  logger.warn('Suspicious session detected', {
    sessionId: req.sessionID,
    originalFingerprint: req.session.fingerprint,
    currentRequest: {
      ip: req.ip,
      userAgent: req.headers['user-agent'],
      acceptLanguage: req.headers['accept-language']
    }
  });
  
  // For high-risk operations, require re-authentication
  if (req.path.startsWith('/account') || req.path.startsWith('/payment')) {
    req.session.requireReauth = true;
    return res.status(401).json({ 
      message: 'Please re-authenticate to continue',
      requireReauth: true 
    });
  }
  
  // For medium-risk operations, add a CAPTCHA challenge
  if (req.path.startsWith('/settings')) {
    req.session.requireCaptcha = true;
    return next();
  }
  
  // For all suspicious sessions, rotate the session ID
  const oldSession = {...req.session};
  req.session.regenerate((err) => {
    if (err) return next(err);
    
    // Transfer important session data to new session
    req.session.user = oldSession.user;
    req.session.fingerprint = {
      ip: req.ip,
      userAgent: req.headers['user-agent'],
      acceptLanguage: req.headers['accept-language'],
      timestamp: new Date().toISOString()
    };
    
    next();
  });
}
```

### 4. Implementation Best Practices

* **Performance Optimization**: Apply rigorous validation only to high-risk endpoints or actions.
* **Fuzzy Matching**: Use algorithms that allow for legitimate variations in headers (e.g., IP subnet matching rather than exact IP matching).
* **Contextual Risk Assessment**: Adjust validation strictness based on the sensitivity of the operation being performed.
* **Transparent User Experience**: When additional verification is required, clearly explain to users why it's happening.
* **Monitor False Positives**: Track cases where legitimate users are flagged to fine-tune your detection algorithms.

### 5. Future Enhancements

Stay informed about emerging standards like Device Bound Session Credentials (DBSC), which aim to cryptographically bind sessions to specific devices, making stolen cookies unusable on other devices.

By implementing these server-side detection mechanisms, you can significantly reduce the impact of cookie theft and session hijacking attacks, even when other defenses have been compromised.
