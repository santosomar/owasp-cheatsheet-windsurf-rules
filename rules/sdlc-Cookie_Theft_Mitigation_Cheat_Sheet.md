```yaml
---
trigger: glob
globs: [js,ts,jsx,tsx,java,py,rb,php]
---

id: cookie-theft-mitigation
name: Cookie Theft Detection and Mitigation Best Practices
message: |
  Protect your application from session hijacking by implementing server-side detection of stolen session cookies.
  Follow these key practices:

  1. Save critical request headers with each session establishment:
     - IP Address
     - User-Agent
     - Accept-Language
     - Date (timestamp)
     - Optionally: Accept, Accept-Encoding
     - Optionally: Sec-Fetch-* and Sec-CH-* headers when available

  2. On each request, compare the current headers against the saved values to detect significant changes that may indicate cookie theft. Use fuzzy comparison to minimize false positives (e.g., IP geolocation ranges, User-Agent variations).

  3. In case of suspicious changes:
     - Trigger secondary verification such as CAPTCHA challenges.
     - Require re-authentication for sensitive operations or confidential data access.
     - Rotate session identifiers by invalidating old sessions and issuing new ones post-verification.

  4. Prioritize checks for high-risk endpoints (e.g. user profile updates, payment processing) to balance security and performance.

  5. Stay informed about emerging standards like Device Bound Session Credentials (DBSC) to strengthen session binding on the client side once available.

  Implementing these recommendations can help detect and mitigate cookie theft attacks, reducing the risk of user session hijacking.
severity: warning
patterns:
  - pattern-either:
      - pattern-inside: |
          SessionStorage.create()
          $X$.save({
            ip: $IP$,
            user_agent: $USER_AGENT$,
            date: $DATE$,
            accept_language: $LANG$,
            ...
          })
      - pattern: |
          req.session.ip
      - pattern-regex: '(user-agent|accept-language|sec-ch-|sec-fetch-|accept-encoding)'
  - pattern-either:
      - pattern: |
          function $FN$($REQ$, $RES$) {
            if ($HEADER_CHANGE_CHECK$) {
              $VALIDATION_ACTION$
            }
          }
      - pattern-inside: |
          app.post($ENDPOINT$, $MIDDLEWARE$, $HANDLER$)
...
```