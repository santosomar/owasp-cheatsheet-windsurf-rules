```yaml
---
trigger: glob
globs: [js,jsx,ts,tsx,java,py,rb,php,go,c,cpp,cs]
---

id: owasp-authentication-best-practices
name: OWASP Authentication Cheat Sheet - Best Practices
severity: high
description: |
  Enforce secure and robust authentication mechanisms aligned with OWASP recommendations.

tags: [security, authentication, best-practices]

rules:
  - id: unique-user-identifiers
    message: Use unique, random user IDs and verify emails for login identification to prevent account enumeration.
    languages: [js,jsx,ts,tsx,java,py,rb,php,go,c,cpp,cs]
    patterns:
      - pattern-either:
          - pattern: "user.id = generateRandomId()"
          - pattern: "user.emailVerified == true"
    remediation: |
      Ensure user identifiers are unpredictable and email ownership is verified before login acceptance.

  - id: internal-account-protection
    message: Internal or sensitive accounts must NOT be exposed on public login forms and systems.
    remediation: |
      Separate internal account authentication from public-facing endpoints.

  - id: password-policy-guidance
    message: |
      Enforce a minimum password length of 8 characters; support passwords at least 64 characters long.
      Avoid forced composition rules; allow all Unicode and whitespace characters.
      Never silently truncate passwords.
    remediation: |
      Review password validation logic to comply with inclusive and user-friendly policies.

  - id: password-storage-and-comparison
    message: Store passwords using modern strong hashing (e.g., bcrypt, Argon2) and compare hashes using constant-time, type-safe functions.
    remediation: |
      Use libraries from OWASP Password Storage Cheat Sheet and avoid insecure comparison methods.

  - id: password-change-requirements
    message: Require verification of current password and an active session before allowing password changes.
    remediation: |
      Implement server-side checks to prevent unauthorized password resets or changes.

  - id: transport-layer-security
    message: Always use TLS/HTTPS to transmit credentials and session tokens.
    remediation: |
      Enforce HTTPS redirects and disable fallback to insecure HTTP.

  - id: generic-error-messages
    message: Return non-specific error messages (e.g. "Invalid username or password") on authentication failures to prevent user enumeration.
    remediation: |
      Avoid error details, varied HTTP status codes, or error URLs that reveal account state.

  - id: consistent-response-timing
    message: Normalize authentication response times regardless of failure reason to mitigate timing attacks.
    remediation: |
      Implement artificial delay or constant-time processing on login failures.

  - id: automated-attack-mitigation
    message: Implement MFA, throttling with exponential backoff per account, and CAPTCHAs after failed attempts.
    remediation: |
      Avoid relying solely on IP-based lockouts; prefer account-centric protections alongside MFA deployment.

  - id: password-manager-support
    message: Use standard HTML password input fields allowing paste and support passwords 64+ characters.
    remediation: |
      Avoid custom or plugin-based login methods that break password manager compatibility.

  - id: email-change-protocol
    message: Enforce strong identity verification (MFA or password re-entry) and dual confirmation via time-limited email links before changing registered email addresses.
    remediation: |
      Use nonces for verification and notify old email addresses to prevent account takeover.

  - id: logging-and-monitoring
    message: Log and monitor authentication failures, password failures, and account lockouts in real time.
    remediation: |
      Integrate with SIEMs or alerting tools to detect possible account attacks promptly.

  - id: modern-auth-protocols
    message: Use OAuth2, OpenID Connect, SAML 2.0, or FIDO U2F/UAF over password sharing for delegated or federated authentication.
    remediation: |
      Prefer modern, standardized protocols for authentication and authorization.

  - id: adaptive-authentication
    message: Implement risk-based authentication adjusting challenges dynamically based on device, location, and behavior risk assessment.
    remediation: |
      Define risk scoring and enforce step-up authentication or block suspicious activity accordingly.

summary: |
  - Secure authentication endpoints with TLS.
  - Use strong, user-friendly password policies without arbitrary complexity.
  - Prevent user enumeration with generic errors and consistent timing.
  - Deploy MFA, throttling, and CAPTCHA to protect against automated attacks.
  - Support modern auth protocols for delegated access.
  - Implement robust workflows for sensitive changes like password and email updates.
  - Log authentication events for real-time monitoring.
  - Adapt authentication strength dynamically based on risk signals.
  
  Following these practices will improve security while maintaining usability.
```