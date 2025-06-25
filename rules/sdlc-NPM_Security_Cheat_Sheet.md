---
trigger: glob
globs: [package.json, npmrc, yarn.lock]
---

rule: npm_security_best_practices

  Ensure npm package security by following these best practices:

  1. Never publish secrets (API keys, passwords). Use `.gitignore` and `.npmignore` properly; prefer the `files` whitelist in package.json. Always run `npm publish --dry-run` before publishing.
  2. Enforce lockfile consistency by using `npm ci` in CI/builds or `yarn install --frozen-lockfile` to avoid unintended dependency changes.
  3. Minimize risks from install-time scripts:
     - Vet third-party packages for credibility.
     - Avoid immediate upgrades; review changelogs.
     - Use `npm install --ignore-scripts` or set `ignore-scripts=true` in `.npmrc`.
  4. Continuously audit dependencies with vulnerability scanners and `npm outdated` / `npm doctor` to monitor health and updates.
  5. Use a private/local npm proxy (e.g., Verdaccio) to gain control of package sources and caching.
  6. Enable 2FA (`auth-and-writes` mode) on your npm account to protect publishing and token management.
  7. Manage npm tokens with least privilege, revoke unused tokens, and never expose them in repos or logs.
  8. Be alert to typosquatting by verifying package names (`npm info <package>`) and avoid trusting unknown scripts.
  9. Follow responsible vulnerability disclosure practices by coordinating privately before public disclosure.

  Adhering to these guidelines helps secure your npm packages, dependencies, and development environment.
