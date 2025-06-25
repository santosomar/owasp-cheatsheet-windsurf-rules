```yaml
---
trigger: glob
globs: [js, mjs, cjs]
---

rule: nodejs-secure-coding-best-practices
message: |
  Follow these essential Node.js security best practices to protect your application:
    • Use async/await or flat Promise chains to avoid callback hell and improve error handling.
    • Limit request body size and validate content types to prevent resource exhaustion.
    • Avoid blocking the event loop with CPU-intensive or synchronous code; use async APIs.
    • Rigorously validate inputs with allow-lists and sanitize to prevent injection attacks.
    • Escape all output rendered in UIs to prevent XSS using trusted libraries.
    • Implement detailed application logging while protecting sensitive data.
    • Monitor event loop health (e.g., toobusy-js) and return HTTP 503 on overload.
    • Rate-limit authentication endpoints to mitigate brute-force attacks; consider CAPTCHAs and lockouts.
    • Protect state-changing requests with anti-CSRF tokens; avoid deprecated middleware.
    • Remove unnecessary routes to reduce attack surface.
    • Use the hpp module to prevent HTTP Parameter Pollution.
    • Return only necessary data fields in API responses to avoid data leaks.
    • Control object property mutability/visibility with JavaScript descriptors.
    • Enforce least privilege via RBAC or ACL modules.
    • Handle all errors properly; subscribe to 'uncaughtException' to log and safely shut down.
    • Always handle 'error' events on EventEmitters.
    • Set secure cookie flags: HttpOnly, Secure, and SameSite.
    • Use helmet to configure HTTP security headers: HSTS, frameguard, CSP, noSniff, disable X-XSS-Protection.
    • Disable caching on sensitive pages and remove X-Powered-By header to avoid info disclosure.
    • Keep dependencies up-to-date; audit regularly with npm audit and tools like Dependency-Check.
    • Avoid eval(), child_process.exec(), unsanitized fs and vm usage to prevent injection.
    • Test regexes for ReDoS and configure security-focused linting in your CI pipeline.
    • Enable strict mode ("use strict") throughout your codebase.
advise:
  - Enforce async patterns and validate all inputs strictly.
  - Implement thorough logging and monitor event loop health actively.
  - Apply layered protections for authentication and state-changing requests.
  - Harden HTTP headers using helmet and secure cookie flags.
  - Keep dependencies patched and avoid dangerous language features.
  - Handle errors on all asynchronous paths explicitly and safely shutdown on fatal exceptions.
  - Regularly incorporate automated security tooling in development and CI workflows.
```