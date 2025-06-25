---
trigger: glob
globs: .js, .jsx, .ts, .tsx, .html
---

## Preventing DOM-Based Cross-Site Scripting (XSS)

As a software engineer building web applications, you need to be vigilant about DOM-based XSS vulnerabilities. Unlike traditional XSS, DOM-based XSS occurs entirely on the client-side when your JavaScript code takes data from an untrusted source (like URL parameters) and inserts it into the DOM in an unsafe way.

### Understanding the Risk

DOM-based XSS occurs when:

1. Your code reads data from a user-controllable source (URL parameters, localStorage, postMessage, etc.)
2. This data is inserted into a DOM sink without proper sanitization or encoding
3. The browser interprets the injected data as executable code rather than text

### High-Risk DOM Sinks

Be especially careful when using these JavaScript features with untrusted data:

* `innerHTML`, `outerHTML`, `document.write()`, `document.writeln()`
* `eval()`, `setTimeout()`, `setInterval()`, `new Function()`
* `location`, `location.href`, `window.open()`
* Event handlers like `element.onclick = userControlledValue`
* `<script>` tag injection

### Best Practices for Prevention

#### 1. Use Safe DOM Methods

Prefer safer DOM manipulation methods that treat input as text, not HTML:

```javascript
// UNSAFE: Can execute injected scripts
element.innerHTML = userInput;

// SAFE: Treats input as text only
element.textContent = userInput;
// or
element.innerText = userInput;
```

When building complex DOM structures, use the DOM API instead of HTML strings:

```javascript
// SAFE: Building elements with the DOM API
const div = document.createElement('div');
const text = document.createTextNode(userInput);
div.appendChild(text);
parentElement.appendChild(div);
```

#### 2. Context-Aware Encoding

If you must insert untrusted data into HTML contexts, use context-specific encoding:

* **HTML Context**: Encode HTML entities

  ```javascript
  function encodeHTML(str) {
    return str.replace(/[&<>"']/g, function(match) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      }[match];
    });
  }
  
  // Usage
  element.innerHTML = encodeHTML(userInput);
  ```

* **JavaScript Context**: Encode JavaScript string literals

  ```javascript
  function encodeForJS(str) {
    return str
      .replace(/\\/g, '\\\\')
      .replace(/'/g, "\\'")  
      .replace(/"/g, '\\"')
      .replace(/\n/g, '\\n')
      .replace(/\r/g, '\\r')
      .replace(/</g, '\\x3C')
      .replace(/>/g, '\\x3E');
  }
  ```

* **URL Context**: Use `encodeURIComponent()` for URL parameters

  ```javascript
  const safeUrl = `https://example.com/?q=${encodeURIComponent(userInput)}`;
  ```

#### 3. Avoid Dangerous JavaScript Functions

Never pass untrusted data to these functions:

```javascript
// DANGEROUS - Never do this
eval(userInput);
new Function(userInput);
setTimeout(userInput, 100);
```

Instead, use safer alternatives:

```javascript
// For JSON parsing, use JSON.parse instead of eval
try {
  const data = JSON.parse(userInput);
} catch (e) {
  console.error('Invalid JSON');
}

// For dynamic function execution, use closures
setTimeout(() => {
  processUserInput(userInput);
}, 100);
```

#### 4. Handle URL Parameters Safely

URL parameters are a common source of DOM XSS attacks:

```javascript
// UNSAFE: Direct use of location.hash
const hash = window.location.hash.substring(1);
document.getElementById('output').innerHTML = hash; // Vulnerable!

// SAFE: Encode and validate
const hash = window.location.hash.substring(1);
document.getElementById('output').textContent = hash;
```

#### 5. Use Modern Frameworks Correctly

Modern frameworks like React, Angular, and Vue have built-in XSS protections, but they can be bypassed if used incorrectly:

```jsx
// React - UNSAFE when using dangerouslySetInnerHTML
function UnsafeComponent({ userInput }) {
  return <div dangerouslySetInnerHTML={{ __html: userInput }} />; // Risky!
}

// React - SAFE approach
function SafeComponent({ userInput }) {
  return <div>{userInput}</div>; // Auto-escaped by React
}
```

#### 6. Implement Content Security Policy (CSP)

Add an additional layer of protection with a strong CSP:

```html
<meta http-equiv="Content-Security-Policy" content="script-src 'self'; object-src 'none'">
```

#### 7. Validate and Sanitize

When rich HTML input is required (e.g., WYSIWYG editors), use a robust sanitization library:

```javascript
import DOMPurify from 'dompurify';

// Safely render HTML from untrusted sources
const cleanHtml = DOMPurify.sanitize(userProvidedHtml);
document.getElementById('content').innerHTML = cleanHtml;
```

By applying these defensive coding practices, you can significantly reduce the risk of DOM-based XSS vulnerabilities in your web applications.
