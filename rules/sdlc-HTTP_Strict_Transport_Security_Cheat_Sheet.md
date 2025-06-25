```yaml
---
trigger: glob
globs: [js, ts, java, py, rb, go, php, html, htm, asp, aspx]
---
rule: enforce-http-strict-transport-security
message: |
  Ensure your web application sets a proper HTTP Strict Transport Security (HSTS) header to protect users by enforcing HTTPS exclusively.

description: |
  HTTP Strict Transport Security (HSTS) is a critical security header that instructs browsers to interact with your site only over HTTPS, protecting users from man-in-the-middle attacks, protocol downgrade attacks, and invalid certificate acceptance.

best_practices:
  - Always serve your site over HTTPS and configure your web server or application to send the `Strict-Transport-Security` header.
  - Use a long `max-age` directive (e.g., 31536000 seconds = 1 year) to ensure consistent HSTS policy enforcement.
  - Include the `includeSubDomains` directive if all subdomains support HTTPS. This extends protection to all subdomains and helps prevent cookie manipulation and other attacks.
  - Consider the `preload` directive only after you have carefully tested HSTS on your domain and subdomains and understand that enrollment in the preload list is permanent until a removal process is completed.
  - Avoid partial or missing HSTS header configurations, as they leave users vulnerable to downgrade and interception attacks.
  - Review your HTTP links and redirects to ensure no content is served over unencrypted HTTP.
  - Understand that HSTS persistence can impact user privacy and plan accordingly.
  - Set the `Secure` flag on cookies to complement HSTS protections.

examples:
  correct:
    - Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
    - Strict-Transport-Security: max-age=31536000; includeSubDomains
  warning:
    - Strict-Transport-Security: max-age=31536000
    - Missing Strict-Transport-Security header entirely

references:
  - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
  - https://hstspreload.org
  - https://owasp.org/www-project-cheat-sheets/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html
  - https://tools.ietf.org/html/rfc6797
actions:
  - Verify the HSTS header is present in all HTTPS responses.
  - Ensure `max-age` is set to at least 1 year (31536000 seconds).
  - Add `includeSubDomains` if all subdomains are HTTPS.
  - Only add `preload` after full evaluation and submission to the preload list.
  - Monitor for any HTTP content or links and migrate them to HTTPS.
  - Test user experience to confirm no HTTP fallbacks are permitted.
  - Audit cookies and set the `Secure` attribute.

```
This Windsurf IDE rule helps developers identify missing or incorrect HSTS configurations early and provides concise instructions to securely implement HSTS headers in their web projects across relevant server-side and client-side technologies.