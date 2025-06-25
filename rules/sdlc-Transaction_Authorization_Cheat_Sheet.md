---
trigger: glob
globs: [js, ts, java, py, rb, go, cs, php]
---

rule: TransactionAuthorizationBestPractices

  Ensure robust transaction authorization by implementing user-consent validation,
  server-side enforcement, unique per-transaction credentials, and protection against
  tampering, downgrade attacks, and brute force.

patterns:
  - pattern: |
      // Any code that processes transaction authorization

  - pattern-not: |
      // user confirms transaction details explicitly (amount, recipient)
  - pattern-not: |
      // authorization tokens are verified server-side without client trust
  - pattern-not: |
      // distinct auth methods and workflows separated from login/authentication
  - pattern-not: |
      // per-transaction unique, time-limited authorization tokens/codes
  - pattern-not: |
      // authorization method changes require re-validation using existing tokens
  - pattern-not: |
      // brute force protections (throttling, retry limits) on authorization attempts
  - pattern-not: |
      // server-side transaction state transition enforcement
  - pattern-not: |
      // secure cryptographic protections and secure key management in place

fix: |
  # Follow these actionable best practices when implementing transaction authorization:

  1. Enforce explicit, user-visible confirmation of all significant transaction details (amount, target) in a "What You See Is What You Sign" manner before authorization.

  2. Strictly separate user authentication from transaction authorization flows; ensure users understand exactly what they are authorizing.

  3. Use fresh, unique, and short-lived authorization tokens or codes per transaction. Avoid reuse to prevent replay attacks.

  4. Perform all authorization checks, token generation, state management, and validation server-side. Never trust the client for enforcing authorization.

  5. Protect changes to authorization tokens or methods by verifying them through existing, authenticated channels and re-authorizing as needed.

  6. Prevent downgrade or switching of authorization methods via client-side tampering; enforce selected methods and policies only on server.

  7. Implement brute-force attack mitigations such as throttling, retry limits, or transaction resets after failed attempts.

  8. Enforce correct transaction state progression, disallow skipping steps or modifying transactions after authorization.

  9. Protect transaction data in transit with strong encryption (e.g., TLS).

  10. Use strong cryptographic signing, encryption, and secure key storage (e.g., TEE, TPM, smart cards) to ensure integrity and non-repudiation.

  11. Educate users to verify transaction details from trusted sources and inform them about risks of different authorization mechanisms.

  12. Monitor, log, and investigate suspicious transaction or authorization activities to detect and respond to attacks promptly.

  Implementing these principles fortifies your transaction authorization against malware, social engineering, replay, MITM, and other common threats.
```