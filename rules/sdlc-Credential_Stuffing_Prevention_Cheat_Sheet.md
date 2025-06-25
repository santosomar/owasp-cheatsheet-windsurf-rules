---
trigger: glob
globs: .js, .jsx, .ts, .tsx, .java, .py, .rb, .php, .go, .cs
---

## Defending Against Credential Stuffing and Password Spraying Attacks

As a software engineer implementing authentication systems, you need to defend against automated attacks that leverage stolen credentials. These attacks are increasingly sophisticated, and a layered defense strategy is essential.

### 1. Multi-Factor Authentication (MFA): Your Primary Defense

MFA is your most effective defense against credential stuffing attacks. Even if attackers have valid credentials, MFA creates a significant barrier.

* **Implement Modern MFA Methods:** Prioritize phishing-resistant options like FIDO2 WebAuthn/Passkeys over SMS or email codes.

* **Apply Risk-Based MFA:** Use adaptive authentication that triggers MFA based on risk factors:
  ```javascript
  function shouldRequireMfa(request, user) {
    return (
      isNewDevice(request, user) ||
      isUnusualLocation(request, user) ||
      isKnownProxyOrVPN(request.ip) ||
      isHighRiskAction(request.path)
    );
  }
  ```

* **Make MFA User-Friendly:** Offer multiple MFA options and clearly explain their security benefits to encourage adoption.

### 2. Layered Controls: Defense in Depth

Implement multiple defensive layers to make automated attacks more difficult and costly:

* **CAPTCHA and Interactive Challenges:** Implement these selectively based on risk signals, not on every login attempt.

* **IP Reputation and Rate Limiting:** Instead of permanent IP blocks (which can affect legitimate users), implement:
  ```javascript
  // Tiered rate limiting example
  function getLoginRateLimit(ip, username) {
    const ipReputation = checkIpReputation(ip);
    
    if (ipReputation === 'known_bad') {
      return { maxAttempts: 3, windowSeconds: 3600 }; // 3 attempts per hour
    } else if (ipReputation === 'suspicious') {
      return { maxAttempts: 10, windowSeconds: 3600 }; // 10 attempts per hour
    } else {
      return { maxAttempts: 5, windowSeconds: 60 }; // 5 attempts per minute
    }
  }
  ```

* **Device Fingerprinting:** Track device characteristics to identify suspicious login patterns:
  ```javascript
  const deviceFingerprint = {
    userAgent: request.headers['user-agent'],
    acceptLanguage: request.headers['accept-language'],
    screenResolution: clientData.screenResolution,
    timezone: clientData.timezone,
    // More sophisticated: TLS JA3 fingerprint
    tlsFingerprint: getTlsJa3Hash(connection)
  };
  ```

* **Unpredictable Usernames:** If possible, avoid using email addresses as public usernames. Generate separate, non-sequential identifiers for users.

### 3. Multi-Step Authentication Flow

Design your login process to be resistant to simple scripting:

* **Client-Side Token Generation:** Require JavaScript execution to generate a token that must be submitted with login credentials.

* **Progressive Enhancement:** Ensure your authentication flow works without JavaScript but includes additional verification steps.

* **Login Sequence Validation:** Check that the sequence and timing of login steps match human behavior rather than automated scripts.

### 4. Breached Password Detection

Prevent users from using known compromised passwords:

```javascript
const isPasswordBreached = await checkHaveIBeenPwned(password);
if (isPasswordBreached) {
  return {
    success: false,
    message: "This password has appeared in a data breach. Please choose a different password."
  };
}
```

### 5. User Notification and Control

* **Notify on Suspicious Activity:** Alert users about unusual login attempts or successful logins from new devices.

* **Session Management:** Provide users with a dashboard showing all active sessions with the ability to terminate any session.

* **Login History:** Show users a history of recent logins with device and location information.

### 6. Monitoring and Continuous Improvement

* **Authentication Metrics:** Track login success rates, MFA usage, and challenge trigger rates.

* **Attack Pattern Detection:** Implement analytics to identify evolving attack patterns.

* **Regular Testing:** Conduct periodic testing of your defenses using the same tools attackers use.

By implementing these defenses in layers, you significantly increase the cost and difficulty for attackers while maintaining a good user experience for legitimate users.
