---
trigger: glob
globs: [.java, .js, .ts, .py, .go, .rb, .xml, .yaml, .yml]
---

Enforce Automated Authorization Testing Using a Formal Authorization Matrix

Automate authorization tests driven by a formal authorization matrix to detect regressions early and ensure reliable access control enforcement.

  1. Define a formal authorization matrix file (preferably XML or YAML) that lists:
    - All features/services/endpoints.
    - Logical roles and data filters if applicable.
    - Expected HTTP response codes for allowed and denied accesses.
    - Optional test payloads per service for richer testing.

  2. Automate integration tests to:
    - Dynamically load and iterate over the matrix entries.
    - Generate role-based access tokens (e.g., JWT) matching each logical role.
    - Call each service endpoint as each role.
    - Validate actual HTTP response codes against expected allowed/denied codes from the matrix.
    - Report any discrepancies immediately, specifying involved role, service, and unexpected response.

  3. Factorize test logic to centralize token creation, service calls, and response validation while isolating role-based POVs for clear error profiling.

  4. Maintain the authorization matrix as a living document alongside code; update it whenever authorization changes occur.

  5. Provide a readable, auditable view of the authorization matrix (HTML via XSLT or similar) accessible to developers and auditors for verification.