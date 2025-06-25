---
trigger: glob
globs: .js, .jsx, .ts, .tsx, .java, .py, .rb, .php, .go, .cs, .html, .config, .xml, .yml, .yaml
---

As a software engineer, building secure authentication is one of the most critical aspects of application development. Here are best practices to follow, aligned with OWASP recommendations.

### 1. User Identification and Passwords

*   **Prevent Account Enumeration:** Use non-public, random, and unique identifiers for users internally. For login, allow users to use their verified email address or a username, but ensure error messages are generic (e.g., "Invalid username or password") to prevent attackers from guessing valid accounts.
*   **Strong Password Policies:** Enforce a minimum password length of 8 characters and support up to at least 64 characters. Allow all characters, including Unicode and spaces, and avoid complex composition rules (e.g., "must have one uppercase, one number..."). Never truncate passwords.
*   **Secure Password Storage:** Store user passwords using a modern, strong, and slow hashing algorithm like **Argon2** (preferred) or **bcrypt**. Use a unique salt for each user.
*   **Support Password Managers:** Use standard `<input type="password">` fields and allow pasting to ensure compatibility with password managers.

### 2. Secure Authentication Process

*   **Use TLS Everywhere:** All communication transmitting credentials, session tokens, or any sensitive data must be over HTTPS.
*   **Constant-Time Comparisons:** When comparing password hashes, use a secure, constant-time comparison function to prevent timing attacks.
*   **Protect Against Automated Attacks:**
    *   **Throttling:** Implement account-based throttling with an exponential backoff on failed login attempts.
    *   **CAPTCHA:** Use CAPTCHA after a small number of failed attempts.
    *   **Multi-Factor Authentication (MFA):** This is one of the most effective controls. Encourage or enforce MFA for all users.

### 3. Account Management

*   **Secure Password Changes:** Before a user can change their password, require them to re-enter their current password.
*   **Secure Email Changes:** Changing a registered email address is a highly sensitive operation. Protect it by requiring strong identity verification (like MFA or password re-entry) and sending a confirmation link to both the old and new email addresses.
*   **Separate Internal Accounts:** Internal or administrative accounts should not be accessible from public login forms. Use a separate, more secure authentication system for internal users.

### 4. Modern Authentication and Monitoring

*   **Use Modern Protocols:** For delegated or federated authentication, use established protocols like **OAuth 2.0**, **OpenID Connect (OIDC)**, or **SAML**. Avoid building your own.
*   **Adaptive Authentication:** Implement risk-based authentication that can dynamically adjust security challenges. For example, require a step-up authentication (like an MFA prompt) if a user logs in from a new device or location.
*   **Log and Monitor:** Log all authentication successes and failures, password reset requests, and account lockouts. Monitor these logs in real-time to detect and respond to attacks.