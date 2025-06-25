```yaml
---
trigger: glob
globs: [css, scss, sass, less]
---
id: secure-css-best-practices
name: Secure CSS Practices to Prevent Information Leakage and Abuse
description: |
  CSS files can unintentionally expose application features and user roles, aiding attackers in reconnaissance or malicious actions. Follow these best practices to harden your CSS against information disclosure and abuse.
severity: medium
tags: [security, css, information-disclosure, access-control]

pattern-either:
  - pattern: |
      /* Global role-based selectors with descriptive names are risky */
      .profileSettings {}
  - pattern: |
      /* Overly descriptive class or ID names revealing features/roles */
      .addUserButton {}

message: |
  Avoid global CSS files containing selectors that reveal user roles or sensitive features.
  Instead:
  - Isolate CSS per access control level: use separate CSS files per role (e.g., Student.css, Administrator.css), and restrict access at the server level.
  - Prevent forced browsing by validating user role before serving CSS files; log unauthorized attempts.
  - Obfuscate class names using build tools (e.g., CSS Modules, JSS minify, Blazor CSS Isolation) to reduce attacker insight.
  - Prefer generic, structural, or element-based selectors over role- or feature-specific names.
  - Use CSS frameworks (Bootstrap, Tailwind) to reduce need for custom selectors.
  - Sanitize and restrict user-generated HTML content to prevent malicious CSS injection or styling abuse.

recommendation: |
  1. Separate CSS by user role and enforce access control at the resource-serving layer.
  2. Avoid descriptive selectors that reveal features or permissions.
  3. Employ CSS class name obfuscation/minification tools during build.
  4. Validate and sanitize all user-generated content that includes styles.
  5. Monitor for forced browsing or unauthorized CSS file access attempts and alert.

references:
  - https://owasp.org/www-project-cheat-sheets/cheatsheets/Securing_Cascading_Style_Sheets_Cheat_Sheet.html
  - https://cssinjs.org
  - https://github.com/css-modules/css-modules
  - https://learn.microsoft.com/en-us/aspnet/core/blazor/components/css-isolation
  - https://getbootstrap.com
  - https://tailwindcss.com
  - https://owasp.org/www-community/attacks/Clickjacking
```