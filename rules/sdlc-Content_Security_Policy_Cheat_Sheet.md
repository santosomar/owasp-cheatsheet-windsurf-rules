```yaml
---
trigger: glob
globs: [html, htm, js, css, json, php, jsp, aspx]
---

# OWASP Content Security Policy (CSP) Enforcement Guide

# Purpose:
# Implement CSP as a defense-in-depth layer to mitigate XSS, clickjacking, and injection attacks.
# CSP complements, but does not replace, secure coding and input validation.

# Best Practices for Developers:

- **Deliver CSP via HTTP Headers:**
  - Use `Content-Security-Policy` header on all responses for full enforcement.
  - For testing, use `Content-Security-Policy-Report-Only` to monitor policy violations without blocking.
  - Avoid obsolete headers like `X-Content-Security-Policy` or `X-WebKit-CSP`.
  - Use `<meta http-equiv="Content-Security-Policy">` only if headers cannot be configured (less effective).

- **Adopt a Strict CSP Strategy:**
  - Use nonce-based or hash-based whitelisting for inline scripts/styles rather than broad allowlists.
  - Generate unique nonces per response and assign only to trusted inline scripts.
  - Employ `strict-dynamic` with nonces or hashes to trust dynamically-added scripts without enlarging allowlists.
  - Do **not** add nonces blindly to all scripts as it risks enabling attacker-injected scripts.

- **Minimal Baseline CSP (if strict not feasible):**
  ```
  Content-Security-Policy: default-src 'self'; frame-ancestors 'self'; form-action 'self'; object-src 'none'; base-uri 'none';
  ```
  - Restricts resource loading and form submissions to the same origin.
  - Prevents framing (clickjacking) and blocks legacy plugins (`object-src 'none'`).
  - Denies base tag injection (`base-uri 'none'`).

- **Avoid Inline JavaScript and Styles:**
  - Move inline scripts, styles, and event handlers to external files or attach via JavaScript listeners.
  - This simplifies CSP enforcement and reduces attack surface.

- **Use Important Directives:**
  - `default-src`, `script-src`, `style-src`, `img-src` to restrict resource sources.
  - `frame-ancestors` to control embedding origins.
  - `form-action` to restrict form submission endpoints.
  - `object-src 'none'` to block plugin-based attacks.
  - `base-uri 'none'` to prevent base tag injection.
  - `upgrade-insecure-requests` to force HTTPS when migrating.

- **Enable Violation Reporting:**
  - Use `report-uri` or `report-to` directives to gather CSP violation reports.
  - Analyze reports to fine-tune policies and detect issues early.

- **Combine CSP with Secure Coding:**
  - Continue rigorous input validation, output encoding, and secure development processes.
  - CSP is a layer of defense, not a silver bullet for XSS or injection.

- **Regularly Review and Update:**
  - Update your CSP as your application evolves.
  - Use tools like the [Google CSP Evaluator](https://csp-evaluator.withgoogle.com/) to assess policy strength.
  - Test changes thoroughly with report-only mode before full enforcement.

By following these guidelines, you significantly reduce the risk and impact of client-side attacks such as XSS and clickjacking.
```