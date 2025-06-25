```yaml
---
trigger: glob
globs: [.rb, .erb, .haml, .slim, .yml, .yaml, .js, .jsx, .ts, .tsx]
---

id: rails-secure-coding-best-practices
message: Follow critical Ruby on Rails security best practices to prevent common vulnerabilities.
severity: warning
languages: [ruby, erb, haml, slim, yaml, javascript, typescript]
categories: [security, secure-coding, rails]

description: |
  This rule highlights essential secure coding practices for Ruby on Rails applications, helping developers avoid injection attacks, XSS, CSRF, insecure session management, unsafe redirects, and more.

recommendation: |
  - Avoid using `eval`, `system`, backticks, `exec`, or similar methods with untrusted input. Always whitelist and validate inputs if such usage is necessary.
  - Use ActiveRecord parameterized queries instead of string concatenation. Sanitize LIKE queries via `ActiveRecord::Base.sanitize_sql_like`.
  - Never disable HTML escaping with `raw`, `html_safe`, or `<%==` unless absolutely safe. Prefer safe markup (e.g., Markdown) over raw HTML.
  - Enforce Content Security Policy (CSP) headers to mitigate XSS risks; validate and sanitize URLs in helpers to block javascript: schemes.
  - Use database-backed session stores instead of default cookie-based sessions for sensitive data.
  - Always enforce TLS (`config.force_ssl = true`) and use mature authentication gems like Devise, integrating strong password complexity checks.
  - Implement authorization consistently using established libraries (e.g., CanCanCan, Pundit), avoiding insecure direct object references.
  - Enable and verify CSRF protections (`protect_from_forgery`), except for explicit token-based API paths.
  - Sanitize and whitelist redirect targets; never redirect to arbitrary user input URLs.
  - Avoid using user input in render paths—restrict to fixed known templates.
  - Configure CORS strictly with trusted origins using `rack-cors`.
  - Set security headers (`X-Frame-Options`, `X-Content-Type-Options`, `X-XSS-Protection`) and enable HSTS.
  - Avoid catch-all routes that expose unintended controller actions.
  - Keep sensitive files out of source control; use environment variables or encrypted credentials.
  - Use Rails default encryption (bcrypt) and established libraries; avoid custom crypto code.
  - Regularly update dependencies; audit third-party gems for security.
  - Integrate static analysis (Brakeman), dependency scanning, and security testing tools in development pipeline.

examples:
  safe_command_execution: |
    # ✅ Use whitelisted input and never eval system commands directly
    safe_action = %w[start stop restart]
    command = params[:command]
    if safe_action.include?(command)
      system("service nginx #{command}")
    end

  safe_sql_query: |
    # ✅ Use parameterized query with sanitization for LIKE
    search_term = ActiveRecord::Base.sanitize_sql_like(params[:q])
    User.where("name LIKE ?", "%#{search_term}%")

  avoid_raw_html: |
    # ❌ Avoid raw unescaped html
    <%= raw user_input %>

    # ✅ Prefer sanitized markdown
    <%= markdown(user_input) %>

  session_store_setup: |
    # config/initializers/session_store.rb
    Rails.application.config.session_store :active_record_store, key: '_your_app_session'

  force_ssl: |
    # config/environments/production.rb
    config.force_ssl = true

  protect_from_forgery: |
    # app/controllers/application_controller.rb
    class ApplicationController < ActionController::Base
      protect_from_forgery with: :exception
    end

  safe_redirect: |
    # ✅ Validate redirect URL or restrict to internal paths
    redirect_to(params[:return_to]) if allowed_url?(params[:return_to])
    # or
    redirect_to root_path, only_path: true

  authorization_example: |
    # Using Pundit
    def show
      @post = Post.find(params[:id])
      authorize @post
    end

notes: |
  This rule summarizes key points from the OWASP Ruby on Rails Security Cheat Sheet. Adhering to these best practices significantly reduces common web application vulnerabilities in Rails.

  For comprehensive coverage, integrate static security scanners like Brakeman and automate dependency updates.

  Secure coding is a continuous process—combine these practices with regular code reviews and security testing.
```