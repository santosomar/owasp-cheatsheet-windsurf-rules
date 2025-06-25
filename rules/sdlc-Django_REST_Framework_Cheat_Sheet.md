```yaml
---
trigger: glob
globs: [.py, .yaml, .yml]
---

# DRF Security Best Practices Rule

This rule advises on critical security practices when developing Django REST Framework APIs to protect against common risks:

- **Authentication & Authorization**  
  - Always set `DEFAULT_AUTHENTICATION_CLASSES` with appropriate authentication schemes for all non-public endpoints.  
  - Never leave `DEFAULT_PERMISSION_CLASSES` as `AllowAny`; explicitly restrict access using proper permission classes.  
  - When overriding `get_object()`, always call `self.check_object_permissions(request, obj)` to enforce object-level access control.  
  - Avoid per-view overrides of authentication, permission, or throttle classes unless fully confident in their implications.

- **Data Exposure & Mass Assignment**  
  - In serializers, specify explicit `fields = [...]` allowlists; do not use `exclude`.  
  - In ModelForms, always use `Meta.fields` allowlist instead of `Meta.exclude` or `"__all__"` to prevent unauthorized field updates.

- **Rate Limiting & Throttling**  
  - Configure `DEFAULT_THROTTLE_CLASSES` to enable API rate limiting as a DoS defense layer.  
  - Prefer to enforce rate limiting at the gateway or WAF level; DRF throttling is a last-resort safeguard.

- **Security Configuration**  
  - Ensure `DEBUG` and `DEBUG_PROPAGATE_EXCEPTIONS` are set to `False` in production environments.  
  - Never hardcode secrets such as `SECRET_KEY`; inject them via environment variables or secrets managers.  
  - Disable all unused or dangerous HTTP methods (e.g., PUT, DELETE) at the API level.  
  - Validate, sanitize, and filter all incoming data rigorously.

- **Prevent Injection Attacks**  
  - Avoid raw SQL queries with user input; use ORM or parameterized queries exclusively.  
  - For YAML parsing, use safe loaders (`yaml.SafeLoader`); never parse YAML or pickle data from untrusted sources.  
  - Do not use `eval()`, `exec()`, or similar dynamic code execution functions on user input.

- **Asset & Version Management**  
  - Maintain an up-to-date inventory of APIs, including host info, versions, environments, access controls, and configurations.

- **Logging & Monitoring**  
  - Log authentication failures, authorization denials, and validation errors with enough context to detect suspicious activity.  
  - Avoid logging sensitive data (passwords, tokens, PII).  
  - Use structured logging compatible with SIEM tools, ensuring data integrity and confidentiality.  
  - Implement continuous monitoring and alerting to detect incidents early.

- **Business Logic & Secret Management**  
  - Apply threat modeling, code reviews, pair programming, and unit testing to reduce business logic flaws.  
  - Manage secrets securely using dedicated managers; never hardcode secrets in code.

- **Dependency Management**  
  - Regularly audit and promptly update dependencies following security advisories.  
  - Assess security posture of libraries before adoption (active maintenance, vulnerability history).

- **Static Analysis Tools**  
  - Use tools like Bandit, Semgrep, and IDE security plugins to detect security issues early in the development lifecycle.

**Summary:**  
Always enforce strict authentication and authorization, minimize data exposure, validate inputs, implement rate limiting, configure secure settings, avoid injection risks, maintain asset inventories, ensure robust logging and monitoring, secure secrets, keep dependencies updated, and leverage static analysis tools. Follow OWASP API Security Top 10 to build secure Django REST Framework APIs.
```