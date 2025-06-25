---
trigger: glob
globs: [js,ts,java,cs,py,go,rb,swift,kt,yaml,yml,json]
---

OWASP Secrets Management Best Practices

Avoid hardcoding secrets (API keys, tokens, passwords) directly in source code or config files.
Use a centralized, standardized secrets management solution to store and access all secrets securely.
Ensure secrets are transmitted only over encrypted channels (e.g., TLS) and stored encrypted at rest.
Implement fine-grained, least-privilege access controls so each user or service accesses only necessary secrets.
Automate secret lifecycle: creation, rotation, revocation, and secure deletion to reduce human error and exposure.
Prefer dynamic, short-lived secrets over static credentials where possible.
Secure secrets in memory by zeroing out after use and, for managed languages, use secure types (e.g., SecureString).
In CI/CD pipelines, avoid persisting long-lived secrets; scope credentials tightly and prevent secrets leaking in logs.
For containers/orchestration, inject secrets at runtime (e.g., mounted volumes, sidecars), not baked into images or environment variables.
Integrate secrets detection tools early (pre-commit hooks, IDE plugins, CI scans) to prevent leaks before deployment.
Maintain and monitor detailed audit logs of secret access, modifications, and revocations to detect suspicious activity.
Prepare and regularly test documented incident response plans for secret exposure, including rapid rotation and revocation.
When operating multi-cloud or hybrid environments, unify secrets management solutions and enforce consistent policies.

Actionable Developer Checklist:
- Never commit secrets into source code or repositories.
- Use environment-specific secrets managers (cloud-native or third-party).
- Automate secret rotation and secure audit logging.
- Secure secrets in memory and minimize their lifespan.
- Harden CI/CD and container environments against secret leaks.
- Detect secrets early during development.
- Plan for incidents and practice response.
