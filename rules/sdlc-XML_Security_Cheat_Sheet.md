---
trigger: glob
globs: [.xml, .xsd, .xslt, .wsdl]
---

  Enforce robust XML security practices to prevent XXE, SSRF, DoS, schema poisoning,
  and data integrity issues in XML parsing and validation.



 "Use a standards-compliant XML parser configured to disable DTD processing and external entity resolution to prevent XXE and entity expansion attacks."
    pattern: |
      // Disable DTDs and external entities in parser configuration
    suggest: |
      - Ensure your XML parser rejects malformed XML documents and halts processing on fatal errors.
      - Configure parser features such as `disallow-doctype-decl`, `external-general-entities`, and `external-parameter-entities` set to false or disabled.

 "Validate all XML documents strictly against local, trusted XML Schemas (XSDs) with narrow data type restrictions and clearly defined element occurrence limits."
    pattern: |
      // Validation against schemas should use local, tightly-restricted copies
    suggest: |
      - Avoid or limit the use of DTDs; prefer comprehensive XSD validation.
      - Use schemas with explicit types, length limits, regex patterns, enumerations, and xs:assertion where appropriate.
      - Set maxOccurs explicitly to control element multiplicity.
      - Store schemas locally with strict filesystem permissions and never load schemas over unencrypted HTTP.

 "Prevent resource exhaustion by rejecting XML documents with excessive depth, nested unclosed tags, or large size to avoid DoS."
    pattern: |
      // Reject deeply nested or very large XML content
    suggest: |
      - Enforce limits on XML element nesting depth and document size.
      - Test parser CPU usage differences between valid and malformed XML inputs.
      - Reject or timeout processing on unexpectedly complex documents.

 "Block or sandbox XML processing from making remote network calls to mitigate SSRF and information disclosure risks."
    pattern: |
      // Disallow network calls triggered by XML external entities or parameter entities
    suggest: |
      - Disable external entity resolution or restrict it to local, whitelisted resources only.
      - Validate and sanitize all external URI references in XML entities.
      - Monitor for unexpected DNS lookups or network activity during XML parsing.

 "Log and monitor XML parsing errors and rejections to detect injection attempts, malformed XML attacks, or schema poisoning."
    pattern: |
      // Implement logging on XML parser errors and validation failures
    suggest: |
      - Capture detailed error information without exposing sensitive data.
      - Alert on repeated or suspicious XML parse failures.
      - Audit local schema files regularly for unauthorized changes.

best_practices: |
  - Always reject unexpected elements, attributes, or data outside the schema definitions.
  - Perform business logic validation on XML data after schema validation (e.g., numeric ranges on payment amounts).
  - Keep XML processing libraries up to date and use secure configurations by default.
