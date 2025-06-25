```yaml
---
trigger: glob
globs: [html, htm, js, jsp, php, asp, aspx, css]
---

rule:
  id: OWASP-Clickjacking-Defense
  message: |
    Ensure robust clickjacking protection by configuring HTTP headers, cookies, and scripts properly.
  severity: high
  languages: [html, javascript, php, asp, aspnet, css]

tests:
  - pattern-either:
      - pattern: 'Content-Security-Policy:.*frame-ancestors'
      - pattern: 'X-Frame-Options:\s*(DENY|SAMEORIGIN)'
  - pattern-not: 'X-Frame-Options:\s*ALLOW-FROM'

description: |
  Clickjacking attacks trick users into interacting with hidden or embedded pages.  
  **To protect your site:**

  1. **Set framing protection headers on every HTML response:**
     - Prefer `Content-Security-Policy` header using `frame-ancestors` directive with value `'none'` to block all framing.
     - If CSP is not supported, fallback to `X-Frame-Options` header with `DENY` (preferred) or `SAMEORIGIN`.
     - **Do NOT use** `ALLOW-FROM` as it is obsolete and unsupported by modern browsers.
  
  2. **Mark sensitive session cookies with `SameSite=Lax` or `SameSite=Strict`:**  
     This prevents cookies from being sent in cross-origin frames and mitigates authenticated clickjacking.

  3. **Implement the recommended anti-clickjacking JavaScript frame-buster snippet inside `<head>` for legacy browser support:**
      ```html
      <style id="antiClickjack">body{display:none !important;}</style>
      <script>
        if (self === top) {
          document.getElementById("antiClickjack").remove();
        } else {
          top.location = self.location;
        }
      </script>
      ```
     Avoid fragile scripts that can be bypassed, such as `if(top != self) top.location = self.location;`.

  4. **If your site must be framed, carefully whitelist trusted domains in `frame-ancestors` and enforce user confirmation (e.g. `window.confirm()`) before sensitive actions.**

  5. **Apply these protections globally on all relevant responses to ensure consistent defense.**

  Combining these layers offers the strongest protection against clickjacking attacks and helps safeguard user interactions.

recommendation: |
  - Always configure CSP `frame-ancestors 'none'` header unless framing is required.
  - Use `X-Frame-Options: DENY` as fallback; never use `ALLOW-FROM`.
  - Set session cookies with `SameSite=Lax` or `Strict`.
  - Add the approved anti-clickjacking JS snippet for legacy browser coverage.
  - Avoid simplistic JS frame busters that attackers can bypass.
  - Employ confirmation dialogs for framed sensitive operations.
  - Test headers and scripts under proxies and across browsers to ensure enforcement.
```