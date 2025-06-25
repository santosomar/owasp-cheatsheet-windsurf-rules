```yaml
---
trigger: glob
globs: [js,ts,java,py,go,cs,cpp,rb,php,sh,dockerfile,yml,yaml,env]
---

id: secure-product-design
name: Secure Product Design Best Practices
description: |
  Enforce core security principles and practices throughout software design and development to build resilient, secure products aligned with organizational standards.
severity: high
tags: [security, secure_design, owasp]

message: |
  Follow these secure product design guidelines:

  1. Apply core security principles:
     - Enforce Least Privilege & Separation of Duties for users and components.
     - Implement Defense-in-Depth using layered security controls.
     - Adopt a Zero Trust mindset: authenticate & authorize every access.
     - Practice Security-in-the-Open: collaborate openly on secure coding and testing.

  2. Understand your product context:
     - Conduct threat modeling early and continuously to identify risks.
     - Align security requirements with data sensitivity and organizational context.

  3. Select and manage components securely:
     - Use maintained, secure third-party libraries; check licenses and update policies.
     - Follow your organization’s secure “Golden Path” design patterns.

  4. Secure connections and environments:
     - Limit and segregate communication paths based on security needs.
     - Use secure protocols (e.g., HTTPS/TLS) everywhere.
     - Architect systems to uphold data segregation and security boundaries.

  5. Implement secure coding and testing:
     - Validate all inputs strictly to prevent injection and overflows.
     - Handle errors without leaking sensitive information.
     - Enforce strong authentication and authorization.
     - Avoid hardcoded secrets; use secure secret management.
     - Use strong, vetted cryptographic algorithms for data protection.
     - Prefer memory-safe languages or apply strict memory management.
     - Continuously test security: automated scans, manual reviews, and threat/abuse scenario tests.
     - Keep dependencies and codebase patched and updated.

  6. Maintain secure configurations and incident readiness:
     - Configure defaults securely with least privilege; avoid post-deployment manual hardening.
     - Ensure systems fail securely without sensitive data exposure.
     - Encrypt sensitive data at rest and in transit.
     - Use trusted base images for containers and keep them updated.
     - Establish and regularly rehearse incident response plans.

  Adopt these principles from design to deployment to build secure, resilient products.

# Note: This rule is a reminder and checklist for developers and reviewers to embed security from start to finish.
```