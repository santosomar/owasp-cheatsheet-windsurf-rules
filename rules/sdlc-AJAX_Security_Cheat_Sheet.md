```yaml
---
trigger: glob
globs: [js, jsx, ts, tsx, java, py, cs, php]
---

  Follow AJAX security best practices to prevent common web vulnerabilities.


1. Avoid dangerous JavaScript functions that evaluate code dynamically.
2. Detect usage of eval, new Function, setTimeout or setInterval with string argument.
  (eval\()|(new\s+Function\()|(setTimeout\s*\(\s*['"`])|(setInterval\s*\(\s*['"`])

3. Detect usage of innerHTML assignments.
  |innerHTML\s*=

4. Detect calls transmitting secrets or encryption done on client side.
  #(This requires context; flag common keywords only)
  |(encrypt|decrypt|secret|privateKey|password).*

5. Detect building JSON or XML by string concatenation (rough heuristic).
  #    The pattern looks for + operators near quotes or object literals.
  |(["']\s*\+\s*[^\s]+)|(>\s*\+\s*["'])|(\+\s*\{)|(\}\s*\+)

6. Detect client side security or business logic comments or suspicious conditionals (heuristic).
  #    We look for keywords in comments or strings.
  #(optional and not covered by patterns here)

  # Since multiple patterns can't be separated in one regex easily, Windsurf will match any of these patterns 
  # and show the advice below.

fix: |
  1. Replace `.innerHTML` usages with `.innerText`, `.textContent`, or a safe templating method to prevent XSS.
  2. Never use `eval()`, `new Function()`, `setTimeout()` or `setInterval()` with string arguments to avoid code injection.
  3. Do not perform encryption or transmit secrets on the client side; keep secrets and encryption logic server-side.
  4. Avoid building JSON or XML by string concatenation. Use built-in or third-party safe serialization libraries.
  5. Never trust client-side security or business logic. Always enforce all security and business rules on the server.
  6. On the server, validate all inputs rigorously as services can be called directly by attackers.
  7. Use CSRF protection mechanisms for all state-changing AJAX requests.
  8. Return JSON responses with an object as the outermost element to prevent JSON hijacking.
  9. Use JSON or XML schemas with libraries to validate inputs and outputs of AJAX services.

notes: |
  - For encoding untrusted data in HTML contexts, prefer `.innerText` over `.innerHTML`.
  - The OWASP Java Encoder Project (https://owasp.org/www-project-java-encoder/) is a good resource.
  - Avoid writing serialization code manually on either client or server side—use trusted libraries.
  - Never rely on client side code for enforcing security or sensitive business logic.
  - Protect AJAX endpoints as you would normal APIs: validate inputs, authenticate and authorize requests.
