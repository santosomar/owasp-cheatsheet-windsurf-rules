---
trigger: glob
globs: .js, .ts, .jsx, .tsx, .html, .http, .conf, .env
---

## Preventing Cross-Site Leaks (XS-Leaks)

As a web developer, protecting your applications from Cross-Site Leaks is crucial for safeguarding user privacy. XS-Leaks are a class of vulnerabilities that exploit subtle browser behaviors to extract sensitive user information across origins. This guide covers practical defenses you can implement to protect your web applications.

### Understanding XS-Leaks

XS-Leaks occur when an attacker's website can infer information about a user's state on another website through side-channels like:

- Error messages
- Frame counting
- Resource timing
- Cache probing
- Response size detection

These attacks can reveal sensitive information such as whether a user is logged in, specific account details, or even extract data from cross-origin resources.

### Secure Cookie Configuration

Properly configured cookies are your first line of defense against XS-Leaks:

```javascript
// Setting cookies in JavaScript with secure attributes
document.cookie = "sessionId=abc123; SameSite=Strict; Secure; HttpOnly; Path=/";
```

For server-side cookie setting (example in Express.js):

```javascript
app.use(session({
  secret: 'your-secret-key',
  cookie: {
    sameSite: 'strict',  // Options: strict, lax, none
    secure: true,         // Requires HTTPS
    httpOnly: true        // Prevents JavaScript access
  }
}));
```

In your HTTP response headers:

```http
Set-Cookie: sessionId=abc123; SameSite=Strict; Secure; HttpOnly; Path=/
```

**Best practices:**

* **Always specify a `SameSite` attribute:**
  * Use `SameSite=Strict` for cookies related to sensitive actions
  * Use `SameSite=Lax` for cookies needed on normal navigation to your site
  * Use `SameSite=None; Secure` only when third-party usage is absolutely required

* **Never rely on browser defaults** as they may vary across browsers and versions

### Framing Protection

Prevent your site from being framed by potentially malicious sites:

```javascript
// In your Express.js application
app.use((req, res, next) => {
  // CSP frame-ancestors directive (modern approach)
  res.setHeader(
    'Content-Security-Policy',
    "frame-ancestors 'self' https://trusted-parent.com"
  );
  
  // X-Frame-Options (legacy fallback)
  res.setHeader('X-Frame-Options', 'SAMEORIGIN');
  
  next();
});
```

In your Nginx configuration:

```nginx
server {
  # Other configuration...
  
  add_header Content-Security-Policy "frame-ancestors 'self'" always;
  add_header X-Frame-Options "SAMEORIGIN" always;
}
```

### Validating Cross-Origin Requests

Use Fetch Metadata headers to detect and block suspicious cross-origin requests:

```javascript
// Express.js middleware for protecting sensitive endpoints
function secureEndpoint(req, res, next) {
  // Get Fetch Metadata headers
  const fetchSite = req.get('Sec-Fetch-Site') || 'unknown';
  const fetchMode = req.get('Sec-Fetch-Mode') || 'unknown';
  const fetchDest = req.get('Sec-Fetch-Dest') || 'unknown';
  
  // Block cross-site requests to sensitive endpoints
  if (fetchSite === 'cross-site' && req.path.startsWith('/api/sensitive')) {
    return res.status(403).send('Cross-site requests not allowed');
  }
  
  // Block embedding in iframes from untrusted sites
  if (fetchDest === 'iframe' && fetchSite === 'cross-site') {
    return res.status(403).send('Embedding not allowed');
  }
  
  next();
}

app.use(secureEndpoint);
```

### Secure Cross-Origin Communication

When using `postMessage` for cross-origin communication:

```javascript
// UNSAFE - Never do this
window.postMessage(sensitiveData, '*');

// SAFE - Always specify the exact target origin
window.postMessage(sensitiveData, 'https://trusted-receiver.com');

// When receiving messages, always verify the origin
window.addEventListener('message', (event) => {
  // Always verify message origin
  if (event.origin !== 'https://trusted-sender.com') {
    console.error('Received message from untrusted origin:', event.origin);
    return;
  }
  
  // Process the message
  processMessage(event.data);
});
```

### Isolating Browsing Contexts

Use Cross-Origin-Opener-Policy (COOP) to isolate your site from potential attackers:

```http
Cross-Origin-Opener-Policy: same-origin
```

In Express.js:

```javascript
app.use((req, res, next) => {
  res.setHeader('Cross-Origin-Opener-Policy', 'same-origin');
  next();
});
```

For maximum isolation, combine with Cross-Origin-Embedder-Policy (COEP):

```javascript
app.use((req, res, next) => {
  res.setHeader('Cross-Origin-Opener-Policy', 'same-origin');
  res.setHeader('Cross-Origin-Embedder-Policy', 'require-corp');
  next();
});
```

### Preventing Cache-Based Leaks

Protect sensitive resources from cache probing attacks:

```javascript
// Express.js middleware for sensitive endpoints
app.get('/api/sensitive-data', (req, res) => {
  // Add user-specific token to prevent cache probing
  const userToken = req.user.securityToken;
  
  // Disable caching for sensitive resources
  res.setHeader('Cache-Control', 'no-store');
  res.setHeader('Pragma', 'no-cache');
  
  // Add user token to response to ensure uniqueness
  const data = { userToken, sensitiveData: 'secret information' };
  res.json(data);
});
```

For static resources that might reveal user state:

```javascript
// Add user-specific tokens to URLs of sensitive resources
function getUserSpecificUrl(baseUrl) {
  const userToken = generateUserToken();
  return `${baseUrl}?token=${userToken}`;
}

const profileImageUrl = getUserSpecificUrl('/images/profile.jpg');
```

### Comprehensive Defense Strategy

Implement these headers for a robust defense against XS-Leaks:

```javascript
app.use((req, res, next) => {
  // Framing protection
  res.setHeader('Content-Security-Policy', "frame-ancestors 'self'");
  res.setHeader('X-Frame-Options', 'SAMEORIGIN');
  
  // Resource isolation
  res.setHeader('Cross-Origin-Resource-Policy', 'same-origin');
  res.setHeader('Cross-Origin-Opener-Policy', 'same-origin');
  
  // Cache control for dynamic content
  if (req.path.startsWith('/api/')) {
    res.setHeader('Cache-Control', 'no-store');
  }
  
  next();
});
```

### Testing Your Defenses

Regularly test your application for XS-Leak vulnerabilities:

1. Use browser developer tools to inspect headers on sensitive endpoints
2. Test cross-origin requests to ensure proper blocking
3. Verify cookie attributes are correctly set
4. Check that sensitive resources aren't cacheable across origins
5. Confirm postMessage implementations use explicit origins

### Browser Support Considerations

Some defenses like Fetch Metadata headers aren't supported in all browsers. Implement defense in depth:

```javascript
function secureEndpoint(req, res, next) {
  const fetchSite = req.get('Sec-Fetch-Site');
  
  // Primary defense: Use Fetch Metadata if available
  if (fetchSite && fetchSite === 'cross-site') {
    return res.status(403).send('Cross-site request blocked');
  }
  
  // Fallback: Check Origin/Referer headers
  const origin = req.get('Origin') || req.get('Referer') || '';
  if (origin && !isAllowedOrigin(origin)) {
    return res.status(403).send('Origin not allowed');
  }
  
  // Additional checks for sensitive operations
  if (req.path.includes('/sensitive') && !req.cookies.csrfToken) {
    return res.status(403).send('Missing CSRF token');
  }
  
  next();
}
```

By implementing these defenses, you'll significantly reduce the risk of XS-Leaks in your web applications, protecting your users' sensitive information from cross-origin attacks.

