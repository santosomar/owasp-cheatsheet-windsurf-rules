---
trigger: glob
globs: .js, .ts, .jsx, .tsx, .html, .java, .cs, .php, .py, .rb, .go
---

## Preventing Cross-Site Request Forgery (CSRF) Attacks

As a software engineer, protecting your web applications from CSRF attacks is essential. These attacks trick users into making unwanted actions on a site where they're already authenticated. Here's how to implement robust CSRF defenses.

### Understanding the Threat

CSRF attacks exploit the trust a website has in a user's browser. When a user is authenticated to your site, an attacker can trick them into submitting a request to your server without their knowledge or consent.

### Implementation Best Practices

#### 1. Fix XSS Vulnerabilities First

Cross-Site Scripting (XSS) vulnerabilities can bypass CSRF protections. Always address XSS issues alongside CSRF mitigations.

#### 2. Leverage Your Framework's Built-in Protection

Modern frameworks provide robust CSRF protection. Use these native defenses whenever possible:

* **React/Next.js**: Use the built-in CSRF protection in Next.js API routes
* **Angular**: The HttpClient automatically handles CSRF tokens
* **Spring**: Enable CSRF protection with `csrf().disable(false)`
* **Django**: Use the `{% csrf_token %}` template tag
* **ASP.NET Core**: Use the `[ValidateAntiForgeryToken]` attribute

#### 3. Implement the Synchronizer Token Pattern

This is the most common and effective CSRF defense:

```javascript
// Server-side token generation (Node.js example)
const crypto = require('crypto');

function generateCsrfToken(sessionId) {
  const secret = process.env.CSRF_SECRET;
  return crypto
    .createHmac('sha256', secret)
    .update(sessionId)
    .digest('hex');
}

// Include in your HTML
app.get('/form', (req, res) => {
  const csrfToken = generateCsrfToken(req.session.id);
  res.render('form', { csrfToken });
});
```

In your HTML form:

```html
<form action="/api/action" method="POST">
  <input type="hidden" name="_csrf" value="{{csrfToken}}">
  <!-- other form fields -->
  <button type="submit">Submit</button>
</form>
```

For AJAX requests, include the token in a custom header:

```javascript
fetch('/api/action', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': document.querySelector('meta[name="csrf-token"]').content
  },
  body: JSON.stringify(data)
});
```

#### 4. Protect All State-Changing Requests

* **Never use GET for state changes**: All operations that change state should use POST, PUT, DELETE, or PATCH.
* **Validate tokens on all unsafe methods**: Verify CSRF tokens on every state-changing request.

#### 5. Harden Session Cookies

Set appropriate cookie attributes to reduce CSRF risk:

```http
Set-Cookie: sessionid=abc123; Path=/; SameSite=Lax; Secure; HttpOnly
```

* **SameSite=Lax**: Prevents cookies from being sent in cross-site requests except for top-level navigations.
* **SameSite=Strict**: More secure but can affect user experience; cookies are never sent in cross-site requests.
* **__Host- prefix**: Use `__Host-sessionid` to prevent subdomain cookie injection.

#### 6. Secondary Defenses

Implement additional layers of protection:

* **Origin/Referer Validation**: Verify that requests come from your domain:

  ```javascript
  // Server-side validation
  function validateOrigin(req) {
    const origin = req.headers.origin || req.headers.referer;
    return origin && new URL(origin).hostname === 'yourdomain.com';
  }
  ```

* **Custom Request Headers**: For AJAX requests, rely on browsers' same-origin policy for custom headers.

#### 7. Special Cases: Login CSRF

Login forms need protection too! Use a pre-session approach:

```javascript
// Generate a token before login
app.get('/login', (req, res) => {
  req.session.loginCsrfToken = crypto.randomBytes(32).toString('hex');
  res.render('login', { csrfToken: req.session.loginCsrfToken });
});

// Validate on login attempt
app.post('/login', (req, res) => {
  if (req.body.csrf !== req.session.loginCsrfToken) {
    return res.status(403).send('CSRF validation failed');
  }
  // Continue with authentication...
});
```

#### 8. Testing Your CSRF Defenses

Verify your protections with these tests:

* Create a test HTML page on a different domain that submits to your endpoints
* Verify that CSRF tokens are properly validated
* Test both traditional form submissions and AJAX requests
* Check behavior with cookies that have different SameSite settings

By implementing these defenses in layers, you'll create a robust protection against CSRF attacks while maintaining a good user experience.