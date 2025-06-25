---
trigger: glob
globs: .js, .jsx, .ts, .tsx, .html
---

## Preventing DOM Clobbering Attacks

As a software engineer working with web applications, you should be aware of DOM Clobbering - a subtle but dangerous attack vector where malicious HTML can override JavaScript variables and functions through conflicting HTML element IDs and names.

### What is DOM Clobbering?

DOM Clobbering occurs when an attacker injects HTML with specific `id` or `name` attributes that override or "clobber" JavaScript variables or properties you expect to use. This happens because named HTML elements automatically become properties of the global `window` object and the `document` object.

**Example of a vulnerability:**

```javascript
// Your JavaScript code
if (!window.config) {
  window.config = { isAdmin: false };
}
```

An attacker could inject:
```html
<a id="config" name="config" href="#"><a id="config" name="isAdmin">true</a></a>
```

Now `window.config.isAdmin` evaluates to `true` instead of `false`!

### Best Practices to Prevent DOM Clobbering

#### 1. Sanitize User-Controlled HTML

Always sanitize HTML from untrusted sources using a robust library like DOMPurify with special configuration for DOM Clobbering protection:

```javascript
// Enable protection against DOM Clobbering
import DOMPurify from 'dompurify';

// Enable SANITIZE_NAMED_PROPS to prevent clobbering via id/name attributes
DOMPurify.setConfig({ SANITIZE_NAMED_PROPS: true });

const sanitizedHtml = DOMPurify.sanitize(userProvidedHtml);
document.getElementById('content').innerHTML = sanitizedHtml;
```

#### 2. Use Proper Variable Declarations

Always explicitly declare your variables and avoid implicit globals:

```javascript
// GOOD: Use explicit declarations
"use strict"; // Enable strict mode
const config = { isAdmin: false };

// BAD: Implicit global - vulnerable to clobbering
config = { isAdmin: false }; // Without var/let/const
```

#### 3. Avoid Storing Critical Data on Global Objects

Don't store important state or configuration directly on `window` or `document`:

```javascript
// AVOID this pattern
window.userIsAdmin = checkAdminStatus();

// BETTER: Use a module or closure
const userState = (function() {
  let isAdmin = checkAdminStatus();
  return {
    getAdminStatus: () => isAdmin
  };
})();
```

#### 4. Type Checking Before Using DOM References

Verify that objects are what you expect them to be before using them:

```javascript
// Get a reference that might be clobbered
const config = window.config;

// Check if it's the expected type before using
if (config && typeof config === 'object' && !(config instanceof Element)) {
  // Safe to use config
  if (config.isAdmin) {
    // Grant admin privileges
  }
}
```

#### 5. Use Object.freeze() for Critical Objects

Freeze important objects to prevent modification:

```javascript
const settings = Object.freeze({
  apiKey: "YOUR_API_KEY",
  maxRetries: 3,
  timeout: 5000
});
```

#### 6. Implement Content Security Policy (CSP)

Add an additional layer of protection with CSP:

```html
<!-- In your HTTP headers or meta tag -->
<meta http-equiv="Content-Security-Policy" content="script-src 'self'">
```

#### 7. Use Modern JavaScript Features

Leverage ES modules and strict mode to reduce global namespace pollution:

```javascript
// In a module file (e.g., config.js)
export const config = {
  isAdmin: false,
  theme: 'light'
};

// In your main file
import { config } from './config.js';
```

#### 8. Avoid Risky DOM APIs

Be cautious with DOM APIs that can introduce clobbering risks:

```javascript
// AVOID when possible with user input
document.write(userProvidedContent);
element.innerHTML = userProvidedContent;

// PREFER safer alternatives
element.textContent = userProvidedContent;
```

By implementing these practices, you'll significantly reduce the risk of DOM Clobbering attacks in your web applications.