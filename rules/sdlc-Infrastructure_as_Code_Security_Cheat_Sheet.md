```yaml
---
trigger: glob
globs: [tf, tfvars, yml, yaml, json, sh, dockerfile]
---
rule: |
  Infrastructure as Code (IaC) Security Best Practices

  1. Manage Secrets Securely
     - Never commit secrets (tokens, passwords, SSH keys) in plain text or in source control.
     - Use secret management tools and scanners (e.g., truffleHog, git-secrets) to detect exposed secrets early.

  2. Enforce Principle of Least Privilege
     - Restrict who can create/update/delete IaC scripts.
     - Limit resource permissions created by IaC to the minimum necessary.

  3. Integrate Security Early 
     - Use IDE plugins (TFLint, Checkov) and static analysis tools (Snyk, kubescan) to identify risks during development.
     - Leverage open source dependency and container image scanners (BlackDuck, Trivy) in your pipeline.

  4. Version Control Best Practices
     - Track all IaC changes with feature branches/merge requests.
     - Keep infrastructure changes tied to the relevant application feature code to maintain traceability.

  5. Tag and Manage Inventory Properly
     - Label all resources on deployment to avoid “ghost” resources that cause security, observability, and cost issues.
     - Ensure secure decommissioning of resources by erasing configs and data.

  6. Automate Security Checks in CI/CD
     - Incorporate IaC security analysis in your pipelines for continuous compliance.
     - Use consolidated reporting tools (DefectDojo, OWASP Glue) to monitor security status.

  7. Embrace Immutable Infrastructure
     - Avoid manual changes to live infrastructure; deploy new versions instead.
  
  8. Enable Logging and Monitoring
     - Consistently enable security and audit logs for infrastructure.
     - Use monitoring tools (Prometheus, ELK) and runtime threat detection (Falco) to detect anomalous behavior.

By following these actionable best practices, you strengthen your IaC security posture, reduce risk exposure, and enable safe, repeatable infrastructure deployments.
```