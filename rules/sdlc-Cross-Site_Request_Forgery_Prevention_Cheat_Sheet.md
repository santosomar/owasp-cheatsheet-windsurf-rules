```yaml
---
trigger: glob
globs: [js,ts,jsx,tsx,html,java,cs,php,py,rb,go]
---
id: csrf-protection-best-practices
message: "CSRF Protection: Follow secure patterns to prevent Cross-Site Request Forgery attacks."
languages: [javascript,typescript,java,csharp,php,python,ruby,go,html]
severity: warning
---

# CSRF Protection - Essential Developer Guidance

1. **Fix XSS First:**  
   Ensure all Cross-Site Scripting vulnerabilities are resolved before or alongside CSRF mitigation, as XSS can bypass CSRF defenses.

2. **Use Built-in Framework Protections:**  
   Prefer framework-native CSRF protection (e.g., ASP.NET AntiForgery, Spring Security CSRF, Angular HttpClient XSRF) and configure it correctly.

3. **Synchronizer Token Pattern:**  
   - Generate unpredictable, per-session/request CSRF tokens using cryptographically secure methods.  
   - Embed tokens in HTML forms or frontend meta-tags / JS variables, never in URLs or cookies.  
   - On every state-changing request (POST, PUT, DELETE, PATCH), validate tokens server-side.

4. **Avoid Token Transport in Cookies or URLs:**  
   - Don’t put CSRF tokens in URLs (avoid exposure in logs).  
   - Don’t rely on naive double-submit cookie patterns; only use the signed double-submit cookie variant with HMAC tied to session and secret keys.

5. **Protect State-Changing Requests:**  
   - Never use GET for operations changing server state.  
   - For AJAX/API calls, require and validate a custom header such as `X-CSRF-Token`. Rely on browser enforcing the same-origin policy for these headers.

6. **Harden Session Cookies:**  
   - Set `SameSite=Lax` or `SameSite=Strict` on session cookies to reduce CSRF risk.  
   - Use `Secure` and `HttpOnly` flags appropriately.  
   - Apply `__Host-` prefix on cookies when possible to prevent subdomain cookie injection.

7. **Validate Origin and Referer Headers:**  
   - Server-side check that requests’ `Origin` or `Referer` headers match trusted domains, block or log anomalies.  
   - Be mindful some legitimate requests may lack these headers; use a risk-based approach.

8. **Client-Side Code Hygiene:**  
   - Store CSRF tokens outside cookies/localStorage (e.g., `<meta>` tags or JS variables).  
   - Automatically add CSRF tokens as a custom header on unsafe HTTP methods.  
   - Prevent attacker input from crafting unauthorized AJAX requests by strict validation and whitelisting of parameters and endpoints.

9. **Login CSRF Mitigation:**  
   - Use a pre-authentication session with CSRF tokens on login forms.  
   - Destroy pre-auth session upon successful login to prevent fixation.

10. **Sensitive Action Protections:**  
    - Require user interaction like re-authentication or one-time tokens on high-risk operations (money transfers, password changes).  
    - Avoid CAPTCHAs as a CSRF mitigation method.

11. **Thorough Testing:**  
    - Test against classical CSRF scenarios AND modern client-side, AJAX-based CSRF.  
    - Validate behavior on legacy browsers and in edge cases.

---

**Following these guidelines will ensure comprehensive protection against CSRF attacks, safeguarding user sessions and application integrity.**
```