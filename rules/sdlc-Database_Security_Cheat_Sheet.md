```yaml
---
trigger: glob
globs: [sql, properties, yml, yaml, json, conf, config, env]
---

title: Secure Database Access and Credential Management

description: |
  Ensure your application follows best practices to securely connect and interact with databases,
  protecting credentials, enforcing least privilege, and securing the database environment.

when: | 
  # Detect usage of database connection strings, credentials, or config files
  # Or SQL scripts used for deployment or initialization.

rules:
  - id: no-hardcoded-db-credentials
    pattern: 
      - pattern-either:
          - pattern: '"password=*"'  # generic pattern in config files or code
          - pattern: 'password: *'
          - pattern: 'PASSWORD=*'
          - pattern: /(["'])?pass(word)?(["'])?\s*=\s*["']?[^"'\s]+["']?/
    message: >
      Avoid hardcoding database credentials in source code. Store credentials securely
      in protected configuration files outside the web root with strict permissions, or use secrets management tools.
    level: error

  - id: require-tls-for-db-connections
    pattern: 
      - pattern-inside: |
          connection.*(encrypt|ssl|tls)
      - pattern-not: /(encrypt|ssl|tls).*false/i
    message: |
      Configure your database connections to enforce TLS encryption (TLS 1.2 or higher).
      Use trusted certificates and verify server identity to protect data in transit.
    level: warning

  - id: least-privilege-db-accounts
    message: |
      Use dedicated database accounts per application or service with minimal permissions (e.g., only SELECT, UPDATE, DELETE).
      Avoid using highly privileged accounts (root, sa) and do not grant owner or admin roles to app accounts.
      Review and remove unused accounts regularly.
    level: warning

  - id: avoid-direct-db-access-from-clients
    message: |
      Never allow untrusted clients to access the database backend directly.
      Always route database access through an API layer to enforce security policies.
    level: error
    languages: [general]  # Applies broadly

  - id: secure-db-configuration-files
    message: |
      Store database credentials in configuration files located outside web root directories.
      Restrict file permissions to prevent unauthorized access.
      Use built-in encryption for config files where available.
    level: warning

  - id: database-server-hardened
    message: |
      Ensure your database server is regularly patched, runs with least privilege OS accounts, and default/sample data or accounts are removed.
      Separate data and log files on distinct disks and use encrypted backups.
      Follow vendor-specific hardening recommendations (e.g., disable xp_cmdshell on MSSQL, run mysql_secure_installation on MySQL).
    level: warning
    languages: [general]

best_practices:
  - "Isolate the database backend network access; bind to localhost or use local sockets."
  - "Use firewall rules and network segmentation to restrict DB connectivity."
  - "Enable and enforce TLS encryption for all database connections."
  - "Use strong, unique passwords and prefer integrated authentication methods."
  - "Never hardcode credentials; secure them using vaults or protected config files."
  - "Grant minimal permissions needed per app, avoid admin/root-level access."
  - "Regularly audit database accounts and permissions, removing unused ones promptly."
  - "Follow official security hardening guidelines for your specific database platform."
  - "Avoid direct database connections from clients; always use an application API layer."
```