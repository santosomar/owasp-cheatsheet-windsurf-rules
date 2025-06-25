```yaml
---
trigger: glob
globs: [tf, yaml, yml, json, js, py, java, go, cfg, conf, sh]
---
id: cloud-architecture-security-best-practices
name: Cloud Architecture Security Best Practices
description: |
  Enforce critical security controls in cloud architectures based on OWASP guidance:
  risk analysis, network segmentation, IAM least privilege, trust model balance,
  WAF and DDoS protection, robust logging/monitoring, and shared responsibility clarity.
severity: high
tags: [cloud, architecture, security, iam, network, waf, ddos, logging]

message: |
  Review your cloud architecture and code for:

  1. Risk analysis & threat modeling guiding design and controls.
  2. Avoid hardcoded credentials; apply least privilege IAM policies.
  3. Separate public/private components using VPCs and subnets.
  4. Define and enforce trust boundaries; never trust user input directly.
  5. Deploy and customize WAF rules; implement rate limiting.
  6. Enable logging with traceability and mask sensitive data.
  7. Leverage managed DDoS protections alongside WAF.
  8. Understand cloud shared responsibility boundaries.
  9. Automate patching of self-managed components.
 10. Secure authentication, authorization, and dependencies even in managed services.

recommendation: |
  - Conduct formal risk assessments and document threat models early.
  - Use IAM roles and policies instead of static credentials; rotate keys regularly.
  - Architect networks to isolate sensitive resources in private subnets.
  - Validate and authorize all inputs at entry points; apply a balanced zero-trust approach.
  - Configure managed WAF with custom rules tailored to your app; apply rate limits.
  - Implement comprehensive logging, tracing, and baseline anomaly detection.
  - Enable cloud provider's DDoS mitigation features appropriate to risk level.
  - Regularly review your cloud provider’s shared responsibility docs and your coverage.
  - Automate updates for OS/images and maintain inventory of self-managed tooling.
  - Continuously patch app code and dependencies; audit access controls diligently.

examples:
  - Avoid:
      - Hardcoded cloud credentials or overly permissive IAM policies
      - Public bucket policies exposing sensitive files
      - Placing databases in public subnets accessible from the internet
      - Accepting user input without validation or authentication checks
  - Prefer:
      - IAM roles with least privilege for object storage access
      - Architecture isolating frontend and backend with strict subnet rules
      - Using signed URLs for limited, expiring access to non-sensitive assets
      - Using managed WAF with tailored rules and rate limits
      - Comprehensive HTTP request logging with PII masked
      - Automated patching pipelines for your container images and VMs
      - Configuring cloud DDoS protections (e.g., AWS Shield, GCP Cloud Armor)

references:
  - https://cheatsheetseries.owasp.org/cheatsheets/Cloud_Architecture_Security_Cheat_Sheet.html
  - https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html
  - https://cloud.google.com/armor/docs/security-policy-overview
  - https://docs.microsoft.com/en-us/azure/architecture/framework/security/
```