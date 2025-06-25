---
trigger: glob
globs: .html, .htm, .js, .css, .json, .php, .jsp, .aspx
---

## Content Security Policy (CSP): A Defense-in-Depth Strategy

As a software engineer, implementing a strong Content Security Policy (CSP) is one of the most effective ways to mitigate cross-site scripting (XSS), clickjacking, and other injection attacks. CSP works by declaring which dynamic resources are allowed to load, effectively creating a whitelist that the browser enforces.

### Implementing CSP in Your Application

#### 1. Deliver CSP via HTTP Headers

The most effective way to implement CSP is through HTTP response headers:

```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted-cdn.com;
```

When testing a new policy, use the report-only mode to monitor without blocking:

```http
Content-Security-Policy-Report-Only: default-src 'self'; script-src 'self';
```

**Note:** Avoid using the meta tag approach (`<meta http-equiv="Content-Security-Policy"...>`) except when you cannot modify HTTP headers, as it provides less protection and doesn't support all directives.

#### 2. Adopt a Strict CSP Strategy

Modern CSP best practices favor nonce-based or hash-based approaches over domain whitelisting:

**Nonce-based approach:**

```http
Content-Security-Policy: script-src 'nonce-random123' 'strict-dynamic';
```

With corresponding HTML:

```html
<script nonce="random123">alert('Hello');</script>
```

**Important:** Generate a unique, cryptographically strong nonce for each page load. The nonce should be at least 128 bits of entropy encoded in base64.

**Hash-based approach:**

```http
Content-Security-Policy: script-src 'sha256-hashOfYourScriptContent' 'strict-dynamic';
```

#### 3. Minimal Baseline CSP

If you're just getting started with CSP, begin with this baseline policy:

```http
Content-Security-Policy: default-src 'self'; frame-ancestors 'self'; form-action 'self'; object-src 'none'; base-uri 'none';
```

This policy:
- Restricts resources to the same origin
- Prevents clickjacking by controlling framing
- Limits form submissions to the same origin
- Blocks plugin content (Flash, Java applets)
- Prevents base tag injection attacks

#### 4. Refactor Your Code for CSP Compatibility

To make CSP implementation easier:

1. **Move inline code to external files:**
   ```html
   <!-- Instead of this -->
   <button onclick="doSomething()">
   
   <!-- Do this -->
   <button id="myButton">
   <script src="buttons.js"></script> <!-- With event listeners -->
   ```

2. **Eliminate inline styles:**
   ```html
   <!-- Instead of this -->
   <div style="color: red">
   
   <!-- Do this -->
   <div class="red-text">
   ```

#### 5. Key CSP Directives You Should Know

- **`default-src`**: The fallback for other fetch directives
- **`script-src`**: Controls JavaScript sources
- **`style-src`**: Controls CSS sources
- **`img-src`**: Controls image sources
- **`connect-src`**: Controls fetch, XHR, WebSocket connections
- **`frame-ancestors`**: Controls which sites can embed your pages (replaces X-Frame-Options)
- **`form-action`**: Controls where forms can be submitted
- **`upgrade-insecure-requests`**: Automatically upgrades HTTP requests to HTTPS

#### 6. Enable Violation Reporting

Set up a reporting endpoint to collect CSP violations:

```http
Content-Security-Policy: default-src 'self'; report-uri https://your-domain.com/csp-reports;
```

Or use the newer `report-to` directive with the Reporting API:

```http
Content-Security-Policy: default-src 'self'; report-to csp-endpoint;
Reporting-Endpoints: csp-endpoint="https://your-domain.com/csp-reports"
```

#### 7. CSP Implementation Workflow

1. Start with report-only mode to understand your application's needs
2. Analyze the reports to identify legitimate resources
3. Gradually tighten your policy
4. Move to enforcement mode once violations are minimized
5. Continue monitoring and adjusting as your application evolves

Remember that CSP is a defense-in-depth measure. It complements, but does not replace, proper input validation, output encoding, and other secure coding practices.
