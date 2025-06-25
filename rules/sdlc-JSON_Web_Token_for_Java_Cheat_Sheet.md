```yaml
---
trigger: glob
globs: [java]
---

rule: Secure JWT Usage in Java
short: Enforce best practices for JWT handling to prevent common security risks.
security-recommendations:
  - Use a robust JWT library and always explicitly specify and verify a strong signing algorithm (e.g., HMAC256 or RSA).
    example: |
      JWTVerifier verifier = JWT.require(Algorithm.HMAC256(key)).build();
    rationale: Prevents attacks exploiting the 'none' algorithm or algorithm confusion.

  - Bind JWTs to a hardened client fingerprint stored as an HttpOnly, Secure, SameSite=Strict cookie with no persistent expiry.
    ensure:
      - The JWT claim stores only a SHA-256 hash of this fingerprint.
      - Validate on each request that the cookie fingerprint hash matches the JWT claim.
    rationale: Mitigates token sidejacking and replay on different clients without relying on IP addresses.

  - Implement a server-side token denylist (revocation list) storing SHA-256 hashes of revoked tokens with timestamps.
    practice:
      - On logout, add the token hash to the denylist.
      - Check denylist on every token validation to reject revoked tokens.
    rationale: Enables token revocation despite JWT’s stateless nature.

  - Encrypt JWT payloads after signing using authenticated encryption (e.g., AES-GCM) with a vetted crypto library like Google Tink.
    note: Maintain signature verification as the primary tampering protection.
    rationale: Prevents sensitive data exposure via JWT payload which is otherwise only base64-encoded.

  - Store JWTs client-side securely:
      - Prefer browser sessionStorage or JavaScript private variables/closures over cookies or localStorage.
      - Use Authorization Bearer header to transmit tokens.
      - If cookies are used, apply HttpOnly, Secure, SameSite flags and implement CSRF protection.
      - Enforce strong Content Security Policy (CSP) headers to mitigate XSS.
    rationale: Reduces risks of XSS and CSRF attacks targeting tokens.

  - Use strong, high-entropy secrets (≥64 random chars) for HMAC signing or prefer RSA/asymmetric keys.
    rationale: Prevents brute force or offline key recovery, ensuring token signature integrity.

  - Adopt additional hardening:
      - Keep token lifetimes short (e.g., 15 minutes).
      - Implement token rotation and absolute session timeouts.
      - Avoid storing sensitive info plaintext in JWT claims unless encrypted.
      - Validate standard claims: issuer (iss), issued at (iat), not before (nbf), expiration (exp).
    rationale: Limits token misuse window and enforces validity.

summary: |
  To secure JWT authentication in Java, always use trusted libraries with explicit algorithm validation, bind tokens to hardened client fingerprints, support revocation with denylisting, encrypt sensitive payloads, and store tokens client-side securely with strong CSP. Utilize strong signing keys and short-lived tokens with proper claim checks to minimize risks of forgery, replay, or data leakage.
```