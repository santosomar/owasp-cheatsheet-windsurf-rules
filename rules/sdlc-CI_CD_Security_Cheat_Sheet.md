```yaml
---
trigger: glob
globs: [yaml,yml,json,groovy,sh,ps1,tf,dockerfile,gradle,xml,ini]
---

rule: "Secure Your CI/CD Pipeline and Supply Chain"

description: |
  This rule guides developers on securing CI/CD pipelines following OWASP best practices,
  reducing risks from pipeline compromise, credential abuse, and supply chain attacks.

recommendations:
  - Enforce strict code reviews and disable auto-merge in SCM; enable protected branches,
    commit signing, and MFA to prevent unauthorized changes.
  - Integrate automated scanning (SAST, DAST, IaC security tools) in your pipeline configuration
    to detect vulnerabilities early.
  - Never hardcode secrets or credentials in code or pipeline config files; use dedicated
    secret management solutions and ensure secrets are encrypted and never logged.
  - Apply the principle of least privilege to all pipeline identities, agents, and secrets,
    avoiding shared credentials and granting minimal permissions needed.
  - Pin all dependencies with version locks and validate package integrity using hashes or checksums.
    Prefer private registries and scoped packages to prevent dependency confusion.
  - Vet and restrict third-party plugins and extensions in your CI/CD platform; keep them updated
    and remove those unused to reduce attack surface.
  - Sign commits, artifacts, and pipeline configurations using code signing tools (e.g., Sigstore)
    and consider frameworks like in-toto or SLSA for supply chain integrity.
  - Centralize and structure pipeline logs (e.g., JSON format), avoid logging sensitive data,
    and set up monitoring and alerting to detect anomalies quickly.
  - Restrict network access to CI/CD servers and isolate build environments to limit attacker movement.
  - Maintain up-to-date access inventories, use centralized identity providers, enforce MFA,
    and promptly deprovision unused accounts or excessive privileges.

rationale: |
  CI/CD pipelines are a high-value target due to their elevated privileges and
  influence over software delivery. Following these actions limits attack vectors,
  ensures integrity and accountability, and secures the continuous delivery process.
```