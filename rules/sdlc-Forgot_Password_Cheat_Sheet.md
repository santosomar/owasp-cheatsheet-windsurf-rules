```yaml
---
trigger: glob
globs: [js, ts, java, py, rb, php, go, cs]
---

id: forgot-password-security
name: Secure Forgot Password Implementation
description: |
  Ensure secure and robust forgot password functionality to prevent user enumeration,
  token abuse, and unauthorized access, following OWASP best practices.

rules:
  - id: consistent-responses
    message: >
      Always return uniform messages and response times for password reset requests
      to prevent user enumeration and timing attacks.
    severity: warning
    languages: [js, ts, java, py, rb, php, go, cs]

  - id: request-abuse-protection
    message: >
      Implement rate limiting and CAPTCHA on password reset requests to prevent abuse and flooding.
      Also, strictly validate all inputs to avoid injection vulnerabilities.
    severity: warning
    languages: [js, ts, java, py, rb, php, go, cs]

  - id: secure-token-generation
    message: >
      Use cryptographically secure, sufficiently long, unique tokens or PINs for password resets.
      Store tokens securely, make them single-use, and set short expiration times.
      Immediately invalidate tokens after use.
    severity: error
    languages: [js, ts, java, py, rb, php, go, cs]

  - id: secure-password-reset-workflow
    message: >
      Send reset tokens via secure channels (e.g., HTTPS email links).
      Avoid using untrusted headers (like Host) when building URLs to prevent host header attacks.
      Apply strict referrer policies (noreferrer) on reset pages.
      Require users to enter and confirm a strong new password.
      Do not auto-login users after resetting their password; require explicit login.
      Notify users via email of password changes without including passwords.
      Invalidate existing sessions post-reset to prevent session hijacking.
    severity: error
    languages: [js, ts, java, py, rb, php, go, cs]

  - id: identity-verification-methods
    message: >
      Prefer URL tokens sent via email for identity verification.
      If using PINs over SMS or other channels, ensure secure generation and handling.
      Avoid relying solely on security questions due to their weak security.
    severity: warning
    languages: [js, ts, java, py, rb, php, go, cs]

  - id: account-lockout-policy
    message: >
      Do NOT lock accounts after failed password reset attempts to prevent denial-of-service attacks.
    severity: info
    languages: [js, ts, java, py, rb, php, go, cs]
```