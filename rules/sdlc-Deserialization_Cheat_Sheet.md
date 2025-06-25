---
trigger: glob
globs: [java, cs, py, php, xml, json, yml, yaml]
---

rule: Avoid Unsafe Deserialization of Untrusted Data

description: |
  Deserialization of untrusted input can lead to critical vulnerabilities such as remote code execution, denial of service, and privilege escalation. This rule ensures developers follow best practices to safely handle serialization and deserialization operations.

recommendations:
  - Always treat incoming serialized data from untrusted sources as hostile.
  - Prefer standardized, safe data formats like JSON or XML without type metadata over native serialization formats.
  - Avoid using unsafe native serialization APIs on untrusted input, such as:
    - PHP: avoid `unserialize()`, use `json_decode()`/`json_encode()` instead.
    - Python: avoid `pickle.loads`, `yaml.load` (use `safe_load`), and `jsonpickle` on untrusted data.
    - Java: override `ObjectInputStream#resolveClass()` to whitelist classes; mark sensitive fields `transient`; avoid polymorphic deserialization unless strictly allowlisted.
    - .NET: avoid `BinaryFormatter`; use `DataContractSerializer` or `XmlSerializer`; set `TypeNameHandling = None` in JSON.Net; never trust deserialized types blindly.
  - Sign serialized data and verify signatures to ensure integrity before deserialization.
  - Configure serialization libraries securely:
    - Disable unsafe features like autotype in fastjson2.
    - Use allowlists in libraries such as XStream and jackson-databind.
    - Keep dependencies updated to fixed versions.
  - Reject or safely handle polymorphic or complex objects deserialization from untrusted sources.
  - Use hardened deserialization agents/tools (e.g., SerialKiller, hardened ObjectInputStream subclasses, JVM agents).
  - Regularly scan code and dependencies for unsafe deserialization patterns using static and dynamic analysis tools.

security_impact: High - insecure deserialization can lead to remote code execution and complete system compromise.

why:
  Deserialization attacks are a frequently exploited vector leading to severe security impacts. Following these practices prevents attackers from injecting malicious objects or payloads that the application may execute.

examples:
  avoid:
    - PHP: calling `unserialize($data)` on external input.
    - Java: deserializing classes without strict allowlisting or type validation.
    - Python: loading YAML with `yaml.load()` on untrusted data.
    - .NET: using `BinaryFormatter.Deserialize()` on untrusted input.
  recommended:
    - PHP: use `json_decode()` and validate JSON schema.
    - Java: override `resolveClass()` to allowlist safe classes.
    - Python: use `yaml.safe_load()` or custom parsers.
    - .NET: use `DataContractSerializer` with explicit known types and disable type name handling.

references:
  - https://owasp.org/www-project-top-ten/ (A9:2017 - Using Components with Known Vulnerabilities)
  - https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html

action_for_developers: |
  Review all deserialization logic in your codebase. Replace unsafe native deserialization calls with safe formats and libraries. Implement strict class allowlists and avoid any dynamic type loading. Sign and verify serialized data when possible. Keep all libraries up-to-date and monitor security advisories related to deserialization vulnerabilities.