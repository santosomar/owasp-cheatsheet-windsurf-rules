---
trigger: glob
globs: [js, ts, java, py, rb, php, go, cs, scala, swift]
---

Denial of Service (DoS) Resilience and Mitigation

  Implement layered DoS defenses by validating inputs early, avoiding expensive operations,
  managing sessions efficiently, and applying rate limits to protect application resources.
  Collaborate with infrastructure teams to ensure network-level redundancies and filtering.



patterns:
  - pattern-either:
      - pattern: |
          if (...) {
            // expensive operation without prior cheap validation
          }
      - pattern-inside: |
          session.setTimeout(...)
      - pattern-regex: '(upload|file).*(size|limit)'
      - pattern-regex: '(rate|limit|timeout|bandwidth)'
      - pattern-regex: 'try\s*{.*}\s*catch\s*\(.*\)\s*{.*}'


  // Follow these best practices to mitigate DoS risks:
  1. Validate inputs using cheap resource checks before costly processing to avoid early resource exhaustion.
  2. Use asynchronous, non-blocking operations for tasks that may take long execution times.
  3. Implement robust exception handling to prevent catastrophic failures during high load.
  4. Design stateless or redundant components and apply bulkheading to avoid single points of failure.
  5. Limit session duration via inactivity and absolute timeouts; minimize data stored per session.
  6. Restrict file upload sizes and allowed extensions to prevent resource overuse.
  7. Apply rate limiting (requests per user/IP, bandwidth, connection timeouts) to throttle abusive traffic.
  8. Collaborate with network/infrastructure to implement caching, redundant links, and ISP-level filtering.
  9. For large-scale attacks, consider cloud or commercial DDoS mitigation services compliant with data protection laws.
