---
trigger: glob
globs: [js, ts, java, py, rb, go, php, cs]
---

Ensure passwords are stored securely using modern, slow, one-way hashing algorithms
with proper salting and optional peppering, balancing security and performance. This
rule helps prevent common pitfalls and keeps your users' credentials safe.

Follow OWASP Password Storage Cheat Sheet recommendations:
  - Use Argon2id (preferred) with memory≥19MiB, iterations≥2, parallelism=1;
    if unavailable, use scrypt (N≥2^17,r=8,p=1), else bcrypt (work factor≥10);
    for FIPS compliance, PBKDF2-HMAC-SHA256 with ≥600,000 iterations.
  - Do NOT encrypt passwords or use reversible transforms; always hash.
  - Rely on library-managed unique salts; avoid manual salt implementation.
  - Consider a secret pepper stored externally, applied after hashing (e.g., HMAC).
  - Tune hash work factors for <1 second verification time; increase over time.
  - When migrating legacy hashes, upgrade on login and store algo+params (PHC format).
  - Avoid unsafe bcrypt pre-hashing; if needed, use keyed HMAC + encoding + pepper.
  - Accept full Unicode and null bytes in passwords without truncation or entropy loss.

- Review password hashing implementation and ensure:
  - Usage of modern, recommended algorithms with secure parameters.
  - Salts are automatically handled, no manual salt reuse.
  - Pepper secret is stored and rotated outside the DB and applied properly.
  - Legacy hashes are migrated on authentication.
  - Input accepts full Unicode and null bytes.
  - Hashing balance performance needs; benchmark and tune regularly.
examples:
  - correct: |
      import argon2
      ph = argon2.PasswordHasher(
          time_cost=2,
          memory_cost=19200,  # 19 MiB
          parallelism=1
      )
      hashed = ph.hash(user_password)
  - incorrect: |
      encrypted_pw = encrypt(user_password)  # reversible encryption
  - incorrect: |
      bcrypt_hash = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt(rounds=5))  # work factor too low