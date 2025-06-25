---
trigger: glob
globs: [cs, config, cshtml, json, xml]
---


message: Follow OWASP .NET Security Cheat Sheet best practices to build secure .NET applications.
languages: [csharp, json, xml]
 high
tags: [security, dotnet, best-practices, authentication, cryptography, injection, csrf, configuration]


  This rule highlights critical security best practices for .NET developers based on OWASP's DotNet Security Cheat Sheet. Adhering to these guidelines helps prevent common vulnerabilities and ensures robust protection for your applications.

recommendation: |
  1. **Keep Frameworks & Dependencies Updated:**  
     - Regularly update .NET Framework, .NET Core, ASP.NET Core, and all NuGet packages.  
     - Integrate Software Composition Analysis (SCA) in your CI/CD pipelines to detect vulnerable libs.

  2. **Authentication & Session Security:**  
     - Use built-in authentication/session management; avoid rolling your own.  
     - Set cookies with `HttpOnly` and `Secure` flags; enforce HTTPS.  
     - Implement strong password policies and account lockout with ASP.NET Core Identity.  
     - Throttle and monitor login-related functionalities and handle errors generically to prevent username enumeration.

  3. **Access Control:**  
     - Use `[Authorize]` attributes at controller/method levels.  
     - Always validate user permissions server-side before providing resource access or edits.  
     - Prevent IDOR by validating references carefully.

  4. **Cryptography:**  
     - Never develop your own crypto primitives; use .NET vetted libraries.  
     - Prefer AES-GCM for symmetric encryption and PBKDF2 with salt for password hashing.  
     - Securely store keys; enforce TLS 1.2+ for all communications.  
     - Apply relevant security headers (HSTS, X-Frame-Options, CSP).  
     - Use Windows DPAPI for local sensitive data encryption.

  5. **Injection Prevention:**  
     - Use parameterized queries or ORMs exclusively; never concatenate SQL commands.  
     - Whitelist and validate all inputs rigorously.  
     - For OS commands or LDAP, validate and whitelist inputs carefully.

  6. **Cross-Site Request Forgery (CSRF):**  
     - Always use anti-forgery tokens (`@Html.AntiForgeryToken()`, `[ValidateAntiForgeryToken]`, or tag helpers).  
     - Remove anti-forgery cookies on logout; attach tokens to AJAX calls.

  7. **Secure Configuration:**  
     - Disable debug/tracing in production.  
     - Force HTTPS redirects and remove default server/version headers.  
     - Encrypt sensitive configuration sections and avoid default credentials.

  8. **Logging & Monitoring:**  
     - Log authentication attempts with user context but exclude sensitive data (passwords).  
     - Use centralized frameworks like ILogger, and implement active monitoring with alerts.

  9. **Serialization & Data Integrity:**  
     - Avoid insecure serializers like `BinaryFormatter`; prefer `System.Text.Json` or `XmlSerializer`.  
     - Validate digital signatures and avoid accepting untrusted serialized data.

  10. **Server-Side Request Forgery (SSRF):**  
      - Sanitize and validate all URLs/domains for outbound requests.  
      - Use allowlists, disable auto-follow of HTTP redirects, and validate IP addresses/hostnames strictly.

  **General Advice:**  
  - Always validate input with allowlists and encode output based on context.  
  - Thoroughly test and fuzz web services, especially WCF, using tools like OWASP ZAP.  
  - Harden Web Forms by enabling HTTPS, using ViewStateUserKey, and applying security headers at IIS/web.config.

---

# Note: Ensure this rule is integrated with static analyzers and CI pipelines to help detect misconfigurations and common insecure code patterns early.
```