```yaml
---
trigger: glob
globs: [js, ts, java, py, rb, php, cs, go, swift]
---

id: owasp-authorization-best-practices
name: OWASP Authorization Best Practices
description: |
  Enforce robust authorization controls to prevent broken access control vulnerabilities by following OWASP core principles.
severity: high
confidence: high

message: >
  Ensure strict authorization enforcement: apply least privilege, deny-by-default,
  validate permissions on every request server-side, protect object IDs, and centralize failure handling.

patterns:
  - pattern-either:
      - pattern: |
          // Common anti-pattern: missing authorization check or relying only on authentication
          if (user.isAuthenticated()) {
              // no authorization validation here
              ...
          }
      - pattern: |
          // Direct use of predictable identifiers without authorization check
          getObjectById(req.params.id);

      - pattern: |
          // Client-side only authorization enforcement
          if (user.canAccess()) { renderContent(); } // no server-side check

      - pattern: |
          // No centralized error handling for authorization failures
          if (!authorized) { 
            res.status(500).send("Error"); 
          }

suggestion: |
  Follow these best practices:
  - Differentiate clearly between authentication and authorization.
  - Implement least privilege: assign minimal permissions and audit regularly.
  - Default-deny all access and require explicit permission grants.
  - Enforce authorization checks on every request at the server/backend level, using centralized middleware or filters.
  - Avoid exposing predictable/internal object IDs; use opaque references and always check access per object.
  - Protect static resources through access control policies consistent with dynamic content.
  - Never rely solely on client-side checks for authorization enforcement.
  - Handle authorization failures uniformly with appropriate HTTP status codes and no sensitive info leakage.
  - Log authorization decisions, failures, and anomalies for audit and monitoring.
  - Automate tests for authorization logic covering edge cases and failure paths.
  - Review and customize third-party framework authorization, keeping dependencies updated.
  - Prefer fine-grained, attribute- or relationship-based access control models for complex apps.
  
  Integrate authorization testing into your CI pipeline to catch regressions early and maintain secure access controls.
```