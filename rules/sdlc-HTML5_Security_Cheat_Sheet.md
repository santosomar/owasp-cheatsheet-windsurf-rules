---
trigger: glob
globs: [js, jsx, ts, tsx, html]
---


  Follow OWASP HTML5 Security best practices to prevent vulnerabilities in your web app.
  Key actionable advice:
  - Web Messaging:
    * Always specify exact target origin in postMessage, never "*".
    * Verify `event.origin` strictly against trusted full domains; no partial matches.
    * Never use `eval()` or `innerHTML` on received message data; prefer safe APIs like `textContent`.
    * Treat all postMessage data as untrusted; validate and sanitize inputs.
  - CORS:
    * Restrict Access-Control-Allow-Origin to trusted origins, never use "*".
    * Validate URLs in XMLHttpRequests; avoid absolute URLs introducing open redirects or data leaks.
    * Reject mixed-content requests (HTTP requests from HTTPS pages).
  - WebSockets:
    * Use only secure `wss://` protocol and RFC 6455+ compliant versions.
    * Authenticate and authorize all connections at app level; never rely on WebSocket alone.
    * Verify Origin header strictly against whitelist on handshake.
    * Validate and parse messages safely (e.g., `JSON.parse`) and enforce JSON schema validation.
    * Implement token invalidation and denylist for revoked tokens.
    * Set limits on connection count and message size/timeouts to mitigate DoS.
    * Log authentication attempts and security events.
  - Client-Side Storage:
    * Never store sensitive tokens, credentials, or PII in localStorage or IndexedDB.
    * Prefer sessionStorage if persistence is not required.
    * Assume client storage data is untrusted.
    * Avoid multiple apps under same origin to prevent data leakage.
  - DOM and Browser API usage:
    * Add `rel="noopener noreferrer"` on all `<a target="_blank">` links.
    * When using `window.open()`, set `noopener,noreferrer` and `newWindow.opener = null`.
    * Use iframe `sandbox` attribute plus `X-Frame-Options` headers to prevent clickjacking.
  - Input Fields:
    * Use `autocomplete="off"`, `spellcheck="false"`, `autocorrect="off"`, and `autocapitalize="off"` on credential/PII inputs.
  - General Security Headers:
    * Implement CSP, X-Content-Type-Options, Referrer-Policy, and other recommended headers.
  - Other:
    * Validate messages to/from Web Workers; avoid creating workers from untrusted inputs.
    * Require explicit user permission before accessing Geolocation API.
    * Use explicit user consent for offline app caching.

  Adhering to these practices reduces risks of XSS, CSRF, clickjacking, data leakage, and DoS in modern HTML5 applications.

languages: [javascript, typescript, html]
```