```yaml
---
trigger: glob
globs: [java, cs, py, js, ts]
---
id: ldap-injection-prevention
name: Prevent LDAP Injection by Proper Input Handling and Escaping
description: |
  LDAP injection occurs when untrusted input manipulates LDAP queries, risking unauthorized data access or modification.
  To prevent this, always validate and escape user inputs based on their context using trusted libraries or frameworks.
  Avoid direct concatenation of raw inputs into LDAP queries.

severity: high
confidence: high

tags: [security, injection, ldap, input-validation, escaping]

message: |
  Possible LDAP injection risk. Ensure all LDAP inputs are validated against allowlists and escaped properly using context-aware APIs or libraries before inclusion in Distinguished Names or Search Filters.

patterns:
  - pattern-either:
      - pattern: |
          // Avoid patterns where untrusted input is concatenated directly into LDAP queries.
          // Example vulnerable pseudocode in Java:
          // String query = "(uid=" + userInput + ")";
          // Instead, use proper escaping methods.
      - pattern: |
          // Similar unsafe patterns in C#, Python, JavaScript, Typescript combining raw user data into LDAP filters or DNs.

fix: |
  1. Use allowlists (whitelists) to validate and restrict user input to safe characters before use.
  2. Escape user input correctly depending on LDAP context:
     - For Distinguished Names (DN), escape special chars: \ # + < > , ; " = and leading/trailing spaces per RFC2253.
     - For Search Filters, escape special chars: * ( ) \ and NUL per RFC4515.
  3. Prefer well-established libraries or framework features that automatically encode inputs:
     - Java: OWASP ESAPI `encodeForLDAP()` / `encodeForDN()`
     - .NET: Microsoft `Encoder.LdapFilterEncode()` / `Encoder.LdapDistinguishedNameEncode()`
     - Use LINQ to LDAP or equivalents with built-in escaping.
  4. Avoid manual string concatenation for LDAP queries.
  5. Implement least privilege on LDAP bind accounts.
  6. Use LDAP bind authentication with valid credentials to restrict access.
  7. Normalize inputs before validation and escaping.
  8. Regularly test your system against LDAP injection vulnerabilities following OWASP testing guides.

resources:
  - https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html
  - https://datatracker.ietf.org/doc/html/rfc4515
  - https://datatracker.ietf.org/doc/html/rfc2253
```