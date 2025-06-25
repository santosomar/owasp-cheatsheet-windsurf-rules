---
trigger: glob
globs: [yaml,yml,json,sh,Dockerfile]
---



  Enforce Kubernetes security best practices throughout the container lifecycle to minimize attack surface and mitigate risks. Focus on secure image management, strict RBAC, pod security contexts, network segmentation, secrets protection, runtime monitoring, and cluster component hardening.


enforce:
  - Build Phase:
      - Use only signed, scanned, minimal base container images from private registries.
      - Integrate vulnerability scanning in CI and block known vulnerable images.
      - Remove shells and package managers to reduce attack surface.

  - Deploy Phase:
      - Apply RBAC policies granting least privilege; avoid privileged service accounts.
      - Configure `securityContext` in Pod specs:
          - Run containers as non-root (`runAsNonRoot: true` or `runAsUser` > 0).
          - Use read-only root filesystems.
          - Drop all unnecessary Linux capabilities.
      - Isolate workloads using Kubernetes namespaces.
      - Use NetworkPolicies to restrict pod-to-pod and external connectivity.
      - Protect secrets:
          - Store secrets separately, encrypted at rest.
          - Mount secrets as read-only volumes.
          - Consider external secrets managers/vaults.
      - Enforce pod security standards using Pod Security Admission Controller with at least 'baseline' or preferably 'restricted' profile.
      - Use admission controllers like ImagePolicyWebhook for image provenance.
      - Define resource quotas per namespace to limit resource abuse.
      - Employ centralized policy enforcement tools (e.g., OPA, Kyverno).

  - Runtime Phase:
      - Monitor container behavior with runtime security tools (Falco, etc.) to detect anomalies.
      - Use sandboxed container runtimes (gVisor, Kata Containers) to isolate pods from host kernel.
      - Continuously monitor and tighten network policies based on traffic patterns.
      - Automate credential and token rotation; revoke bootstrap tokens promptly.
      - Have remediation plans ready, e.g., scaling down compromised pods.

  - Kubernetes Components:
      - Keep Kubernetes and all components up to date with security patches.
      - Secure etcd with mutual TLS and firewall restrictions.
      - Limit API server access to trusted sources, use strong authentication (OIDC, cloud IAM).
      - Protect Kubelets with authentication/authorization; avoid unauthenticated access.
      - Lock down Kubernetes Dashboard behind authenticating reverse proxies with MFA.

  - Logging & Auditing:
      - Enable Kubernetes audit logging with focused policies on sensitive events.
      - Collect and centralize container logs using stdout/stderr and log rotation.
      - Integrate logs and alerts with external monitoring and incident response systems.
      - Regularly review logs and cluster events for suspicious activities.

recommendation: |
  - Always embed security early across the build, deploy, and runtime stages.
  - Prefer native Kubernetes security controls and admission controllers over ad hoc solutions.
  - Prioritize fixing vulnerabilities based on severity, exposure, and environment criticality.
  - Carefully assess service mesh adoption benefits against complexity and operational cost.

actionable_advice: |
  - Configure your CI pipelines to scan and block vulnerable or unsigned container images.
  - Define and enforce least privilege RBAC policies; audit existing roles & bindings regularly.
  - Set securityContext on all pods to avoid running as root and harden container filesystems.
  - Implement namespaces and NetworkPolicies to segment workloads effectively.
  - Store secrets securely with encryption; avoid baking them in images or config files.
  - Enable audit logging and implement real-time monitoring for container behaviors.
  - Automate credential rotation to minimize exposure window.
  - Use admission controllers like ImagePolicyWebhook and Pod Security Admission to enforce compliance.
  - Monitor and patch Kubernetes components regularly to protect cluster integrity.

