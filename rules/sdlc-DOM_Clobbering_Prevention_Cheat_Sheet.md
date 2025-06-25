```yaml
---
trigger: glob
globs: [.js, .jsx, .ts, .tsx, .html]
---

id: prevent-dom-clobbering
message: |
  Prevent DOM Clobbering attacks by following secure coding and sanitization best practices.
severity: warning
pattern-either:
  - pattern: 'let $VAR = $VAL'
  - pattern: 'const $VAR = $VAL'
  - pattern: 'var $VAR = $VAL'
  - pattern-not: 'window.$VAR'
  - pattern-not: 'document.$VAR'
  - pattern-not: '<* id=$ID>'
  - pattern-not: '<* name=$NAME>'
  - pattern-not: 'unsafeInnerHTML = $HTML'
  - pattern-not: 'innerHTML = $HTML'
  - pattern-not: 'document.write($HTML)'

meta:
  category: security
  technology: javascript, html
  description: |
    DOM Clobbering can lead to serious security issues by overwriting or shadowing expected JavaScript variables or browser APIs through injected HTML elements with conflicting id or name attributes.

  recommendation: |
    1. Always sanitize user-controlled HTML inputs with robust libraries like DOMPurify with SANITIZE_NAMED_PROPS enabled to remove or namespace risky `id` and `name` attributes.
    2. Avoid storing important state or variables on the global `window` or `document` objects.
    3. Declare variables explicitly using `let`, `const`, or `var` to prevent implicit globals and reduce clobbering vectors.
    4. Use strict mode (`"use strict";`) in your JavaScript files to enforce safer variable declarations and catch unintentional globals.
    5. Validate types before using DOM references (e.g., verify if an object is an `instanceof Element`) to detect and avoid clobbered variables.
    6. Implement Content Security Policy (CSP) to restrict external script execution and reduce risk of injected code leveraging clobbered objects.
    7. Consider freezing critical objects using `Object.freeze()` as a partial mitigation against overwriting.
    8. Use unique naming conventions and encapsulate variables within modules or classes to reduce collision risk.
    9. Avoid relying on untested or unsupported browser features that may yield undefined globals vulnerable to clobbering.

  references:
    - "https://owasp.org/www-community/attacks/DOM_Based_DOM_Clobbering"
    - "https://github.com/cure53/DOMPurify#sanitize_named_props"

notes: |
  This rule reminds developers to treat all HTML and DOM manipulation with caution, explicitly declare variables, and harden the client environment to minimize opportunities for DOM Clobbering attacks.
```