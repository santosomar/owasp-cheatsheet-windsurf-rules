```yaml
---
trigger: glob
globs: [yaml,yml,json,conf,ini,tf,sh,env]
---

rule: network-segmentation-best-practices
description: >
  Enforce effective multi-layer network segmentation and access control to contain breaches,
  limit lateral movement, and protect sensitive resources following OWASP guidelines.
severity: warning
tags: [network-segmentation, security, infrastructure, access-control]

message: >
  Follow a strict three-layer network segmentation: FRONTEND (internet-facing), MIDDLEWARE (business logic), and BACKEND (sensitive data).
  Enforce firewall rules denying direct FRONTEND-BACKEND or cross-backend access.
  Use VLANs and firewalls to isolate zones; limit interservice communication to only required flows.
  Collaborate with network/security teams to understand and implement documented network policies.
  All backend service calls must go through middleware; avoid direct frontend-to-backend access.
  Ensure logs are forwarded securely to immutable storage.
  Limit network permissions for CI/CD and monitoring tools explicitly.
  Remember network segmentation complements but does not replace application layer security.

recommendations:
  - "Design deployments respecting FRONTEND, MIDDLEWARE, BACKEND segmentation layers."
  - "Deny direct communication from FRONTEND to BACKEND; route all backend access via MIDDLEWARE."
  - "Implement and maintain strict firewall policies allowing only necessary traffic between zones."
  - "Use VLANs and firewalls to enforce network boundaries and inspect cross-zone traffic."
  - "Document network segmentation policies clearly and share with all stakeholders."
  - "Securely forward logs to isolated append-only logging servers to prevent tampering."
  - "Restrict and monitor network access for development (CI/CD) and monitoring tools."
  - "Maintain application-layer security controls alongside network segmentation."

example_bad: |
  # Frontend communicating directly with backend databases
  database_connection = "db.internal.example.com:5432"

example_good: |
  # Frontend only connects to middleware API; middleware handles database access
  middleware_api_endpoint = "middleware.internal.example.com/api"

---
```