---
trigger: glob
globs: [java, php, cs, rb, rs, js, ts]
---



  Avoid unvalidated redirects and forwards. Do not use raw user input to determine redirect or forward URLs.
  This prevents phishing attacks and access control bypass.

patterns:
  - pattern-either:
      - pattern: response.sendRedirect(request.getParameter($PARAM))
      - pattern: header("Location: " ~ $_)
      - pattern: redirect_to $_
      - pattern: Response.Redirect($_)
      - pattern: res.redirect($_)
      - pattern: ... # Add language-appropriate patterns for redirects using user input directly

suggestions:
  - Use hard-coded or application-controlled URLs for redirects:
    - e.g. `response.sendRedirect("https://www.mysite.com/home")`
  - If user input must indicate redirect target:
    - Accept an ID or token, then map it server-side to an allow-listed URL.
    - Example:
      ```
      String id = request.getParameter("id");
      Map<String, String> allowed = Map.of("home", "/home", "profile", "/user/profile");
      if (allowed.containsKey(id)) {
          response.sendRedirect(allowed.get(id));
      } else {
          // reject or show error
      }
      ```
  - Build and enforce a whitelist (allow-list) of permitted URLs or hosts; never rely on blacklists.
  - Validate the user is authorized for the redirect/forward target before performing it.
  - For external redirects, show an interstitial warning page requiring user confirmation.
  - In PHP, follow `header("Location: ...")` with `exit;` to stop execution.
  - Use sufficiently large or complex token spaces for IDs to prevent guessing and enumeration attacks.
  - Stay updated with framework versions and adopt security patches addressing open redirect vulnerabilities.
```