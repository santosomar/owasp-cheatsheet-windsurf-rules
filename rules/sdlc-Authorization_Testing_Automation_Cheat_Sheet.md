```yaml
---
trigger: glob
globs: [.java, .js, .ts, .py, .go, .rb, .xml, .yaml, .yml]
---

title: Enforce Automated Authorization Testing Using a Formal Authorization Matrix

description: |
  Authorization issues frequently emerge after feature or role changes. 
  Automate authorization tests driven by a formal authorization matrix to detect regressions early and ensure reliable access control enforcement.

rule: |
  - Define a formal authorization matrix file (preferably XML or YAML) that lists:
    - All features/services/endpoints.
    - Logical roles and data filters if applicable.
    - Expected HTTP response codes for allowed and denied accesses.
    - Optional test payloads per service for richer testing.

  - Automate integration tests to:
    - Dynamically load and iterate over the matrix entries.
    - Generate role-based access tokens (e.g., JWT) matching each logical role.
    - Call each service endpoint as each role.
    - Validate actual HTTP response codes against expected allowed/denied codes from the matrix.
    - Report any discrepancies immediately, specifying involved role, service, and unexpected response.

  - Factorize test logic to centralize token creation, service calls, and response validation while isolating role-based POVs for clear error profiling.

  - Maintain the authorization matrix as a living document alongside code; update it whenever authorization changes occur.

  - Provide a readable, auditable view of the authorization matrix (HTML via XSLT or similar) accessible to developers and auditors for verification.

advice: |
  - Automate authorization testing on every build/release to catch regressions early.
  - Use machine- and human-readable files for the authorization matrix to simplify maintenance and audit.
  - Generate realistic role-based tokens dynamically to simulate real user contexts accurately.
  - Keep tests concise and focused per role to isolate authorization errors clearly.
  - Review and audit the authorization matrix periodically with your security team to ensure coverage and correctness.
```