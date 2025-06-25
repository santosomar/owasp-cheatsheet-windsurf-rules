---
trigger: glob
globs: [php, twig, yml, yaml]
---



  Enforce critical security best practices when developing Symfony applications.



patterns:
  # 1. Cross-Site Scripting (XSS)
  - pattern-either:
      - pattern: '{{ ... }}'
      - pattern-not-inside-twig-raw: true # Pseudocode to illustrate no raw on untrusted output

  # 2. CSRF protection: check use of isCsrfTokenValid() or usage of form components (heuristic)
  - pattern-either:
      - pattern: 'isCsrfTokenValid(...)'
      - pattern-inside-class: 'Form' # heuristic to encourage use of Symfony Forms

  # 3. SQL Injection - disallow direct concatenation of user input strings in queries
  - pattern-not: '->createQuery(".*".*)' # discourages concatenation literals in DQL
  - pattern-not: '->executeQuery(".*".*)' # likewise DBAL

  # 4. Command Injection prevention
  - pattern-not: 'exec($userInput)'
  - pattern-not: 'shell_exec($userInput)'
  - pattern-not: 'system($userInput)'
  - pattern: 'use Symfony\Component\Filesystem\Filesystem' # encourages safer filesystem ops

  # 5. Open Redirection - disallow direct redirects to user inputs
  - pattern-not: 'return $this->redirect($request->query->get(...))'

  # 6. File Upload Security
  - pattern: '@Assert\File' # encourages validation constraints on uploads
  - pattern: 'move(UploadedFile...)' # ensure unique names, store outside web root

  # 7. Directory Traversal Prevention
  - pattern: 'realpath(...)'
  - pattern: 'basename(...)'

  # 8. Dependency Vulnerability
  - pattern: 'composer update'
  - pattern: 'symfony check:security'

  # 9. CORS
  - pattern: 'nelmio_cors' # configuration bundle usage
  - pattern-not: 'allow_origin: [*]' # warning against wildcard origins in prod

  # 10. Security Headers
  - pattern: 'Strict-Transport-Security'
  - pattern: 'Content-Security-Policy'
  - pattern: 'X-Frame-Options'
  - pattern: 'X-Content-Type-Options'

  # 11. Session & Cookie Security
  - pattern: 'cookie_secure: true|auto'
  - pattern: 'cookie_httponly: true'
  - pattern: 'cookie_samesite: lax|strict'
  - pattern-not: 'session.auto_start: 1'

  # 12. Authentication and Authorization
  - pattern: 'firewalls:'
  - pattern: 'access_control:'

  # 13. Error Handling
  - pattern-not: 'APP_ENV=dev'
  - pattern: 'APP_ENV=prod'

  # 14. Sensitive Data Handling
  - pattern: 'secrets:'
  - pattern-not: 'API_KEY=' # check commitments of sensitive creds

  # 15. General Best Practices
  - pattern: 'debug: false'
  - pattern: 'https://'
  - pattern: 'file permissions'

fix: |
  Follow these security best practices:

  - Use Twig's default {{ }} escaping; avoid |raw except for trusted content.
  - Use Symfony Forms for CSRF protection or manually handle tokens with `isCsrfTokenValid()`.
  - Never concatenate user data directly into queries; use parameter binding.
  - Avoid exec/system calls with user input; prefer Symfony Filesystem component.
  - Validate or whitelist redirect URLs; never redirect directly to user input.
  - Validate uploaded files with Symfony Validator; store files securely with unique names.
  - Use realpath() and basename() to sanitize file paths and prevent traversal.
  - Regularly run `composer update` and `symfony check:security`.
  - Configure CORS with nelmio/cors-bundle, avoiding wildcard origins in production.
  - Set security headers (HSTS, CSP, X-Frame-Options, etc.) in responses or web server.
  - Secure session cookies with `cookie_secure`, `cookie_httponly`, and `cookie_samesite`.
  - Configure access controls and firewalls properly; disable debug mode in production.
  - Use Symfony secrets for sensitive data; never commit secrets to version control.
  - Enforce HTTPS, set proper file permissions, and implement backups and monitoring.

  Adhering to these guidelines will significantly reduce common vulnerabilities in Symfony apps.
```