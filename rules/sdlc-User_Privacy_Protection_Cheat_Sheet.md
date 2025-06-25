---
trigger: glob
globs: [js, ts, java, py, rb, go, swift, kt, html, css]
---


  
    Implement strong cryptography, enforce HTTPS with HSTS, enable certificate pinning,
    and provide user privacy features to protect data and anonymity.
  languages: [javascript, typescript, java, python, ruby, go, swift, kotlin, html, css]
  
  patterns:
    - pattern-either:
        - pattern: "TLS"
        - pattern: "SSL"
        - pattern: "HSTS"
        - pattern: "certificate pinning"
        - pattern: "session revoke"
        - pattern: "panic mode"
        - pattern: "Tor"
        - pattern: "I2P"
        - pattern: "third-party content block"

    Follow these best practices:
    1. Use strong, up-to-date cryptographic algorithms for data in transit and at rest; 
       securely hash passwords with established libraries.
    2. Enforce HTTPS exclusively and implement HTTP Strict Transport Security (HSTS).
    3. Implement certificate pinning to prevent man-in-the-middle attacks even if CAs are compromised.
    4. Provide hidden panic modes to protect at-risk users, allowing discreet data concealment or decoy accounts.
    5. Enable users to remotely view and invalidate active sessions to protect against compromised devices.
    6. Support anonymity networks by allowing Tor/I2P connectivity without blocking or fingerprinting users.
    7. Minimize IP address leakage by blocking third-party external content loading where feasible.
    8. Maintain transparency by informing users about privacy limitations and data handling policies.

