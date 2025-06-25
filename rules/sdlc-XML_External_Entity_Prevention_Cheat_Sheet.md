```yaml
---
trigger: glob
globs: [java, cs, cpp, h, c, php, py, swift, m, xml, xsd, xslt, cfml]
---

rule:
  id: owasp-xxe-prevention-best-practices
  patterns:
    - pattern-either:
        # Generic check for XML parser configurations disabling DOCTYPE or external entities
        - pattern: |
            factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true)
        - pattern: |
            xmlResolver = null
        - pattern: |
            reader.DtdProcessing = DtdProcessing.Prohibit
        - pattern: |
            libxml_set_external_entity_loader(null)
        - pattern: |
            # In Python, usage of defusedxml to parse XML securely
            import defusedxml
        - pattern: |
            this.xmlFeatures = 'disallow-doctype-decl, disallow-external'
        - pattern: |
            NSXMLDocument with NSXMLNodeLoadExternalEntitiesNever
  message: |
    XML External Entity (XXE) attack prevention:
    - Always disable DTD processing and external entity resolution unless explicitly needed.
    - Configure your XML parsers to disallow DOCTYPE declarations and external entity loading.
    - Use library-specific secure parser configuration:
      * Java: set `disallow-doctype-decl` and disable external entities on `DocumentBuilderFactory` and others.
      * .NET: set `XmlResolver = null`, `DtdProcessing = Prohibit`, and ensure targetFramework ≥4.5.2.
      * C/C++: disable flags like `XML_PARSE_NOENT` and `XML_PARSE_DTDLOAD`; use libxml2 ≥2.9.
      * PHP: call `libxml_set_external_entity_loader(null)` for older versions.
      * Python: use `defusedxml` or similar secure XML libraries.
      * ColdFusion: set `ALLOWEXTERNALENTITIES=false` or equivalent.
      * iOS: use `NSXMLNodeLoadExternalEntitiesNever` flag.
    - Always keep XML libraries up-to-date with security patches.
    - Reject or sanitize untrusted XML inputs before processing.
    - Avoid unsafe APIs such as `java.beans.XMLDecoder`.
    - Leverage static analysis tools (e.g., Semgrep rules) to identify risky XML parsing code.
  severity: warning
  metadata:
    category: security
    cwe: "CWE-611: Improper Restriction of XML External Entity Reference"
    owasp: "A4:2021 – XML External Entities (XXE)"
  fix:
    - "Disable DTDs completely in your XML parser configuration whenever possible."
    - "Explicitly disable external entity resolution on your XML parser."
    - "For Java, set `factory.setFeature('http://apache.org/xml/features/disallow-doctype-decl', true)`."
    - "For .NET, set `XmlResolver = null` and `DtdProcessing = Prohibit`."
    - "Use secure parsing libraries like defusedxml (Python) or updated parser versions."
    - "Regularly update XML libraries and frameworks."
    - "Avoid using `java.beans.XMLDecoder` unless inputs are fully trusted."
    - "Test your codebase with static analysis tools specialized in XXE detection."
```