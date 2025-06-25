```yaml
---
trigger: glob
globs: [Dockerfile]
---

id: secure-nodejs-docker-container
message: |
  Ensure your Node.js Docker container follows best security practices:
  - Pin base image exactly by tag and SHA256 digest (e.g. FROM node:lts-alpine@sha256:...).
  - Prefer minimal base images like node:lts-alpine to reduce attack surface.
  - Install only production deps using `npm ci --omit=dev` for deterministic, lean installs.
  - Set environment variable NODE_ENV=production to enable production optimizations.
  - Avoid running the container as root: use `COPY --chown=node:node` and `USER node`.
  - Run your app process directly with a minimal init (e.g., dumb-init) to handle signals properly:
    ```
    RUN apk add dumb-init
    CMD ["dumb-init", "node", "server.js"]
    ```
  - Implement graceful shutdown handlers in app code monitoring SIGINT/SIGTERM to close resources.
  - Use multi-stage builds to separate build/runtime, minimize image size and avoid embedding secrets.
  - Use .dockerignore to exclude node_modules, .git, .npmrc and other sensitive/unnecessary files.
  - Use Docker BuildKit secrets to mount credentials securely during build (`RUN --mount=type=secret`).
  - Regularly scan your images for vulnerabilities and update dependencies accordingly.

recommendation: |
  Follow these practices to build secure, efficient, and maintainable Node.js Docker images ready for production deployments.
  Review your Dockerfile and CI/CD pipelines to enforce these rules and automate scanning.

severity: medium
patterns:
  - pattern-either:
      - pattern: |
          FROM node:*  # missing digest pin
      - pattern-not: |
          FROM node:*@sha256:*  # no digest in FROM
  - pattern-not: |
      ENV NODE_ENV production
  - pattern-not: |
      RUN npm ci --omit=dev
  - pattern: |
      USER root
  - pattern-not: |
      USER node
  - pattern: |
      CMD npm start
  - pattern-not: |
      CMD ["dumb-init", "node", ...]
  - pattern-not: |
      COPY --chown=node:node *
  - pattern-not: |
      # Use multi-stage build with at least two FROM nodes
  - pattern-not: |
      # .dockerignore excluding node_modules, .git, .npmrc
  - pattern-not: |
      RUN --mount=type=secret
  - pattern-not: |
      # evidence of scanning steps (CI config, or comments)
```
