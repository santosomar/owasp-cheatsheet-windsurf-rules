---
trigger: glob
globs: [js, ts, java, py, rb, php, go, cs]
---

# 1. Avoid Open Redirectors
- Never allow URLs to redirect based on uncontrolled query parameters to prevent token theft.
- Validate and whitelist redirect URIs strictly.

# 2. Use PKCE in Authorization Code Flow
- Always implement PKCE (Proof Key for Code Exchange) for public/native clients.
- Use `S256` as the code challenge method to avoid exposing verifiers.
- Authorization servers must verify `code_verifier` when `code_challenge` is sent.

# 3. Enforce CSRF Protections
- Use PKCE’s inherent CSRF defenses or OpenID Connect’s `nonce`.
- If unavailable, bind a securely generated one-time CSRF token to the OAuth `state` parameter and validate it.

# 4. Prefer Authorization Code Grant over Implicit Grant
- Use `response_type=code` or `code id_token` to avoid exposing tokens in URLs and facilitate replay detection.

# 5. Sender-Constrain Tokens to Prevent Replay
- Implement token binding using Mutual TLS (mTLS) or Demonstration of Proof of Possession (DPoP).
- Rotate refresh tokens regularly or ensure they are sender-constrained.

# 6. Scope and Restrict Token Privileges
- Limit tokens to minimum necessary scopes.
- Restrict tokens to specific resource servers (`aud` claim).
- Enforce usage via scopes and `authorization_details` claims.

# 7. Avoid Resource Owner Password Credentials Grant
- Do not use the password grant due to credential exposure risks.

# 8. Use Strong Client Authentication
- Prefer asymmetric methods such as mTLS or `private_key_jwt`.
- Avoid weak symmetric key storage or authentication methods.

# 9. Prevent Mix-up Attacks in Multi-Authorization Server Environments
- Validate the token issuer (`iss` claim) on all tokens and authorization responses.
- Use distinct redirect URIs per authorization server if issuer validation isn't possible.

# 10. Protect Sensitive Claims and Tokens
- Clients must never control `client_id` or `sub` claims.
- Enforce end-to-end TLS; only allow unencrypted HTTP redirects for localhost loopback on native apps.
- Never send authorization responses over unsecured channels.

---

# Summary:
Ensure secure OAuth 2.0 implementations by rigorously applying PKCE, CSRF protections, and sender-bound tokens; use authorization code grants exclusively over implicit flows; limit token scopes and audiences; avoid insecure grants; enforce strong client authentication; validate issuers and redirect URIs carefully; prevent open redirectors; and always protect tokens and sensitive claims with encryption and integrity checks.
```