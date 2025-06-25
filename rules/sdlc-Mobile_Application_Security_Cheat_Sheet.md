---
trigger: glob
globs: [java, kt, swift, m, plist, xml, gradle]
---



  Follow mobile security best practices to protect your app and users:
  - Design with least privilege and defense in depth; embed security from the start.
  - Use standard secure authentication protocols (OAuth2, JWT) and perform all auth checks on the server.
  - Store sensitive data encrypted using platform APIs (Keychain, Keystore, Secure Enclave); avoid custom encryption and insecure storage (e.g., SharedPreferences without encryption).
  - Limit app permissions and backend privileges strictly to what is necessary.
  - Use biometric authentication with secure fallbacks and manage sessions securely (timeouts, remote logout).
  - Avoid logging sensitive info or caching data insecurely.
  - Always use HTTPS with valid certs and enable certificate pinning where possible.
  - Implement runtime integrity checks against tampering, debugging, hooking, or rooting/jailbreaking.
  - Keep dependencies updated and disable debugging in production builds; obfuscate binaries (e.g., ProGuard for Android).
  - For iOS, secure Info.plist permissions, avoid storing sensitive data in plist files, use App Attest & DeviceCheck APIs.
  - For Android, disable backups to prevent data leaks and use Play Integrity API.
  - Conduct automated and manual security testing regularly and monitor your app post-release.
  - Prepare incident response and enforce timely app updates, including forced updates if needed.


confidence: high
tags: [mobile-security, authentication, encryption, network-security, code-integrity, platform-specific]

patterns:
  - pattern-either:
      - pattern: |
          // Insecure storage of sensitive data (e.g. SharedPreferences without encryption)
          SharedPreferences.putString($KEY, $VALUE)
      - pattern: |
          // Hardcoded secrets or tokens in source code
          val $VAR = "$SECRET"
      - pattern-not-inside: |
          // Use of platform secure storage APIs e.g. Keychain or Keystore
          Keychain.get($KEY)
      - pattern: |
          // Unsafe SSL/TLS configuration (allowing all certificates, bypassing checks)
          SSLSocketFactory.allowAllHostnames()
      - pattern: |
          // Debugging enabled or log statements printing sensitive info
          Log.d(..., ...)
      - pattern-not: |
          // Enabled strictly in debug builds only
          if (BuildConfig.DEBUG) { ... }
      - pattern: |
          // Missing server-side authentication/authorization check placeholders
          if (clientAuthOnly()) { ... }
      - pattern: |
          // Disabling app backups on Android manifest (should be true)
          android:allowBackup="true"
      - pattern: |
          // No code to detect rooting/jailbreak, debugging or tampering in runtime
          noRootCheckDetected();
          noDebugDetect();
...
```