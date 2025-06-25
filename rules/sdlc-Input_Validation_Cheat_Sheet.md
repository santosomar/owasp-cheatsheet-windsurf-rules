---
trigger: glob
globs: [js, ts, java, py, rb, php, cs, go, json, xml, html, css]
---

rule: Input Validation Best Practices (OWASP Cheat Sheet)


  Ensures developers validate all untrusted input early and robustly to prevent injection and other attacks.
  Highlights the use of allowlist validation, syntactic and semantic checks, server-side enforcement,
  safe file upload handling, and email validation best practices.

recommendations:
  - Always perform input validation on the server side; client-side validation is insufficient and untrusted.
  - Use allowlist (whitelist) validation to define exact acceptable input patterns or values, avoiding error-prone denylist filters.
  - Combine syntactic validation (e.g., anchored regex, schema validation) with semantic validation (business rules) where applicable.
  - Enforce strict length limits and type checking; handle parsing exceptions to avoid unexpected behavior.
  - Normalize Unicode inputs and restrict character sets for free-form text; avoid overly restrictive patterns that impair usability.
  - For free text fields (comments, names), rely primarily on context-aware output encoding to prevent injection vulnerabilities.
  - When handling file uploads:
      * Allowlist permitted file extensions and MIME types; reject dangerous or unknown files (.php, .htaccess, crossdomain.xml, etc.).
      * Validate file names; do not use user-supplied file names directly—rename files with server-generated random names.
      * Check archive contents before extraction; use image processing libraries to verify and sanitize images.
      * Enforce maximum file sizes to reduce resource abuse.
      * Serve uploaded files with correct Content-Type headers; never trust client-supplied metadata.
  - For email addresses:
      * Perform basic syntactic validation (one `@`, allowed characters, length limits).
      * Rely on confirmation workflows with secure, single-use, time-limited tokens to verify ownership.
      * Avoid stripping sub-addressing tags; be aware of disposable email limitations.
  - Use existing, reputable validation libraries and frameworks (e.g., JSON Schema, Apache Commons Validator).
  - Avoid complex or overly permissive regex to prevent ReDoS attacks; prefer simple, anchored patterns.
  - Remember input validation reduces attack surface but must be paired with context-specific output encoding and other protections (e.g., parameterized SQL, XSS encoding).

rationale: |
  Input validation is the first line of defense against malformed or malicious data.
  Proper validation minimizes the chance of injection and other input-based attacks,
  but alone it cannot eliminate them—output encoding and safe coding practices remain essential.

references:
  - https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
  - https://cheatsheetseries.owasp.org/cheatsheets/XSS_Prevention_Cheat_Sheet.html
```