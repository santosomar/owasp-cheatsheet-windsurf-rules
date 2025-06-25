---
trigger: glob
globs: [xml, saml, jsp, java, py, js]
---

Ensure SAML SSO is implemented following OWASP best practices to prevent common security issues like signature wrapping, token replay, and improper validation.

# Transport Security
check: |
  # Always use TLS 1.2 or higher for any transport carrying SAML messages.
  # Verify your app enforces HTTPS usage and rejects insecure connections.

# Signature and Encryption
check: |
  # Digitally sign SAML assertions or entire responses using locally stored, trusted IdP certificates.
  # Avoid trusting KeyInfo elements from incoming XML; do not use dynamic keys for validation.
  # Encrypt assertions using XML Encryption to protect sensitive data after transit.

# Strict Validation of SAML Elements
check: |
  # Validate all required protocol elements strictly:
  # - AuthnRequest must have unique ID and valid SP identifier.
  # - Responses must contain unique ID, SP and IdP identifiers, and signed assertions.
  # - Authentication Assertions must include ID, client, IdP, and SP identifiers.
  # Always ensure InResponseTo matches a previously sent request ID.

# XML Signature Wrapping Protection
check: |
  # Perform strict XML schema validation with local trusted schemas; disable wildcard namespaces.
  # Never select XML elements solely by tag name; use absolute XPath expressions for element selection.
  # Validate signatures only against fixed trusted keys; reject messages that fail schema or signature checks.

# SAML Protocol Compliance and Replay Prevention
check: |
  # Follow official SAML Core and Profiles specs for protocol processing.
  # Enforce NotBefore and NotOnOrAfter conditions; validate Recipient attributes.
  # Implement replay detection mechanisms and reject expired or replayed assertions.

# Secure Binding Handling
check: |
  # When using HTTP Redirect or POST bindings, correctly encode/decode SAML messages.
  # Disable caching of SAML messages and assertions to prevent replay or token theft.

# Countermeasures and IdP-Initiated Flows
check: |
  # Use IP filtering for trusted partners where possible.
  # Set short response lifetimes and mark responses as OneTimeUse.
  # Avoid or carefully secure IdP-initiated SSO:
  # - Validate RelayState against allowlists.
  # - Detect and reject replayed unsolicited responses.

# Identity Provider and Service Provider Best Practices
check: |
  # Use strong, current X.509 certificates and cryptographic algorithms.
  # Verify signature trust chains, revocation status, and certificate expiration.
  # Validate assertion conditions and audience restrictions.
  # Securely manage user sessions after assertion validation.

# Input Validation and Cryptography
check: |
  # Rigorously validate all inputs from SAML messages as untrusted external data.
  # Use modern cryptography; avoid weak or deprecated algorithms like RSA 1.5 XML Encryption.


  Always enforce strict schema validation and signature verification with local trusted keys.
  Protect all SAML transport with TLS 1.2+ and encrypt assertions where possible.
  Validate all required protocol elements and prevent replay attacks.
  Harden XML processing by using absolute XPath and rejecting element selection by name only.
  Employ short-lived, one-time-use tokens and IP-filter partner endpoints.
  Avoid IdP-initiated SSO flows unless fully validated and secured.
  Maintain strong certificate validation and session management.
  Finally, treat all SAML inputs as untrusted and use current cryptographic standards only.
