```yaml
---
trigger: glob
globs: [md, rst, txt]
---
id: deprecated-transport-layer-protection
name: Deprecated Transport Layer Protection Cheat Sheet Usage
message: |
  The Transport Layer Protection Cheat Sheet is deprecated.
  Please update your references and practices to use the Transport Layer Security Cheat Sheet instead:
  Transport_Layer_Security_Cheat_Sheet.md
severity: info
tags: [deprecated, documentation, security]
help: |
  Avoid relying on outdated or deprecated guidance.
  Review and follow the latest Transport Layer Security Cheat Sheet to ensure modern, secure transport layer protections such as:
  - Use of TLS 1.2 or higher
  - Strong cipher suites and key exchange algorithms
  - Proper certificate and trust management
  - Secure configuration of TLS on your servers and clients
  Update documentation links, training materials, and code comments accordingly.
```
