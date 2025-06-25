---
trigger: glob
globs: .js, .ts, .java, .py, .rb, .go, .cs, .php, .swift, .kt
---

## Implementing Strong Multifactor Authentication

As a software engineer, implementing robust multifactor authentication (MFA) is essential for protecting user accounts and sensitive operations in your applications. This guide covers best practices for designing and implementing effective MFA systems.

### Understanding MFA Factor Categories

True MFA requires at least two factors from different categories:

1. **Knowledge factors** - something the user knows (passwords, PINs, security questions)
2. **Possession factors** - something the user has (hardware tokens, mobile devices, smart cards)
3. **Inherence factors** - something the user is (biometrics like fingerprints, facial recognition)
4. **Location factors** - somewhere the user is (geolocation, network location)
5. **Behavior factors** - something the user does (typing patterns, gesture patterns)

### MFA Implementation Best Practices

#### 1. Select Strong Authentication Factors

Choose robust MFA methods in order of preference:

**Recommended Options:**
* FIDO2/WebAuthn passkeys (biometric hardware tokens)
* Hardware security keys (YubiKey, Titan Security Key)
* Time-based One-Time Password (TOTP) apps (Google Authenticator, Authy)
* Push notifications with verification (Duo Security, Okta Verify)

**Less Secure Options (Use with Caution):**
* SMS or voice-based OTPs (vulnerable to SIM swapping)
* Email-based verification codes (vulnerable to account takeover)
* Security questions (often guessable or researchable)

```javascript
// Example: Implementing TOTP verification
const speakeasy = require('speakeasy');

function verifyTOTP(userSecret, userToken) {
  return speakeasy.totp.verify({
    secret: userSecret,
    encoding: 'base32',
    token: userToken,
    window: 1  // Allow 1 step before/after for time drift
  });
}

// Usage in authentication flow
app.post('/verify-mfa', (req, res) => {
  const { userId, totpToken } = req.body;
  const user = getUserById(userId);
  
  if (verifyTOTP(user.totpSecret, totpToken)) {
    // TOTP verification successful
    completeAuthentication(user, req, res);
  } else {
    // Failed verification
    logFailedAttempt(user, 'TOTP', req.ip);
    res.status(401).json({ error: 'Invalid authentication code' });
  }
});
```

#### 2. Enforce MFA on Critical Surfaces

Require MFA for all of these scenarios:

* Initial account login
* Password resets and recovery flows
* Email or phone number changes
* Financial transactions or sensitive data access
* Account permission changes
* MFA enrollment or disablement
* Administrative actions

```java
// Example: Java method to check if action requires MFA
public boolean requiresMFA(UserAction action, User user, HttpRequest request) {
    // Always require MFA for sensitive actions
    if (action == UserAction.CHANGE_PASSWORD || 
        action == UserAction.CHANGE_EMAIL || 
        action == UserAction.FINANCIAL_TRANSACTION) {
        return true;
    }
    
    // For login, use risk-based approach
    if (action == UserAction.LOGIN) {
        return riskEngine.calculateRiskScore(user, request) > RISK_THRESHOLD;
    }
    
    // For admin actions, always require MFA
    if (user.hasRole(Role.ADMIN)) {
        return true;
    }
    
    return false;
}
```

#### 3. Implement Adaptive Risk-Based Authentication

Minimize user friction while maintaining security by adapting MFA requirements based on risk signals:

```python
# Example: Python risk-based MFA decision
def should_require_mfa(user, request, action):
    # Calculate risk score based on various signals
    risk_score = 0
    
    # New device or location
    if not is_known_device(user, request.device_fingerprint):
        risk_score += 25
    
    # Unusual location
    if is_unusual_location(user, request.geo_location):
        risk_score += 20
    
    # Unusual time of access
    if is_unusual_time(user, request.timestamp):
        risk_score += 15
    
    # Suspicious IP address
    if is_suspicious_ip(request.ip_address):
        risk_score += 30
    
    # Sensitive action always requires MFA
    if action in SENSITIVE_ACTIONS:
        return True
    
    # Require MFA if risk score exceeds threshold
    return risk_score >= RISK_THRESHOLD
```

#### 4. Design Secure MFA Recovery Flows

Implement secure recovery mechanisms for when users lose access to their MFA devices:

* Generate one-time use recovery codes during MFA enrollment
* Require identity verification through multiple channels
* Implement cooling-off periods for recovery actions
* Log and notify about recovery attempts

```typescript
// Example: TypeScript recovery code generation
function generateRecoveryCodes(userId: string): string[] {
  const recoveryCodes: string[] = [];
  
  // Generate 10 secure random recovery codes
  for (let i = 0; i < 10; i++) {
    const code = crypto.randomBytes(10).toString('hex');
    recoveryCodes.push(code);
  }
  
  // Store hashed versions in the database
  const hashedCodes = recoveryCodes.map(code => hashCode(code));
  storeRecoveryCodes(userId, hashedCodes);
  
  // Return plain text codes to show to user ONCE
  return recoveryCodes;
}
```

#### 5. Implement User Notifications

Alert users about authentication events to help them identify unauthorized access attempts:

```csharp
// Example: C# notification for MFA events
public async Task NotifyUserOfMFAEvent(User user, MFAEvent eventType, RequestContext context)
{
    var notification = new UserNotification
    {
        UserId = user.Id,
        EventType = eventType,
        Timestamp = DateTime.UtcNow,
        IPAddress = context.IPAddress,
        DeviceInfo = context.UserAgent,
        Location = await GeolocateIP(context.IPAddress)
    };
    
    // Send immediate email for suspicious events
    if (eventType == MFAEvent.FailedAttempt || 
        eventType == MFAEvent.DisabledMFA || 
        eventType == MFAEvent.RecoveryCodeUsed)
    {
        await _emailService.SendUrgentNotification(user.Email, notification);
    }
    
    // Log all events
    await _notificationRepository.LogNotification(notification);
}
```

#### 6. Protect Against MFA Bypass

Implement safeguards to prevent attackers from bypassing MFA:

* Rate limit authentication attempts
* Implement account lockout after multiple failed MFA attempts
* Verify MFA state in all authenticated endpoints
* Avoid "remember this device" options for highly sensitive applications

```go
// Example: Go function to check MFA bypass attempts
func detectPotentialMFABypass(userID string, request *http.Request) bool {
    // Check if user has MFA enabled but request is missing MFA token
    user := getUserByID(userID)
    if user.MFAEnabled && !request.Header.Get("X-MFA-Verified") {
        logSecurityEvent("potential_mfa_bypass_attempt", userID, request)
        return true
    }
    
    // Check for multiple failed MFA attempts
    attempts := getRecentFailedMFAAttempts(userID, 30) // Last 30 minutes
    if len(attempts) >= 5 {
        lockAccount(userID, "Too many failed MFA attempts")
        notifyUser(userID, "account_locked", request)
        return true
    }
    
    return false
}
```

#### 7. Test and Audit Your MFA Implementation

* Regularly test MFA flows for security vulnerabilities
* Conduct penetration testing specifically targeting authentication
* Log and monitor MFA-related events
* Review MFA provider security practices and certifications

### MFA Implementation Checklist

- [ ] Use at least two factors from different categories
- [ ] Implement FIDO2/WebAuthn where possible
- [ ] Enforce MFA on all authentication points and sensitive actions
- [ ] Implement risk-based adaptive authentication
- [ ] Create secure recovery mechanisms
- [ ] Notify users of important MFA events
- [ ] Rate limit and monitor for bypass attempts
- [ ] Regularly test and audit your MFA implementation

By following these best practices, you'll create a robust MFA system that balances security and usability while protecting your users from account compromise.
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