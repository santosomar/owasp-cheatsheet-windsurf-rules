```yaml
---
trigger: glob
globs: [js, jsx, ts, tsx, html]
---

id: dom-xss-prevention
title: Prevent DOM Based XSS - Context-Aware Encoding & Safe DOM Manipulation
description: |
  DOM XSS occurs when untrusted data is injected into the browser DOM without correct context-aware encoding 
  or proper API usage, allowing attacker-controlled scripts to execute. Follow these critical rules to prevent DOM XSS.

author: OWASP Cheat Sheet adaptation
severity: high
tags: [security, xss, dom-xss, encoding, javascript, frontend]

message: >-
  Potential DOM XSS vulnerability detected. Ensure untrusted data is properly encoded 
  based on its DOM context and prefer safe DOM APIs over direct HTML injection.

languages: [javascript, typescript]

patterns:
  # Detect assignment to innerHTML, outerHTML, document.write with untrusted data
  - pattern-either:
      - pattern: |
          $EL.innerHTML = $DATA
      - pattern: |
          $EL.outerHTML = $DATA
      - pattern: |
          document.write($DATA)
      - pattern: |
          document.writeln($DATA)

  # Usage of eval-like constructs with variable data
  - pattern-either:
      - pattern: |
          eval($DATA)
      - pattern: |
          new Function($DATA)
      - pattern: |
          setTimeout($DATA, $TIME)
        condition: $DATA instanceof String or $DATA contains dynamic variable

  # Event handler attributes assignment as string
  - pattern: |
      $EL.setAttribute($ATTR, $DATA)
    where:
      $ATTR =~ /^on/i

  # Unsafe direct insertion of untrusted input as object keys (simple heuristic)
  - pattern: |
      $OBJ[$DATA] = $VAL

fix: |
  # Key Recommendations and Fixes:
  - Never use untrusted input directly as code or markup. Treat it strictly as text.
  - Replace `innerHTML`, `outerHTML`, `document.write()` assignments with `textContent` or `innerText`:
      ```js
      element.textContent = untrustedData; // safe insertion as text
      ```
  - When inserting untrusted data into HTML subcontexts (e.g. innerHTML), first encode for HTML, then JavaScript:
      ```js
      element.innerHTML = encodeForJavaScript(encodeForHTML(untrustedData));
      ```
  - For HTML attribute subcontexts, JavaScript encode only:
      ```js
      element.setAttribute('title', encodeForJavaScript(untrustedData));
      ```
  - For URL attributes and CSS contexts, apply URL encoding first, then JavaScript encoding.
  - Avoid injecting untrusted data directly into event handler strings; instead assign functions directly:
      ```js
      element.onclick = function() { /* safe code */ };
      ```
  - Avoid `eval()`, `new Function()`, and string-based `setTimeout`. Use closures or safe parsing (`JSON.parse`) instead.
  - Build dynamic interfaces using safe DOM APIs:
      ```js
      const el = document.createElement('div');
      el.textContent = untrustedData;
      parent.appendChild(el);
      ```
  - Validate and whitelist object property keys from untrusted input to prevent prototype pollution or logic bypass.
  - Use established encoding libraries (e.g., OWASP ESAPI, Java Encoder) for all encoding needs.
  - Perform server-side encoding on output and complement with client-side DOM-context-specific encoding.
  - Enable strict mode and sandbox JS environments where possible.
  - Regularly audit and test your codebase for DOM XSS with static analysis and dynamic tools.

recommendation: Always apply context-aware encoding and prefer safe DOM APIs to prevent client-side injection.
```