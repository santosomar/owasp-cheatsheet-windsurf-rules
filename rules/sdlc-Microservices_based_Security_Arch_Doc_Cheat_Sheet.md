---
trigger: glob
globs: [yaml,yml,json,md,dot,proto,java,js,ts,go,py]
---
# Microservices Security Architecture Best Practices

# Ensure comprehensive documentation for every microservice and infrastructure component:
# - Document unique service IDs, business functions, source code repos, API definitions with security schemes (scopes, API keys),
#   architecture diagrams, and runbooks.
# - Include infrastructure components (auth, logging, discovery), data storages, message queues, and classify data assets with protection levels.

# Map and maintain up-to-date relationships between components:
# - Detail service-to-storage access permissions and service-to-service communication (sync/async), including protocols and data types.
# - Create and update visual diagrams (e.g., DOT graphs) representing service calls, data flows, and trust boundaries.

# Use this documentation to enforce strong security controls:
# - Apply the principle of least privilege by assigning minimal necessary permissions based on documented scopes and data flows.
# - Enumerate all endpoints from API definitions and infrastructure docs to focus security testing on critical attack surfaces.
# - Track sensitive data movement across the system to detect and prevent leakage.
# - Verify and justify all trust boundaries and data flows to restrict unauthorized access.
# - Centralize authentication, authorization, logging, and monitoring to maintain consistent, vetted security mechanisms.
# - Ensure sensitive data classification is complete and strictly enforced.

# Align your security activities with OWASP standards such as ASVS and Top 10 Sensitive Data Exposure to enhance verification rigor.

# Developer Action Items:
# - Keep all architecture and security documentation current and integrated into your development lifecycle.
# - Explicitly define and enforce minimal privileges for APIs, databases, and messaging systems.
# - Regularly update and review service interaction maps and data flow diagrams to support threat modeling.
# - Centralize reusable security controls to prevent inconsistent implementations or gaps.
# - Classify and monitor sensitive data assets proactively to detect potential exposure.
# - Use documented architecture to guide targeted security assessments, focusing on exposed endpoints and critical data paths.
```