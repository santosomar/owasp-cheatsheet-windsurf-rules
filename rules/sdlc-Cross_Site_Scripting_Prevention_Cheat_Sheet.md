---
trigger: glob
globs: .js, .jsx, .ts, .tsx, .html, .vue, .css
---

## Preventing Cross-Site Scripting (XSS) Vulnerabilities

As a software engineer, preventing XSS vulnerabilities is critical for web application security. XSS attacks occur when an attacker injects malicious scripts that execute in users' browsers, potentially stealing cookies, session tokens, or other sensitive information.

### Core Defensive Strategies

#### 1. Context-Aware Output Encoding

The most important defense against XSS is proper output encoding based on the context where data will be inserted:

* **HTML Body Context:**
  ```javascript
  // Instead of this (vulnerable):
  element.innerHTML = userInput;
  
  // Do this (safe):
  element.textContent = userInput;
  // Or if using a library:
  element.innerHTML = DOMPurify.sanitize(userInput);
  ```

* **HTML Attribute Context:**
  ```html
  <!-- Always quote attributes and encode their values -->
  <div data-user="{{encodedUserInput}}">Safe</div>
  ```

* **JavaScript Context:**
  ```javascript
  // Avoid dynamically creating JavaScript from user input
  // If necessary, use JavaScript Unicode escapes
  const safeValue = userInput.replace(/[\\"']/g, char => `\u${char.charCodeAt(0).toString(16).padStart(4, '0')}`);
  const code = `const message = "${safeValue}";`;
  ```

* **CSS Context:**
  ```javascript
  // Avoid injecting user input into CSS when possible
  // If necessary, strictly validate against an allowlist
  const safeColor = /^#[0-9a-f]{6}$/i.test(userColor) ? userColor : '#default';
  element.style.backgroundColor = safeColor;
  ```

* **URL Context:**
  ```javascript
  // For URLs in attributes
  const safeUrl = encodeURIComponent(userProvidedUrl);
  // Validate URL protocol to prevent javascript: URLs
  if (!/^(javascript|data|vbscript):/i.test(userProvidedUrl)) {
    element.href = userProvidedUrl;
  }
  ```

#### 2. Leverage Framework Protections

Modern frameworks provide built-in XSS protections:

* **React:** Auto-escapes values in JSX, but be careful with `dangerouslySetInnerHTML`
* **Angular:** Uses contextual auto-escaping, but be cautious with `[innerHTML]` binding
* **Vue:** Auto-escapes mustache interpolations, but watch out for `v-html`

When using these escape hatches, always sanitize the input:

```javascript
// React example with sanitization
import DOMPurify from 'dompurify';

function SafeHtml({ content }) {
  return <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(content) }} />;
}
```

#### 3. Input Validation and Sanitization

* **Validate Early:** Apply strict input validation as close to the input source as possible.
* **Sanitize When Needed:** When rich HTML input is required (e.g., WYSIWYG editors), use a robust sanitization library:

```javascript
import DOMPurify from 'dompurify';

// Configure allowed tags and attributes
DOMPurify.setConfig({
  ALLOWED_TAGS: ['b', 'i', 'p', 'a', 'ul', 'li'],
  ALLOWED_ATTR: ['href', 'target', 'rel']
});

const cleanHtml = DOMPurify.sanitize(userHtml);
```

#### 4. Additional Layers of Defense

* **Content Security Policy (CSP):** Implement a strong CSP as a backup defense:

```http
Content-Security-Policy: default-src 'self'; script-src 'self'; object-src 'none';
```

* **Use Safe DOM APIs:** Prefer safer DOM manipulation methods:

```javascript
// Instead of innerHTML
element.textContent = userInput;

// Instead of setting attributes directly with string concatenation
element.setAttribute('data-user', userInput);
```

* **HTTP-only Cookies:** Mark sensitive cookies as HTTP-only to prevent JavaScript access.

#### 5. Common Pitfalls to Avoid

* **Don't trust any data source:** Even internal APIs or databases can contain malicious data.
* **Beware of indirect inputs:** User data can enter your application through URLs, form fields, HTTP headers, and JSON/XML payloads.
* **Don't rely on client-side sanitization alone:** Always re-validate and sanitize on the server.
* **Keep dependencies updated:** Regularly update your frameworks and libraries to benefit from security patches.

By applying these context-specific encoding strategies and defense-in-depth approaches, you can significantly reduce the risk of XSS vulnerabilities in your web applications.
