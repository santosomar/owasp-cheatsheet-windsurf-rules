```yaml
---
trigger: glob
globs: [js, jsx, ts, tsx, java, py, rb, php, go, cs]
---
id: credential-stuffing-prevention
title: Prevent Credential Stuffing Attacks with MFA and Adaptive Controls
description: |
  Implement multi-factor authentication (MFA) with adaptive risk-based enforcement as your primary defense against credential stuffing and password spraying attacks.  
  Supplement MFA with layered controls including CAPTCHA, IP and device fingerprinting, unpredictable usernames, and multi-step login flows to build defense-in-depth.  
  Monitor and adjust controls dynamically based on attack patterns and user risk signals. Prevent use of leaked passwords and notify users of suspicious activities responsibly.

criteria:
  - Implement MFA using modern, phishing-resistant methods (e.g., FIDO2 Passkeys).
  - Apply adaptive MFA triggers on new devices, suspicious IPs/locations, known proxies/VPNs, or high-risk actions.
  - Use secondary controls (CAPTCHA, IP reputation throttling, secondary PINs) where MFA is not feasible.
  - Avoid relying solely on IP blocking; employ IP classification, geo-thresholds, and temporary blocklists with automated removal.
  - Implement device and connection fingerprinting (headers, TLS JA3 hashes) to detect anomalies and require step-up auth.
  - Avoid using email addresses as usernames; use unpredictable, non-sequential usernames wherever possible.
  - Design multi-step login flows requiring JavaScript token generation and checks to block automated scripted attacks.
  - Detect and mitigate headless browser automation when it does not conflict with accessibility.
  - Introduce degradation techniques (delays, complex JS challenges) to raise attack costs without harming legitimate users.
  - Integrate leaked password detection services during password selection; block or warn on compromised passwords.
  - Provide user notifications for high-risk events (e.g., successful password with failed MFA), showing recent logins and active sessions with user controls.
  - Consider account locking and additional verification on suspicious reset or login behavior.

recommendation: |
  1. **Primary Defense:** Deploy strong MFA, preferably modern phishing-resistant methods, and enforce it adaptively based on risk.
  2. **Layered Controls:** Combine CAPTCHA, IP reputation, device fingerprinting, user behavior analysis, and unpredictable usernames to complicate attacker efforts.
  3. **Login Flow:** Use multi-step, JavaScript-dependent authentication flows to thwart simple automated attacks.
  4. **Monitoring:** Collect metrics on authentication events and security controls to detect evolving attack patterns and failures.
  5. **User Experience:** Notify users only about actionable and high-risk events to avoid alert fatigue. Allow users to view and manage active sessions.
  6. **Prevent Compromised Password Use:** Integrate breached password checking at registration and password changes.
  7. **Continuous Improvement:** Regularly review and update controls balancing security effectiveness and usability.

impact: |
  Effective prevention of credential stuffing and password spraying attacks drastically reduces account takeover risk, protects user data, and strengthens overall application security posture.

references:
  - https://owasp.org/www-project-cheat-sheets/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html
  - https://fidoalliance.org/
  - https://haveibeenpwned.com/Passwords
```