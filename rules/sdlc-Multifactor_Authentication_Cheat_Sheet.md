```yaml
---
trigger: glob
globs: [.js, .ts, .java, .py, .rb, .go, .cs, .php, .swift, .kt]
---

id: enforce-strong-mfa
title: Enforce Strong, Adaptive Multifactor Authentication (MFA)
shortdesc: Ensure applications implement true MFA using independent factors and adaptive risk-based controls.
description: |
  Multifactor Authentication (MFA) must require at least two independent factor categories (knowledge, possession, inherence, location, or behavior).
  Avoid relying on multiple factors of the same type (e.g., password + PIN) or weak factors like SMS or security questions.
  Enforce MFA on all authentication surfaces including APIs and mobile apps, especially on login and sensitive operations (password/email changes, privilege escalation).
  Incorporate adaptive risk-based authentication to minimize user friction while maximizing security.
  Provide secure MFA reset/recovery flows, alert users on failed MFA attempts, and educate users about securing their MFA credentials.
  Prefer hardware or software tokens like FIDO2/U2F or TOTP apps over weaker methods.
  Monitor and protect against MFA bypass attempts and service dependencies risks.

impact: high
tags: [security, authentication, mfa, multifactor]
references:
  - https://cheatsheetseries.owasp.org/cheatsheets/Multi-factor_Authentication_Cheat_Sheet.html

check: |
  # This pseudo-check outlines things to verify in code or config:
  # - MFA is enforced on login and sensitive actions.
  # - MFA factors are from independent categories, not just password variants.
  # - SMS & email codes are not primary MFA factors.
  # - Adaptive/risk-based MFA logic is present.
  # - MFA reset/recovery flows are secure and protected from easy bypass.
  # - User notification on failed MFA attempts is implemented.

fix: |
  1. Enforce MFA on all user authentication points, including login, API, and admin actions.
  2. Use strong MFA factors such as FIDO2/U2F hardware tokens or TOTP apps; avoid SMS, email, and security questions.
  3. Implement risk-based adaptive MFA to request additional factors only in high-risk scenarios.
  4. Design secure MFA recovery mechanisms (e.g., one-time recovery codes, multi-step verification).
  5. Notify users immediately on failed MFA attempts with contextual details (time, IP, device).
  6. Educate users on protecting their MFA credentials and device security.
  7. Regularly review MFA provider security posture and comply with regulatory MFA requirements.

examples:
  - good: |
      // Example: Enforce MFA with TOTP + password on login and sensitive actions
      if (user.login) {
        requirePassword();
        requireTOTP();
      }
      if (user.changingEmail || user.disablingMFA) {
        requirePassword();
        requireTOTP();
      }
    bad: |
      // Example: Weak MFA using only password + SMS or security questions
      if (user.login) {
        requirePassword();
        requireSMSCode();  // Avoid SMS as primary MFA
      }
      if (user.changingEmail) {
        requirePassword();
        askSecurityQuestion();  // Avoid security questions for MFA
      }
```