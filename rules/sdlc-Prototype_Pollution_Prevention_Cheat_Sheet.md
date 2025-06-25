```yaml
---
trigger: glob
globs: [.js, .jsx, .ts, .tsx]
---
id: prototype-pollution-prevention
message: >
  Prevent Prototype Pollution vulnerabilities by avoiding object literals for maps/sets,
  using safe object creation patterns, and protecting prototypes.

recommendation: |
  1. Prefer using `new Set()` and `new Map()` over plain object literals for collections to avoid prototype inheritance risks.
  2. When plain objects are required as maps, create them with `Object.create(null)` to eliminate inherited prototype properties:
     ```js
     let obj = Object.create(null);
     ```
  3. As a last resort, initialize object literals with `__proto__: null` to prevent prototype pollution:
     ```js
     let obj = { __proto__: null };
     ```
  4. Use `Object.freeze()` or `Object.seal()` to make prototypes immutable where possible, but verify this does not break your dependencies.
  5. In Node.js environments, consider using the `--disable-proto=delete` flag to remove the dangerous `__proto__` property as an additional defense layer.
  6. Avoid assigning or modifying the `__proto__` or `constructor.prototype` properties dynamically in your code or dependencies.

reason: >
  Prototype Pollution vulnerabilities allow attackers to tamper with object prototypes, leading to critical security risks including privilege escalation and remote code execution.

references:
  - https://portswigger.net/web-security/prototype-pollution
  - https://learn.snyk.io/lessons/prototype-pollution/javascript/
```