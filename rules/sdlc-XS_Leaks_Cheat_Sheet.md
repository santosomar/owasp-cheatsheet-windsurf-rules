```yaml
---
trigger: glob
globs: [js, ts, jsx, tsx, html, http, conf, env]
---

id: xs-leaks-best-practices
title: Prevent Cross-Site Leaks (XS-Leaks)
description: |
  Cross-Site Leaks exploit subtle browser behaviors to infer sensitive user data. Follow these best practices to protect your web app.

tags: security, xs-leaks, privacy, cookies, headers, cross-origin

rule: |
  1. **Set cookies securely:**
     - Always specify a `SameSite` attribute (`Strict` or `Lax`) on cookies to restrict cross-site sending.
     - Use `SameSite=None; Secure` only if third-party cross-site usage is required and HTTPS is enforced.
     - Avoid relying on defaults; explicitly set `SameSite` to prevent unexpected behavior.

  2. **Protect against framing attacks:**
     - Implement `Content-Security-Policy: frame-ancestors` to whitelist allowed framing origins.
     - As fallback or complement, set `X-Frame-Options` (`DENY` or `SAMEORIGIN`) headers.
     - Validate and handle the Fetch Metadata header `Sec-Fetch-Dest` to block unauthorized iframe embedding.

  3. **Secure sensitive endpoints:**
     - Use long, unpredictable per-user tokens in URLs or request parameters instead of guessable IDs.
     - Leverage `Sec-Fetch-Site` header to deny or restrict cross-site requests on sensitive APIs.
     - Apply `Cross-Origin-Resource-Policy (CORP)` headers (`same-origin` or `same-site`) to restrict resource sharing.

  4. **Use strict `postMessage` origins:**
     - Never use `"*"` as `targetOrigin` in `window.postMessage()`; always specify the exact origin string.

  5. **Mitigate frame counting attacks:**
     - Set `Cross-Origin-Opener-Policy` (e.g., `same-origin`) headers to isolate browsing contexts and prevent cross-origin access to `window.frames`.

  6. **Manage caching to prevent timing leaks:**
     - Include unpredictable per-user tokens in cacheable resource URLs to avoid attackers verifying cached content presence.
     - When possible, disable caching on sensitive resources via `Cache-Control: no-store` headers, balancing security and performance.

  7. **Adopt Fetch Metadata headers broadly:**
     - Use headers like `Sec-Fetch-Site`, `Sec-Fetch-Dest`, and `Sec-Fetch-Mode` to build policies that block unwanted cross-site requests.
     - Provide fallbacks for browsers that do not support Fetch Metadata.

  **Summary:**
  - Explicitly set `SameSite` on cookies.
  - Restrict framing via CSP frame-ancestors or X-Frame-Options.
  - Enforce Fetch Metadata headers on sensitive endpoints.
  - Never use `"*"` in `postMessage`.
  - Apply COOP headers for origin isolation.
  - Use tokens or disable caching on sensitive cached resources.
  - Continuously test and update based on browser support.

failure_message: |
  Your code or configuration is missing essential XS-Leak defenses:
  - Cookies lack explicit SameSite attribute.
  - No framing restrictions present.
  - Sensitive endpoints do not check Fetch Metadata headers or use unique tokens.
  - postMessage uses "*" as targetOrigin.
  - No COOP to isolate browsing contexts.
  - Sensitive cached resources lack protection.

fix_suggestion: |
  Review and update cookie settings to include SameSite.
  Implement CSP frame-ancestors or X-Frame-Options headers.
  Add server-side validation of Fetch Metadata headers on critical endpoints.
  Specify exact origin in all postMessage calls.
  Enable COOP headers (`same-origin`) for isolation.
  Add per-user tokens or disable caching on sensitive resources.
```
