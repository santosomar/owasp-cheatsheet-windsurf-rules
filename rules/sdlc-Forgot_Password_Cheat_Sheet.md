---
trigger: glob
globs: [js, ts, java, py, rb, php, go, cs]
---


name: Secure Forgot Password Implementation

  Ensure secure and robust forgot password functionality to prevent user enumeration,
  token abuse, and unauthorized access, following OWASP best practices.

rules:
  - 
    
      Always return uniform messages and response times for password reset requests
      to prevent user enumeration and timing attacks.
    
    languages: [js, ts, java, py, rb, php, go, cs]

  - 
    
      Implement rate limiting and CAPTCHA on password reset requests to prevent abuse and flooding.
      Also, strictly validate all inputs to avoid injection vulnerabilities.
    
    languages: [js, ts, java, py, rb, php, go, cs]

  - 
    
      Use cryptographically secure, sufficiently long, unique tokens or PINs for password resets.
      Store tokens securely, make them single-use, and set short expiration times.
      Immediately invalidate tokens after use.
    
    languages: [js, ts, java, py, rb, php, go, cs]

  - 
    
      Send reset tokens via secure channels (e.g., HTTPS email links).
      Avoid using untrusted headers (like Host) when building URLs to prevent host header attacks.
      Apply strict referrer policies (noreferrer) on reset pages.
      Require users to enter and confirm a strong new password.
      Do not auto-login users after resetting their password; require explicit login.
      Notify users via email of password changes without including passwords.
      Invalidate existing sessions post-reset to prevent session hijacking.
    
    languages: [js, ts, java, py, rb, php, go, cs]

  - 
    
      Prefer URL tokens sent via email for identity verification.
      If using PINs over SMS or other channels, ensure secure generation and handling.
      Avoid relying solely on security questions due to their weak security.
    
    languages: [js, ts, java, py, rb, php, go, cs]

  - 
    
      Do NOT lock accounts after failed password reset attempts to prevent denial-of-service attacks.
    
    languages: [js, ts, java, py, rb, php, go, cs]
```