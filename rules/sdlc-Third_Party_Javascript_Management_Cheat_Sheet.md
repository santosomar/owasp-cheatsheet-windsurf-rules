```yaml
---
trigger: glob
globs: [.html,.js,.jsx,.ts,.tsx]
---

id: secure-third-party-js
message: >
  Third-party JavaScript tags carry significant risks including arbitrary code execution and data leakage. Follow these best practices to protect your web application and users:

severity: warning
languages: [javascript, typescript, html]

labels:
  - security
  - third-party
  - javascript
  - privacy

rule: |
  # 1. Prefer a Server-Driven Data Layer Architecture
  #    - Only your first-party code should populate a controlled, sanitized data layer.
  #    - Third-party scripts should read exclusively from this vetted data layer.
  #    - Avoid passing URL params or untrusted DOM data directly to third-party scripts.

  # 2. Never Include Vendor JavaScript Inline or Call Directly Without Controls
  #    - Avoid direct script includes from vendor URLs without integrity checks.
  #    - Use tag managers with careful, limited access and strict configuration governance.

  # 3. Enforce Subresource Integrity (SRI) with crossorigin Attribute
  #    - Always specify SRI hashes on third-party script tags, e.g.:
  #      <script src="..." integrity="sha384-..." crossorigin="anonymous"></script>
  #    - Regularly monitor vendor scripts for hash mismatches or updates.

  # 4. Isolate High-Risk Third-Party Scripts Using Sandboxing
  #    - Employ sandboxed iframes with restrictive `sandbox` attributes to contain third-party code.
  #    - Consider virtual iframe containment for asynchronous or dynamic loading scenarios.

  # 5. Sanitize and Validate Data Sent to Third Parties
  #    - Use XSS sanitizers (e.g., DOMPurify) before including any dynamic data in analytics or tag payloads.
  #    - Restrict data sent to only what is necessary, fully validated and encoded.

  # 6. Keep All JavaScript Libraries Up to Date
  #    - Regularly update dependencies and monitor for known vulnerabilities to minimize risk exposure.

  # 7. Contractual and Operational Controls
  #    - Require evidence of secure coding, integrity checks, and source control from vendors.
  #    - Include contractual penalties for serving malicious code.
  #    - Implement ongoing cross-team security operations for monitoring and maintaining tag and data layer security.

  # 8. Minimize Exposure
  #    - Limit which third-party tags run on which pages or events.
  #    - Prefer architectures where your trusted code runs client-side controlling data flow.

  # Summary:
  # Secure third-party JavaScript by combining: strict data layer isolation, SRI enforcement, sandbox containment,
  # rigorous data sanitization, operational vigilance, and contractual assurances.
```