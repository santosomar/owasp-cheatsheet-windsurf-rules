```yaml
---
trigger: glob
globs: [.ini, .php]
---

id: php-secure-configuration
name: PHP Secure Configuration Best Practices
description: Ensure your PHP configuration follows security best practices to harden your PHP environment and reduce attack surface.
severity: warning
tags: [php, configuration, security]

pattern-either:
  - pattern: |
      expose_php\s*=\s*On
    message: 'Set expose_php = Off to prevent PHP version disclosure to attackers.'
    level: warning
  - pattern-not: |
      error_reporting\s*=\s*E_ALL
  - pattern-not: |
      display_errors\s*=\s*Off
    message: 'Set display_errors = Off on production servers to avoid leaking sensitive error details.'
  - pattern-not: |
      log_errors\s*=\s*On
  - pattern-not: |
      error_log\s*=\s*.+
    message: 'Enable log_errors = On and set error_log to a secure path to capture PHP errors for analysis.'
  - pattern: |
      allow_url_fopen\s*=\s*On
    message: 'Set allow_url_fopen = Off to prevent Remote File Inclusion (RFI) vulnerabilities.'
  - pattern: |
      allow_url_include\s*=\s*On
    message: 'Set allow_url_include = Off to prevent inclusion of remote files.'
  - pattern: |
      file_uploads\s*=\s*On
    message: 'Ensure file_uploads is enabled only if application requires file uploads; disable otherwise.'
  - pattern-not: |
      disable_functions\s*=\s*.*
    message: 'Disable dangerous PHP functions like system, exec, shell_exec, passthru, and others not used by your app.'
  - pattern-not: |
      session.use_strict_mode\s*=\s*1
    message: 'Enable session.use_strict_mode = 1 to prevent session fixation attacks.'
  - pattern-not: |
      session.cookie_secure\s*=\s*1
    message: 'Set session.cookie_secure = 1 to ensure cookies are sent only over HTTPS.'
  - pattern-not: |
      session.cookie_httponly\s*=\s*1
    message: 'Set session.cookie_httponly = 1 to prevent JavaScript access to session cookies.'
  - pattern-not: |
      session.cookie_samesite\s*=\s*(Strict|Lax)
    message: 'Set session.cookie_samesite = Strict or Lax to mitigate CSRF attacks.'
  - pattern-not: |
      session.name\s*=\s*myPHPSESSID
    message: 'Change the default session.name to a custom value to hinder session guessing.'
  - pattern: |
      enable_dl\s*=\s*On
    message: 'Set enable_dl = Off to prevent dynamic loading of PHP extensions at runtime.'
  - pattern-not: |
      memory_limit\s*=\s*\d+[MmGg]
    message: 'Set a reasonable memory_limit (e.g., 50M) to prevent resource exhaustion.'
  - pattern-not: |
      max_execution_time\s*=\s*\d+
    message: 'Set a reasonable max_execution_time (e.g., 60) to limit script runtime.'
  - pattern: |
      display_startup_errors\s*=\s*On
    message: 'Set display_startup_errors = Off on production servers to avoid leaking startup errors.'
  - pattern-not: |
      session.save_path\s*=\s*\/[^ ]+
    message: 'Set session.save_path to a secure directory accessible only by your application.'
  - pattern-not: |
      session.cookie_domain\s*=\s*[^ ]+
    message: 'Set session.cookie_domain to your actual domain to restrict cookie scope.'
  - pattern-not: |
      session.cookie_lifetime\s*=\s*\d+
    message: 'Configure session.cookie_lifetime according to your application needs (e.g., 14400 for 4 hours).'

recommendation: |
  Review and apply the recommended PHP configuration settings in your `php.ini`:
  - Keep `expose_php` OFF to hide PHP version.
  - Turn off `display_errors` and `display_startup_errors` in production.
  - Enable error logging with a secure `error_log` location.
  - Disable `allow_url_fopen` and `allow_url_include` to prevent remote file inclusion.
  - Disable all dangerous functions that your codebase doesn't need.
  - Harden session settings: use strict mode, secure and httponly cookies, set SameSite, customize session name.
  - Limit resource usage with memory_limit and max_execution_time.
  - Disable dynamic function loading (`enable_dl`).
  - Use secure paths for sessions and uploads.
  Additionally, consider deploying Snuffleupagus for advanced PHP protection.

resources:
  - https://www.php.net/manual/en/ini.core.php
  - https://paragonie.com/blog/2017/12/2018-guide-building-secure-php-software
  - https://www.acunetix.com/blog/articles/local-file-inclusion-lfi/
  - https://snuffleupagus.readthedocs.io/en/latest/
```