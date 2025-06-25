```yaml
---
trigger: glob
globs: [js, ts, java, py, rb, go, cs, cpp, c, swift, kt, m]
---

# OWASP Cryptographic Storage Best Practices

# Avoid reversible encryption for passwords:
#   - Use strong, dedicated password hashing (e.g., bcrypt, Argon2, scrypt).
#   - Never store passwords encrypted with reversible methods.

# Start with threat modeling to identify data adversaries and protection needs.
# Leverage dedicated key management systems (KMS, Vaults, HSMs) when available.

# Choose strong, vetted algorithms:
#   - Symmetric: AES (128-bit minimum, prefer 256-bit).
#   - Asymmetric: ECC (Curve25519 recommended) or RSA (≥2048 bits).
#   - Avoid custom or obscure crypto algorithms.

# Use authenticated encryption modes:
#   - Prefer AES-GCM or AES-CCM.
#   - If unavailable, use CTR or CBC with Encrypt-then-MAC.
#   - Avoid ECB mode except in very specific cases.

# Use cryptographically secure PRNGs for all keys, IVs, tokens, and nonces.
# Do NOT use non-secure random functions (e.g., rand(), Math.random()).
# Consult your language's crypto library for secure randomness.

# Do NOT trust encrypted data in URLs or client-side storage.
# Implement defense-in-depth: access controls, monitoring, secure defaults.

# Implement a robust key lifecycle:
#   - Generate keys securely using CSPRNG.
#   - Protect keys in secure storage (avoid hardcoding or source control).
#   - Rotate keys proactively based on policy, compromise suspicion, or volume thresholds.
#   - Support key versioning and data re-encryption strategies.

# Secure key storage guidelines:
#   - Use OS/framework/cloud secure vaults or HSMs.
#   - Restrict permissions on config files containing keys.
#   - Avoid environment variables for sensitive keys when possible.
#   - Store keys separate from encrypted data; use envelope encryption with KEKs and DEKs.
#   - Use key derivation functions (KDFs) for passphrase-based keys.

# Minimize storage of sensitive data overall, especially highly targeted info (e.g., credit cards).
```
