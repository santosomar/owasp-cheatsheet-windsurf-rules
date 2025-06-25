```yaml
---
trigger: glob
globs: [xml, wsdl, xsd, soap, java, cs, py, js]
---

id: secure-web-service-communication
message: >-
  Ensure your web services follow OWASP best practices for secure communication and processing.
  Enforce strong TLS transport security, strict server authentication, and robust user authentication.
  Validate all XML inputs against schemas to prevent injection and XML-based attacks.
  Use XML Digital Signatures for message integrity and encrypt sensitive data in transit and at rest.
  Authorize every request tightly and separate administrative functions.
  Limit message sizes and parser resources to mitigate DoS.
  Scan all file attachments for viruses before storage.
  Comply with WS-I Basic Profile for interoperability and security baseline.
  Enable XML parser protections against recursive payloads, entity expansion, and malformed XML.
help: |
  ⦿ Always configure TLS properly for ALL web service communications.
  ⦿ Validate server certificates strictly: trusted CA, expiry, revocation, domain match.
  ⦿ Use Mutual TLS or strong authentication schemes; avoid Basic Auth without TLS.
  ⦿ Enforce strict schema validation (XSD) on incoming XML.
  ⦿ Sign XML messages digitally to ensure integrity and non-repudiation.
  ⦿ Encrypt sensitive data beyond transport-level encryption when necessary.
  ⦿ Apply least privilege for each client operation and separate admin interfaces.
  ⦿ Limit SOAP message size and parser resource usage to prevent DoS.
  ⦿ Scan all attachments inline before storage using up-to-date virus definitions.
  ⦿ Encode outputs properly to prevent XSS if consumed by web clients.
  ⦿ Follow WS-I Basic Profile compliance for interoperability and security.
tags:
  - security
  - web services
  - soap
  - xml
  - tls
  - authentication
  - authorization
  - input-validation
  - dos-mitigation
severity: high
languages:
  - java
  - csharp
  - python
  - javascript

patterns:
  - pattern: >
      // Detect absence or improper TLS usage would require environment-level checks
      // So here we check for use of Basic Authentication without TLS or certificate validation missing.

      BasicAuth() if !TLSConfigured()
        ||
      ServerCertificateValidation() == false
  - pattern-not: "TLS transport"
  - pattern-not: "XMLSchemaValidation()"
  - pattern-not: "XMLSignature()"
  - pattern-not: "VirusScan()"
  - pattern-not: "MessageSizeLimit()"
  - pattern-not: "ResourceLimit()"
  - pattern-not: "MutualTLS()"
  - pattern-not: "StrictAuthorization()"

action: |
  Review all web service communication endpoints and ensure:
  - TLS v1.2+ is enforced and configured with strict certificate validation.
  - Basic Authentication only over TLS or replaced with stronger auth mechanisms like Mutual TLS or OAuth.
  - Incoming XML payloads are validated against XSD schemas with length and pattern allowlists.
  - XML Digital Signatures are applied to critical SOAP messages.
  - Sensitive data encryption is applied at transport and, if needed, at rest.
  - Every request is authorized according to least privilege principles.
  - Separate admin management API endpoints from regular service endpoints.
  - SOAP message sizes and XML parser resources are limited to prevent Denial of Service.
  - Virus scanning is performed inline on all SOAP attachments before storage.
  - Output encoding is applied if data is rendered in a web client context.
  - WS-I Basic Profile compliance is verified in your web service implementation.
  - XML parsers are configured to detect and reject recursive and oversized payloads, XML bombs, and external entity attacks.
```