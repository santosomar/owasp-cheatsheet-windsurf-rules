---
trigger: glob
globs: [js, ts, java, py, cs, go, cpp, c, rb, swift, kt]
---
Ensure strong, secure handling of cryptographic keys per OWASP guidelines.
  - Define security objectives before selecting algorithms and key types.
  - Use only approved, strong algorithms and key lengths (NIST SP 800-57 / quantum-resistant if possible).
  - Separate keys by purpose; NEVER reuse the same key for encryption, signing, or authentication.
  - Generate keys only within FIPS 140-2 validated modules or HSMs; use internal secure RNGs.
  - Store keys solely in secure vaults or cryptographic modules; encrypt keys at rest using strong KEKs.
  - Never expose plaintext keys in application memory longer than necessary; favor key splitting and frequent rotation.
  - Transmit keys only via secure channels with authenticated provisioning methods.
  - Implement encrypted, access-controlled backups and avoid escrow of signing keys unless strictly justified.
  - Log all key accesses with unique identifiers and timestamps; audit key management regularly.
  - Maintain a compromise response plan including re-keying and secure key destruction.
  - Use ephemeral keys to achieve Perfect Forward Secrecy for session encryption.
  - Control trust stores rigorously; protect root certificates and keys from unauthorized modification.
  - Rely exclusively on reputable, validated cryptographic libraries; do not implement crypto primitives yourself.

  Following these controls minimizes key compromise risks and strengthens your application’s cryptographic posture.

languages: [javascript, typescript, java, python, csharp, go, cpp, c, ruby, swift, kotlin]
tags: [security, cryptography, key-management, best-practices]
---
# OWASP Key Management Best Practices

# Developer Guidance:
1. Define your app's cryptographic goals before choosing algorithms and key types — do not default blindly.
2. Use only NIST-approved algorithms (and key sizes) or approved quantum-resistant algorithms.
3. Enforce strict separation of keys by function: never reuse keys for different purposes.
4. Generate keys exclusively inside hardware security modules (HSMs) or validated software modules.
5. Store keys only in secure vaults or encrypted with strong KEKs; never as plaintext in config or code.
6. Keep keys out of memory longer than necessary; consider key splitting and prompt rotation.
7. Always transport keys over authenticated, encrypted channels.
8. Securely back up keys with encryption and strict access controls; avoid escrow unless critical.
9. Log and audit every key access event for accountability.
10. Prepare and practice a key compromise response plan including key destruction.
11. Use ephemeral keys in cryptographic protocols to support Perfect Forward Secrecy.
12. Control and harden trust stores rigorously to prevent unauthorized changes.
13. Use only vetted cryptographic libraries; avoid custom crypto code.

Ensure your code and infrastructure follow these key management principles to protect sensitive data and maintain cryptographic integrity.
