---
trigger: glob
globs: [.js,.ts,.java,.py,.go,.rb,.cs,.php,.json,.yaml,.yml,.xml]
---

This rule highlights critical REST API security measures developers must implement,
  including HTTPS enforcement, access control, JWT handling, input validation, 
  method restrictions, and secure error handling.



check:
  any_of:
     1. Ensure HTTPS usage - discourage plain HTTP URLs or HTTP server configs
    - pattern-inside: |
        http://
    - pattern: |
        server.use_http()
    - pattern: |
        httpServer.listen(
    
     2. Access control per API endpoint (presence of auth checks in handlers)
    - pattern-inside: |
        if (!auth || !checkAccess(...
    - pattern-inside: |
        validateToken(
    - pattern-inside: |
        authorize(
    
     3. JWT usage & validation common patterns
    - pattern-inside: |
        jwt.verify(token, ...)
    - pattern-inside: |
        jwt.decode(token, { complete: true, ... })
    - pattern-inside: |
        if (token.header.alg == 'none')
    - pattern-inside: |
        validateClaims(token.payload.iss, token.payload.aud, token.payload.exp, token.payload.nbf)
    
     4. API key usage and rate limiting
    - pattern-inside: |
        checkApiKey(...)
    - pattern-inside: |
        rateLimiter(...)
    - pattern-inside: |
        revokeApiKey(...)
    
     5. HTTP method allowlisting and response on disallowed methods
    - pattern-inside: |
        if (method not in allowedMethods)
        return 405
    - pattern-inside: |
        router.method('GET', ...)
    
     6. Input validation and filtering
    - pattern-inside: |
        validateInput(...)
    - pattern-inside: |
        if (input.length > MAX_LENGTH)
    - pattern-inside: |
        if (!regex.test(input))
    
     7. Content-Type strict validation for requests and responses
    - pattern-inside: |
        if (contentType !== 'application/json')
        return 415
    - pattern-inside: |
        response.headers['Content-Type'] = 'application/json'
    
     8. Management endpoint protection
    - pattern-inside: |
        if (isManagementEndpoint(path))
        requireMfaAuth()
    
     9. Generic error message handling
    - pattern-inside: |
        catch (error)
        return genericErrorMessage()
    
     10. Audit logging of security events
    - pattern-inside: |
        logSecurityEvent(...)
    - pattern-inside: |
        sanitizeLogData(...)
    
     11. Security HTTP headers enforced
    - pattern-inside: |
        response.setHeader('Cache-Control', 'no-store')
    - pattern-inside: |
        response.setHeader('Content-Security-Policy', "frame-ancestors 'none'")
    - pattern-inside: |
        response.setHeader('Strict-Transport-Security', ...)
    - pattern-inside: |
        response.setHeader('X-Content-Type-Options', 'nosniff')
    - pattern-inside: |
        response.setHeader('X-Frame-Options', 'DENY')
    
     12. CORS configuration checks
    - pattern-inside: |
        corsOrigin != '*'
    - pattern-inside: |
        corsDisabled == true
    
     13. Sensitive data in URL prevention
    - pattern-inside: |
        if (url contains 'password' || 'token' || 'apikey')
    
     14. Proper HTTP status code usage
    - pattern-inside: |
        return 401
    - pattern-inside: |
        return 403
    - pattern-inside: |
        return 405
    - pattern-inside: |
        return 429

fix: |
  - Always host APIs exclusively via HTTPS; configure servers and clients accordingly.
  - Enforce authorization checks on every API endpoint; do not rely on global session state.
  - Use JWT tokens securely: verify signatures, reject tokens with `alg: none`, validate claims, and implement token revocation.
  - Protect public endpoints with API keys plus rate limiting; revoke keys if abused.
  - Allow only required HTTP methods on each endpoint; reject others with 405 responses.
  - Validate all client inputs: check length, type, format, and ranges. Reject invalid or oversized input.
  - Strictly validate and enforce Content-Type headers on requests and responses; reject unsupported types.
  - Protect management endpoints with strong, multi-factor authentication and restrict network access.
  - Return generic error messages; never expose stack traces or internal errors to clients.
  - Log security-related events safely; sanitize logs to prevent injection.
  - Include essential security headers (`Cache-Control: no-store`, `Content-Security-Policy: frame-ancestors 'none'`, `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`) in all responses.
  - Disable CORS unless required; if enabled, restrict allowed origins as tightly as possible.
  - Do not pass sensitive data via URL paths or query parameters; use headers or POST/PUT bodies instead.
  - Use semantically correct HTTP status codes for authentication, authorization, method, and rate-limiting issues to aid clients.