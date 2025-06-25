```yaml
---
trigger: glob
globs: [js, jsx, ts, tsx, java, kt, py, rb, php, go, cs, swift]
---

id: prevent-insecure-direct-object-reference
name: Prevent Insecure Direct Object References (IDOR)
message: "Avoid exposing direct object references without proper access control. Always verify user authorization before accessing or modifying objects."
severity: high
languages: [javascript, typescript, java, kotlin, python, ruby, php, go, csharp, swift]
tags: [security, access-control, idor]

pattern: |
  # Detect usage of direct object references in URLs, parameters, or form fields without immediate surrounding access checks
  # This requires customized implementation per language/web framework, so this pattern flags references to ID parameters in handlers/controllers.
  
  # Example (pseudocode):
  # Look for queries like find(params[:id]) or find(request.GET["id"]) without subsequent user ownership check

suggestion: |
  1. Always enforce authorization checks on the server side for every object access, verifying the user has permission to the requested resource.
  2. Prefer fetching objects scoped to the current user or their allowed data sets (e.g., use current_user.projects.find(id) instead of raw find(id)).
  3. Use non-enumerable, hard-to-guess identifiers such as UUIDs or random strings instead of sequential numeric IDs.
  4. Avoid exposing identifiers in URLs or form fields whenever possible; rely on authenticated session context.
  5. In multi-step flows, keep sensitive identifiers in the server-side session rather than passing them through client-side inputs.
  6. Avoid encrypting identifiers unless you have a robust, secure scheme; better to use opaque random tokens or UUIDs.
  7. Leverage your web framework’s standard authorization mechanisms to implement these checks consistently across the app.
```