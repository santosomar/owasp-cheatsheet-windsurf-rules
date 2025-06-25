---
trigger: glob
globs: .html, .htm, .js, .jsp, .php, .asp, .aspx, .css
---

## Protecting Your Web Application Against Clickjacking

As a software engineer, you need to understand that clickjacking (UI redress attacks) can trick your users into performing unintended actions by hiding or disguising interactive elements. These attacks embed your site in an invisible iframe, allowing attackers to capture clicks meant for their site and redirect them to your application.

### Defense Strategy: Multiple Layers of Protection

#### 1. HTTP Headers: Your First Line of Defense

**Content Security Policy (CSP)** is the modern, recommended approach:

```http
Content-Security-Policy: frame-ancestors 'none';
```

This directive prevents any site from framing your content. If you need to allow specific sites to frame your content, use:

```http
Content-Security-Policy: frame-ancestors 'self' https://trusted-site.com;
```

For older browsers that don't support CSP, implement the **X-Frame-Options** header as a fallback:

```http
X-Frame-Options: DENY
```

or

```http
X-Frame-Options: SAMEORIGIN
```

**Important:** Never use `X-Frame-Options: ALLOW-FROM` as it's obsolete and not supported by modern browsers.

#### 2. Cookie Protection

Protect your session cookies from being included in cross-origin requests:

```http
Set-Cookie: sessionid=abc123; SameSite=Lax; Secure; HttpOnly
```

Options for the SameSite attribute:
- `Strict`: Cookies are only sent in first-party context (most secure)
- `Lax`: Cookies are sent when navigating to your site from another site (good balance)

#### 3. JavaScript Frame-Buster

For legacy browsers or as an additional layer, implement this defensive code in your page's `<head>` section:

```html
<style id="antiClickjack">body{display:none !important;}</style>
<script>
  if (self === top) {
    // Not framed, remove the style that hides content
    document.getElementById("antiClickjack").remove();
  } else {
    // Framed, break out of the frame
    top.location = self.location;
  }
</script>
```

This approach first hides the page content, then only reveals it if the page is not framed. If framed, it attempts to break out of the frame.

#### 4. Special Cases: When Your Site Must Be Framed

If your application legitimately needs to be framed (e.g., it's designed to be embedded):

1. Use CSP to whitelist only specific domains:
   ```http
   Content-Security-Policy: frame-ancestors 'self' https://trusted-partner.com;
   ```

2. Implement additional confirmation for sensitive actions:
   ```javascript
   if (sensitiveAction && window !== window.top) {
     if (!window.confirm('Confirm this action?')) {
       return false; // Cancel the action if not confirmed
     }
   }
   ```

### Implementation Best Practices

1. **Apply Globally:** Add these protections to all pages, not just sensitive ones.
2. **Test Thoroughly:** Verify your defenses work across different browsers and with proxies.
3. **Defense in Depth:** Combine all three protection methods for maximum security.
4. **Verify Implementation:** Use tools like the OWASP ZAP scanner to confirm your headers are properly set.

By implementing these defenses, you significantly reduce the risk of clickjacking attacks against your web application.
