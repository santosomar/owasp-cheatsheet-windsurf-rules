```yaml
---
trigger: glob
globs: [.java,.js,.ts,.go,.py,.rb,.cs,.json,.yaml,.yml]
---

title: Secure Microservices Authorization and Authentication Best Practices

description: |
  Ensure microservices implement defense-in-depth authorization, secure identity propagation, strong service authentication, and robust, privacy-conscious logging.

author: OWASP Microservices Security Cheat Sheet (summary)

rule: |
  # Authorization Strategy: Defense in Depth
  - Always enforce coarse-grained authorization at API gateways or edges.
  - Implement fine-grained authorization inside each microservice for business logic enforcement.
  - Do NOT rely solely on edge authorization; avoid gateway bypass risks.
  
  # Service-Level Authorization Patterns
  - Centralize authorization policies using a dedicated PDP platform but evaluate them locally within microservices.
  - Avoid hardcoding authorization logic; externalize policies (e.g., XACML) for maintainability.
  - Collaborate with platform/security teams to manage policies and authorization SDKs securely.
  - Enforce formal change control and testing procedures for access control rules.

  # External Entity Identity Propagation
  - Never propagate raw external tokens downstream to internal services.
  - Use signed/encrypted opaque internal tokens ("passports") that carry minimal claims needed by services.
  - Keep internal tokens internal; do not expose them outside the trusted boundary.
  
  # Service-to-Service Authentication
  - Use mutual TLS (mTLS) to authenticate and encrypt service connections whenever possible.
  - When using token-based auth, always combine with TLS and perform online revocation checks for critical operations.
  - Implement secure key provisioning, rotation, and bootstrapping processes.

  # Logging and Auditing
  - Write logs to local files first and forward asynchronously via a logging agent and message broker.
  - Enforce mutual authentication and TLS between logging agents and brokers.
  - Apply least privilege access control on logging infrastructure.
  - Sanitize logs to remove PII and sensitive data prior to transmission.
  - Use structured logging formats (e.g., JSON) enriched with correlation IDs and relevant context.
  - Monitor logging system health continuously.
  
recommendations:
  - Use shared libraries or sidecars to integrate authorization logic consistently.
  - Collaborate with security teams for policy management and platform support.
  - Validate internal tokens strictly and avoid any trust on external tokens within services.
  - Practice formal governance and testing with every policy update.
  - Design logs to aid comprehensive tracing without compromising sensitive info or service availability.
```