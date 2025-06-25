
---
trigger: glob
globs: [Dockerfile, yml, yaml, sh, k8s, kubernetes]
---

Follow these critical Docker container security best practices to reduce risk:

  1. Run containers as non-root users:
     - Use `USER` directive in Dockerfiles or `docker run -u`.
     - In Kubernetes, set `securityContext.runAsUser`.
  
  2. Never expose the Docker daemon socket (`/var/run/docker.sock`) to containers or external networks, avoid TCP socket exposure.
  
  3. Drop all unnecessary Linux capabilities (`--cap-drop all`) and add only minimal required; never use `--privileged`.
     In Kubernetes, control capabilities via `securityContext.capabilities`.
  
  4. Prevent privilege escalation by enabling `--security-opt=no-new-privileges`.
     Set `allowPrivilegeEscalation: false` in Kubernetes pods.
  
  5. Enforce resource limits (CPU, memory, processes) to prevent DoS attacks.
  
  6. Use read-only root filesystems (`--read-only`), mount volumes read-only (`:ro`), and prefer `--tmpfs` for writable temp storage.
  
  7. Enable and do not disable Linux security modules (seccomp, AppArmor, SELinux) and use their default profiles.
  
  8. Implement network segmentation:
     - Docker: avoid default bridge networking, use custom networks.
     - Kubernetes: enforce Network Policies.
  
  9. Integrate container image scanning (Trivy, Clair, Snyk) and linting in your CI/CD pipeline.
  
  10. Manage secrets securely using Docker Secrets or Kubernetes encrypted secrets; avoid baking sensitive info into images or environment variables.
  
  11. Keep the host OS kernel, Docker Engine, and related dependencies regularly updated.
  
  12. Consider running Docker in rootless mode or use Podman for enhanced security.
  
  13. Maintain Docker daemon logging level at `info` unless `debug` is necessary.
