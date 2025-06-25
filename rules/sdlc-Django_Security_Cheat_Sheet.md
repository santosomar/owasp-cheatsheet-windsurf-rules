```yaml
---
trigger: glob
globs: [py, html, txt, env]
---

id: django-security-best-practices
name: Django Security Best Practices
description: |
  Enforce critical Django security recommendations including dependency updates, safe configuration, strong authentication, secure keys, middleware usage, cookie settings, CSRF/XSS protection and HTTPS enforcement.
severity: high
languages: [python, html]
tags: [security, django, authentication, csrf, xss, https, secrets]

pattern: |
  # This rule scans for common Django security misconfigurations and provides best practice advice.
  # It is advisory and does not enforce code changes but highlights security-critical areas.

message: |
  {{ advice }}

# This Windsurf rule inspects settings and code for common Django security settings and usage patterns, issuing guidance where improvements are needed.

validate: |
  issues = []

  settings_lines = [line.strip() for line in lines]

  # 1. Check DEBUG is False or not set to True
  for line in settings_lines:
    if line.startswith("DEBUG") and "True" in line:
      issues.append({
        "line": lines.index(line)+1,
        "advice": "DEBUG must NEVER be True in production; set DEBUG = False before deployment."
      })
      
  # 2. Verify SECRET_KEY presence and security
  secret_key_lines = [l for l in settings_lines if l.startswith("SECRET_KEY")]
  if not secret_key_lines:
    issues.append({
      "line": 0,
      "advice": "SECRET_KEY is missing; generate a strong random key with get_random_secret_key() and store it securely."
    })
  else:
    for sk_line in secret_key_lines:
      # Check if SECRET_KEY is hardcoded insecurely (too short or simple)
      import re
      val_match = re.search(r"['\"](.{1,})['\"]", sk_line)
      if val_match:
        key = val_match.group(1)
        if len(key) < 50:
          issues.append({
            "line": lines.index(sk_line)+1,
            "advice": "SECRET_KEY should be at least 50 characters long with letters, digits, and symbols."
          })

  # 3. Check for security middleware and CSRF middleware presence
  middleware_lines = [l for l in settings_lines if l.startswith("MIDDLEWARE") or l.startswith("MIDDLEWARE_CLASSES")]
  middleware_str = " ".join(middleware_lines).lower()
  if "securitymiddleware" not in middleware_str:
    issues.append({
      "line": 0,
      "advice": "Enable 'django.middleware.security.SecurityMiddleware' in MIDDLEWARE for critical security headers."
    })
  if "csrfviewmiddleware" not in middleware_str:
    issues.append({
      "line": 0,
      "advice": "Enable 'django.middleware.csrf.CsrfViewMiddleware' to protect against CSRF attacks."
    })
  if "xframeoptionsmiddleware" not in middleware_str:
    issues.append({
      "line": 0,
      "advice": "Enable 'django.middleware.clickjacking.XFrameOptionsMiddleware' to prevent clickjacking."
    })

  # 4. Check common security settings
  def check_setting(name):
    for l in settings_lines:
      if l.startswith(name):
        value = l.split("=",1)[1].strip().lower()
        return value
    return None

  if check_setting("SECURE_CONTENT_TYPE_NOSNIFF") != "true":
    issues.append({
      "line": 0,
      "advice": "Set SECURE_CONTENT_TYPE_NOSNIFF = True to add X-Content-Type-Options: nosniff header."
    })
  if not check_setting("SECURE_HSTS_SECONDS") or int(check_setting("SECURE_HSTS_SECONDS") or "0") == 0:
    issues.append({
      "line": 0,
      "advice": "Configure SECURE_HSTS_SECONDS with a positive integer to enforce HTTPS with HSTS."
    })

  x_frame_option = check_setting("X_FRAME_OPTIONS")
  if x_frame_option not in ["'deny'", '"deny"', "'sameorigin'", '"sameorigin"']:
    issues.append({
      "line": 0,
      "advice": "Set X_FRAME_OPTIONS = 'DENY' or 'SAMEORIGIN' to prevent clickjacking."
    })

  # 5. Check cookies secure flags
  if check_setting("SESSION_COOKIE_SECURE") != "true":
    issues.append({
      "line": 0,
      "advice": "Set SESSION_COOKIE_SECURE = True to ensure cookies only sent over HTTPS."
    })
  if check_setting("CSRF_COOKIE_SECURE") != "true":
    issues.append({
      "line": 0,
      "advice": "Set CSRF_COOKIE_SECURE = True to ensure CSRF cookie only sent over HTTPS."
    })

  # 6. Check HTTPS redirect
  if check_setting("SECURE_SSL_REDIRECT") != "true":
    issues.append({
      "line": 0,
      "advice": "Enable SECURE_SSL_REDIRECT = True to redirect all HTTP to HTTPS."
    })

  # 7. Check DEBUG not exposed in templates and views
  # Not enforceable here but remind developer

  # 8. Authentication system usage hints - best effort (checking INSTALLED_APPS and decorators)
  installed_apps_line = [l for l in settings_lines if l.startswith("INSTALLED_APPS")]
  if installed_apps_line:
    installed_apps_vals = " ".join(installed_apps_line).lower()
    if "django.contrib.auth" not in installed_apps_vals:
      issues.append({
        "line": lines.index(installed_apps_line[0])+1,
        "advice": "Include 'django.contrib.auth' in INSTALLED_APPS to leverage Django's authentication system."
      })

  # Combine issues into output messages
  outputs = []
  for issue in issues:
    outputs.append(f"Line {issue['line']}: {issue['advice']}")

  advice = "\n".join(outputs) if outputs else "No immediate Django security misconfigurations detected. Ensure to follow all best practices."

  return advice
```