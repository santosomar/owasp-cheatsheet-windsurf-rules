---
trigger: glob
globs: [html, js, php, asp, aspx, jsp, nginx, apache, conf, config, json, yml, yaml]
---

Ensure your web application sets critical HTTP security headers to protect against XSS, clickjacking, MIME sniffing, information disclosure,
and enforce secure communication as recommended by OWASP. Use CSP as primary defense and combine with additional headers for robust protection.

tags: [security, http-headers, csp, clickjacking, cors, hsts, x-content-type-options, permissions-policy]

patterns:
  - pattern-either:
      # 1. Content-Security-Policy presence with frame-ancestors directive preferred
      - pattern: 'Content-Security-Policy: .*frame-ancestors'
      - pattern: 'Content-Security-Policy: .*'
      # 2. X-Frame-Options fallback
      - pattern: 'X-Frame-Options: DENY'
      # 3. X-XSS-Protection disabled explicitly
      - pattern: 'X-XSS-Protection: 0'
      # 4. X-Content-Type-Options nosniff present
      - pattern: 'X-Content-Type-Options: nosniff'
      # 5. Strict-Transport-Security with long max-age, includeSubDomains, preload
      - pattern: 'Strict-Transport-Security:.*max-age=63072000.*includeSubDomains.*preload'
      # 6. Server and related headers removed or sanitized (best effort detection)
      - pattern-not: 'Server: .+'
      - pattern-not: 'X-Powered-By: .+'
      - pattern-not: 'X-AspNet-Version: .+'
      - pattern-not: 'X-AspNetMvc-Version: .+'
      # 7. Referrer-Policy strict-origin-when-cross-origin
      - pattern: 'Referrer-Policy: strict-origin-when-cross-origin'
      # 8. Permissions-Policy disabling camera, microphone, geolocation, interest-cohort
      - pattern: 'Permissions-Policy: .*geolocation=\(\),.*camera=\(\),.*microphone=\(\),.*interest-cohort=\(\)'
      # 9. CORS Access-Control-Allow-Origin carefully set (not wildcard *)
      - pattern-not: 'Access-Control-Allow-Origin: \*'
      # 10. Cross-Origin Isolation Headers
      - pattern: 'Cross-Origin-Opener-Policy: same-origin'
      - pattern: 'Cross-Origin-Embedder-Policy: require-corp'
      - pattern: 'Cross-Origin-Resource-Policy: same-site'

  - pattern-not:
      # Deprecated or bad headers
      - pattern: 'Expect-CT:'
      - pattern: 'Public-Key-Pins:'
      - pattern: 'Public-Key-Pins-Report-Only:'

  Your HTTP response headers are missing or misconfigured critical security headers recommended by OWASP:

  - Implement a strong Content-Security-Policy including `frame-ancestors` directive; disable inline scripts.
  - Use `X-Frame-Options: DENY` only if CSP frame-ancestors is not supported.
  - Explicitly disable `X-XSS-Protection` with `X-XSS-Protection: 0`.
  - Always set `X-Content-Type-Options: nosniff`.
  - Configure `Strict-Transport-Security` with `max-age=63072000; includeSubDomains; preload`.
  - Remove or sanitize `Server`, `X-Powered-By`, `X-AspNet-Version`, and `X-AspNetMvc-Version` headers.
  - Set `Referrer-Policy: strict-origin-when-cross-origin`.
  - Use `Permissions-Policy` to disable camera, microphone, geolocation, and block FLoC (`interest-cohort=()`).
  - Avoid wildcard `Access-Control-Allow-Origin`; whitelist specific origins instead.
  - Add cross-origin isolation headers to mitigate modern attacks:  
    `Cross-Origin-Opener-Policy: same-origin`  
    `Cross-Origin-Embedder-Policy: require-corp`  
    `Cross-Origin-Resource-Policy: same-site`.
  - Do not use deprecated headers like `Expect-CT` or `Public-Key-Pins`.

  Regularly verify your header configurations with tools like Mozilla Observatory or SmartScanner to maintain strong security posture.

recommendation: |
  Review and update your server or application code that sets HTTP response headers to comply with OWASP's HTTP Security Response Headers guidelines. Examples:

  - Use CSP with `frame-ancestors` to control framing and disable inline scripts.
  - Set headers in your web server config or application middleware. For example, in Express.js use Helmet middleware.
  - Test headers after deployment to avoid breaking functionality.
  - Remove any deprecated or informative headers that expose technology stacks.

  Ensuring these headers are set correctly significantly strengthens your app's defenses against XSS, clickjacking, MIME sniffing, information leakage, and network-level attacks.
