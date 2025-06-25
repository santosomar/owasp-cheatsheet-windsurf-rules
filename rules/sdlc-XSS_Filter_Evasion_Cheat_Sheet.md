```yaml
---
trigger: glob
globs: [.js, .jsx, .ts, .tsx, .html, .htm, .vue, .php, .jsp, .asp, .aspx]
---

id: xss-filter-evasion-prevention
message: |
  Beware that input filtering alone cannot prevent XSS due to diverse obfuscation and encoding techniques.
  Follow these best practices to mitigate XSS risks:

  - Do NOT rely solely on input filtering or blacklists; attackers evade filters using mixed encodings, whitespace, malformed tags, and obfuscated payloads.
  - Always perform **context-aware output encoding**:
    • HTML escape data inside HTML body and attributes.
    • JavaScript escape data inserted into script contexts.
    • URL encode data used within URLs or URL attributes.
    • CSS escape data in style contexts.
  - Avoid allowing or rendering:
    • Inline scripts (`<script>`)
    • Inline event handlers (`onload`, `onclick`, `onerror`, etc.)
    • `javascript:` or unsafe `data:` URLs
  - Use well-established, up-to-date sanitization libraries (e.g., DOMPurify, OWASP Java Encoder) instead of custom regex filters.
  - Validate and strictly type inputs by length and format before processing.
  - Sanitize and encode all untrusted inputs at the point of output, including HTTP parameters.
  - Employ defense-in-depth: combine input validation, output encoding, Content Security Policy headers, and secure cookie flags (HttpOnly, Secure).
  - Test outputs in multiple browsers to catch browser-specific render quirks that could be exploited.
  - Avoid unsafe JavaScript APIs like `eval()`, `document.write()`, or inserting untrusted input directly into scripts or styles.
  - Recognize event handler attributes and obscure HTML elements as potential XSS vectors; do not whitelist blindly.
  - Do not rely on Web Application Firewalls (WAFs) as the sole protection layer.
  
level: warning
languages: [javascript, html, php, asp, aspx, jsp, vue]
patterns:
  - pattern: |
      /<\s*script\b[^>]*>.*?<\/\s*script\s*>/is
  - pattern-either:
      - pattern: /\bon\w+\s*=/i # event handlers like onclick=
      - pattern: /\bjavascript\s*:/i
      - pattern: /\bdata\s*:/i
  - pattern: | # usage of unsafe JS APIs with untrusted input placeholder (heuristic)
      /\b(eval|document\.write|setTimeout|setInterval)\s*\((.+)\)/
  - pattern-not-inside:
      - pattern: /DOMPurify/i
  - pattern: | # direct insertion of URL parameters into script or HTML without encoding (heuristic)
      /[?&]\w+=.*(\w+).*/   # flagged for manual review - cannot detect fully automatically

description: |
  This rule warns that simplistic input filtering cannot prevent XSS attacks due to sophisticated evasion techniques. 
  Developers must adopt a layered defense combining input validation, output encoding matched to context, use of vetted sanitizers, proper handling of dangerous tags and attributes, and thorough testing across browsers.

  Always encode outputs for the specific context they are used in (HTML, JS, CSS, URL). Avoid inline scripts and event handlers unless absolutely necessary and sanitized. Implement CSP and secure cookie flags as additional barriers.

  Use trusted libraries rather than regex blacklists and never trust repeated or reflected parameters blindly. This approach is crucial given the wide variety of XSS vectors attackers exploit through obfuscation and encoding tricks.

tags: [security, xss, validation, encoding, sanitization, web]
```