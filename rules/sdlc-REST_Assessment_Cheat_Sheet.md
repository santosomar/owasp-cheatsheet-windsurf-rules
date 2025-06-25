---
trigger: glob
globs: [js,ts,java,py,rb,go,cs,json,xml,conf,yml,yaml]
---

  Follow these best practices when developing or testing RESTful web services to ensure secure, effective assessment and improve overall security posture:

  - Use standard HTTP methods (GET, POST, PUT, DELETE) appropriately to align with REST principles.
  - Clearly document all REST endpoints, parameters (URL segments, headers, request body), and expected data formats (JSON, XML).
  - Recognize that many parameters may be embedded in URL paths or custom headers rather than just query strings.
  - Collect full HTTP requests (including headers and body) using a capable proxy tool to uncover the full attack surface.
  - Analyze variable URL path segments and abnormal headers to identify undocumented parameters for security testing.
  - When fuzzing parameters, focus on borderline invalid inputs informed by observed valid values to optimize testing effort.
  - Identify and understand custom authentication tokens/mechanisms as standard session tracking tools may not be effective.
  - Gain access to source code, configuration, or developer guides wherever possible for more comprehensive coverage.
  - Verify suspected URL path parameters by testing invalid values and observing server vs. application-level error responses.
  - Consider adopting or providing formal service descriptions (WADL, WSDL 2.0) or developer guides to ease assessment.
  - Always emulate the authentication mechanisms properly during security testing to avoid false negatives.

