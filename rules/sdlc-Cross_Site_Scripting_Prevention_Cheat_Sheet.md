```yaml
---
trigger: glob
globs: [.js, .jsx, .ts, .tsx, .html, .vue, .jsx, .css]
---

rule: |
  **Prevent Cross-Site Scripting (XSS) Vulnerabilities: Best Practices**

  1. **Treat all inputs as untrusted:** Always validate and sanitize user input early, and apply context-appropriate encoding right before output/render.

  2. **Use framework protections carefully:** Rely on your modern web framework's automatic escaping features, but avoid or strictly sanitize any use of escape hatches like React's `dangerouslySetInnerHTML`.

  3. **Apply proper encoding by context:**
     - HTML body: use HTML entity encoding.
     - HTML attributes: HTML attribute encoding with quoted values; never inject into event handlers or JavaScript attributes.
     - JavaScript strings: encode using JavaScript Unicode escapes (`\uXXXX`).
     - CSS property values: use CSS hex encoding; avoid injecting into selectors.
     - URLs: URL-encode parameters, plus HTML-attribute encode within attributes like href.

  4. **Avoid unsafe sinks:** Prefer safe APIs like `.textContent` or `.setAttribute` over `innerHTML` and similar DOM injection points.

  5. **Sanitize user-generated HTML:** When accepting HTML input (e.g., from WYSIWYG editors), use strong, up-to-date sanitizers such as DOMPurify.

  6. **Do not rely solely on CSP or centralized filters:** CSP is defense-in-depth only and filters lack context awareness, so always handle encoding/sanitization correctly in code.

  7. **Assume data may be tainted regardless of source:** Never trust internal or legacy data without validation and encoding.

  8. **Keep dependencies updated:** Regularly update your frameworks and sanitization libraries to benefit from latest XSS mitigations.

  Following these core measures ensures robust protection against XSS attacks and secures your web applications effectively.
```