---
trigger: glob
globs: [.js, .ts, .java, .php, .py, .rb, .go, .cs, .scala, .kt, .swift]
---

OWASP Session Management Best Practices

1. Secure Session ID Generation
- Use a cryptographically secure pseudo-random number generator (CSPRNG) for session IDs.
- Ensure session IDs provide at least 64 bits of entropy (minimum 16 hex characters).
- Avoid meaningful or predictable content; session IDs must be opaque and fully random.
- Change default session ID names (e.g., “PHPSESSID”) to generic names like “id” to reduce fingerprinting.

2. Secure Session ID Exchange and Cookies
- Use cookies exclusively to transmit session IDs; avoid URLs or other exposed channels.
- Set cookies with these attributes:
  - Secure: Only send over HTTPS.
  - HttpOnly: Prevent JavaScript access to protect against XSS.
  - SameSite: Prefer `Strict` or `Lax` to mitigate CSRF.
  - Domain/Path: Scope cookies narrowly to minimize cross-subdomain exposure.
  - Avoid persistent cookies for session IDs; no `Expires` or `Max-Age` to enforce non-persistence.
- Enforce HTTPS site-wide with HSTS to safeguard cookie transmission.

3. Robust Session Lifecycle Management
- Regenerate session IDs after any privilege change (login, role change, password update).
- Reject session IDs that were not created by the server.
- Use separate session IDs or cookie names for pre- and post-authentication states when feasible.
- Properly invalidate session IDs server- and client-side on logout or timeout.
- Implement idle timeouts (2–30 minutes) and absolute timeouts (hours as per app sensitivity).
- Optionally, renew session IDs periodically during active sessions to limit token reuse.

4. Session Expiration and Logout
- Provide a clear, accessible logout button that fully invalidates sessions server-side.
- Enforce session expiration on the server; do not rely solely on client-side controls.
- Set HTTP headers, especially `Cache-Control: no-store`, to prevent caching of sensitive pages and tokens.

5. Additional Security Controls and Monitoring
- Bind sessions to client properties (IP, User-Agent) for anomaly detection, but tolerate legitimate variations.
- Log session events (creation, renewal, destruction) using non-sensitive session-derived IDs (e.g., salted hashes).
- Detect and alert on session ID brute force or guessing attempts.
- Manage simultaneous sessions per user according to business policy; provide user controls when possible.

6. Client-Side Defense (Defense-in-Depth)
- Optionally enforce login timeouts and logout on browser/tab close via JavaScript.
- Prevent session sharing across tabs/windows where feasible.
- Remember: client-side controls complement but do not replace server-side security.

7. Use Framework and Platform Features
- Prefer built-in session management mechanisms, keep them updated, and configure securely.
- Avoid homegrown session management unless thoroughly reviewed for security.

8. Transport Layer Security
- Enforce HTTPS on all session exchanges (not just login).
- Do not mix HTTP and HTTPS within the same user session.
- Use HSTS headers to enforce HTTPS.

9. Modern Client-Side Storage Caution
- Avoid storing session tokens in localStorage or sessionStorage—accessible via JavaScript.
- For cases requiring JS access, consider Web Workers to isolate secrets.
- Never store session IDs in locations accessible to injected scripts (XSS risk).

10. Reauthentication Policies
- Require reauthentication (password + MFA) for sensitive events (password changes, new devices, recovery).

11. Web Application Firewall (WAF) Support
- Use WAFs to enforce cookie flags, detect session fixation, and assist session protection when code changes are limited.

Summary for Developers:
- Generate strong, fully random session IDs (≥64 bits entropy) via CSPRNG.
- Use appropriately flagged, narrowly scoped cookies over HTTPS with HSTS.
- Regenerate session IDs on privilege change; reject unknown IDs.
- Implement both idle and absolute session timeouts; provide full logout.
- Prevent sensitive page caching and secure session lifecycle events.
- Use well-maintained built-in session frameworks.
- Limit JavaScript-accessible session storage; isolate with Web Workers if necessary.
- Monitor and respond to session abuse attempts.
- Incorporate reauthentication and consider WAF protections.
