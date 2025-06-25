```yaml
---
trigger: glob
globs: [json, js, jsx, ts, tsx, html, css]
---

rule: secure-browser-extension-development
name: Secure Browser Extension Development Best Practices
message: Follow these critical security best practices when building browser extensions to protect users and their data.
severity: warning
metadata:
  category: security
  technology: browser-extensions
  reference: OWASP Browser Extensions Cheat Sheet

patterns:
  - pattern-either:
      patterns:
        - pattern: '"permissions":\s*\[\s*".*"\s*\]'
        - pattern: '"optional_permissions":\s*\[\s*".*"\s*\]'
    message: |
      ⚠️ Apply principle of least privilege: Only request permissions your extension absolutely needs.
      Avoid broad or overly permissive entries like "tabs" or unrestricted URL patterns ("http://*/*").
      Regularly audit and remove unused permissions from manifest.json.

  - pattern-either:
      patterns:
        - pattern: 'http://'
        - pattern: 'new\s+WebSocket\s*\(\s*"ws://'
    message: |
      🚫 Avoid insecure network communication:
      Always use HTTPS (and wss) URLs to encrypt data in transit and prevent interception.

  - pattern-not-inside:
      language: json
      scope: string.quoted.double.json
      patterns:
        - pattern: '"storage"'
    patterns:
      - pattern: 'localStorage\.setItem'
      - pattern: 'localStorage\.getItem'
    message: |
      ⚠️ Avoid localStorage for sensitive data storage; prefer the Chrome Storage API which is more secure.
      Encrypt sensitive information before storage and never store secrets hardcoded in your source code.

  - pattern-either:
      patterns:
        - pattern-either:
            patterns:
              - pattern: 'content_security_policy\s*:\s*".*"'
              - pattern: '"content_security_policy"\s*:\s*".*"'
        - pattern: 'eval\s*\('
        - pattern: 'new Function\('
        - pattern: 'import\(.*\)'
    message: |
      🛡️ Mitigate code injection risks:
      Define a strict Content Security Policy (CSP) that disallows inline scripts and restricts sources.
      Avoid dynamic code execution via eval(), new Function(), and dynamic import().
      Do not load or execute scripts from untrusted or remote locations.

  - pattern:
      - pattern: 'innerHTML\s*='
      - pattern-not-inside: 'sanitizer|DOMPurify'
    message: |
      ✋ Sanitize all user inputs before injecting into the DOM.
      Avoid using innerHTML with untrusted data; favor safer APIs like textContent or libraries like DOMPurify.

  - pattern:
      - pattern: '"dependencies"'
    message: |
      🔄 Regularly audit and update third-party dependencies using tools like npm audit or OWASP Dependency-Check.
      Use trusted, actively maintained libraries with a history of prompt security fixes.

  - pattern:
      - pattern: 'fetch\([^)]*\)'
      - pattern-not-inside: 'manifest.json'
      - pattern-not-inside: 'chrome\.runtime\.sendMessage'
    message: |
      ⚠️ Do not fetch or execute extension updates or scripts from untrusted external servers.
      Rely solely on official signed extension updates from marketplaces.
      If loading code programmatically, implement integrity verification.

  - pattern:
      - pattern: 'document\.body|document\.querySelector'
    message: |
      🔒 Prevent DOM-based data leakage:
      Do not inject sensitive user data directly into web pages where page scripts can access it.
      Use extension-owned UI components (popups, options pages, sidebars) to display sensitive information.
      Shadow DOM alone is insufficient for isolation; use proper UI separation.

# Summary advice for developers (can be shown as a related message or documentation link)
documentation: |
  **Secure Extension Development Summary:**

  - Limit permissions strictly using the principle of least privilege.
  - Always use HTTPS for all network communications.
  - Store sensitive data securely; avoid localStorage and hardcoded secrets.
  - Enforce a strict Content Security Policy (CSP) to prevent code injection and XSS.
  - Sanitize all user input before use in the DOM; prefer safe APIs.
  - Do not fetch or execute remote code dynamically.
  - Audit and maintain third-party dependencies regularly.
  - Isolate sensitive UI components from page context to prevent data skimming.
  - Provide transparent privacy policies and obtain explicit user consent.
  
Following these guidelines protects users from privacy violations, data theft, and malicious code execution.
```
