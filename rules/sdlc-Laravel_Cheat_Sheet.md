---
trigger: glob
globs: [php, blade.php, env]
---


rules:
  - id: disable-debug-in-production
    message: "Disable debug mode in production by setting APP_DEBUG=false in your .env file."
    pattern: 'APP_DEBUG\s*=\s*true'
    files: ['.env']
    recommendation: "Set APP_DEBUG=false in production to prevent detailed error messages leaking sensitive data."

  - id: secure-app-key
    message: "Ensure the application key is generated and secured using 'php artisan key:generate'."
    check: "Verify 'APP_KEY' is set and not empty in .env."

  - id: enforce-secure-permissions
    message: "Use strict file (664) and directory (775) permissions to reduce unauthorized access."
    recommendation: "Review and set appropriate file/directory permissions on your Laravel project."

  - id: encrypt-cookies-enable
    message: "Enable EncryptCookies middleware to protect cookie and session data."
    check: "Verify EncryptCookies is registered in app/Http/Kernel.php middleware."

  - id: set-secure-cookie-flags
    message: "Configure session cookies with HttpOnly, Secure, and SameSite attributes appropriately."
    check: |
      - SESSION_SECURE_COOKIE=true if using HTTPS
      - SESSION_HTTP_ONLY=true
      - SESSION_SAME_SITE=lax or strict
    recommendation: "Update config/session.php and .env accordingly to harden cookie security."

  - id: session-lifetime-configuration
    message: "Set session 'lifetime' to an appropriate timeout (e.g., 15-30 mins for low risk apps)."
    check: "Review 'lifetime' value in config/session.php."

  - id: prefer-official-authentication
    message: "Use Laravel official auth starter kits (Breeze, Fortify, Jetstream) instead of custom authentication."
    recommendation: "Leverage tested authentication flows to minimize vulnerabilities."

  - id: mass-assignment-protection
    message: "Avoid using `$request->all()` for model updates; whitelist input using `$request->only()` or validated data."
    recommendation: "Do not disable mass assignment protection via $guarded = [] or unguard(). Avoid forceFill()/forceCreate() without validated input."

  - id: prevent-sql-injection
    message: "Use Eloquent ORM or query builder with parameter binding; avoid raw concatenated queries."
    recommendation: "If using raw queries, always use bindings: e.g., whereRaw('email = ?', [$email]). Validate inputs for column names and order fields."

  - id: xss-escaping
    message: "Use Blade’s escaped output {{ }} for all untrusted data; never use {!! !!} on untrusted input."
    recommendation: "Consistently escape output to prevent Cross-Site Scripting."

  - id: secure-file-uploads
    message: "Validate uploaded file types and sizes; sanitize filenames with basename() and avoid processing risky XML or ZIP files unnecessarily."
    recommendation: "Prevent remote code execution and directory traversal by strict validation and sanitization."

  - id: prevent-open-redirect
    message: "Avoid redirecting to URLs from untrusted user input; whitelist allowed redirect destinations."
    recommendation: "Validate or whitelist redirect URLs to prevent phishing attacks."

  - id: csrf-protection
    message: "Ensure VerifyCsrfToken middleware is enabled and add @csrf in forms."
    recommendation: "Set X-CSRF-Token header for AJAX requests. Only exclude CSRF protection for stateless routes."

  - id: command-injection-prevention
    message: "Never pass unescaped user input to shell commands; use escapeshellcmd() or escapeshellarg(). Avoid eval(), unserialize(), extract() on untrusted input."
    recommendation: "Use safe APIs and avoid dangerous PHP functions."

  - id: security-headers
    message: "Configure security headers: X-Frame-Options, X-Content-Type-Options, Strict-Transport-Security, Content-Security-Policy."
    recommendation: "Set headers in middleware or web server config to harden app security."

  - id: use-security-tools
    message: "Regularly scan for vulnerabilities using tools like Enlightn Security Checker and dependency security scanners."
    recommendation: "Integrate static and dynamic analysis tools in your development workflow."

