---
trigger: glob
globs: [.js, .ts, .jsx, .tsx, .graphql, .gql]
---


name: OWASP GraphQL Security Best Practices

  Ensure your GraphQL API follows OWASP recommended security controls to prevent injection, DoS, unauthorized access, and information leakage.

patterns:
  - pattern: |
      $INPUT = $VALUE
      where NOT isValidGraphQLInput($VALUE)
    
      Validate all incoming GraphQL inputs using allowlists (scalar types, enums, custom validators). Reject invalid inputs gracefully without exposing internal errors.
    level: error

  - pattern: |
      userInput === $VULN
      where isUsedInSensitiveSink($VULN)
    
      Avoid using user input directly in SQL/NoSQL queries or system commands. Use parameterized queries or safe APIs to eliminate injection risks.
    level: error

  - pattern: |
      queryDepth($QUERY) > $MAX_DEPTH
    
      Enforce query depth limits to mitigate DoS attack vectors caused by deeply nested queries.
    level: warning

  - pattern: |
      requestedAmount($FIELD) > $MAX_ALLOWED
    
      Limit the number of items requested per field and implement pagination to prevent excessive data fetching.
    level: warning

  - pattern: |
      batchQuery($BATCH) && isSensitiveQuery($BATCH)
    
      Limit or disable batching on sensitive queries. Implement server-side limits on batch size and concurrent operations to prevent enumeration and brute force attacks.
    level: warning

  - pattern: |
      !hasAccessControl($RESOLVER)
    
      Enforce strict authorization checks on all queries and mutations. Verify object-level permissions to prevent BOLA/IDOR vulnerabilities.
    level: error

  - pattern: |
      introspectionEnabled() && isProduction()
    
      Disable or restrict GraphQL introspection and tools like GraphiQL in production to reduce schema exposure.
    level: warning

  - pattern: |
      verboseErrorsEnabled() && isProduction()
    
      Mask error messages and stack traces in production environments to avoid leaking internal implementation details.
    level: warning

actions:
  - action: addValidator
    description: Add or enforce strict allowlist input validation using GraphQL scalars and enums.
  - action: implementQueryLimits
    description: Implement query depth, field amount, pagination, and cost analysis limits.
  - action: applyAuthChecks
    description: Add authentication and authorization on all resolvers, validating access to each requested object.
  - action: disableIntrospection
    description: Turn off GraphQL introspection and GraphiQL in production/public APIs.
  - action: enableErrorMasking
    description: Configure server to mask detailed error messages in client responses.
  - action: configureBatchingLimits
    description: Restrict or disable query batching for sensitive data and limit batch operation concurrency.
  - action: enforceResourceLimits
    description: Apply OS/container-level resource limits (memory, CPU) to protect API from resource exhaustion.

notes: |
  Follow OWASP GraphQL Cheat Sheet guidelines to secure your API from injection, DoS, authorization bypass, and information disclosure.
  Regularly audit your schema for overexposure and access control gaps.
```