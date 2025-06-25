---
trigger: glob
globs: [sql, properties, yml, yaml, json, conf, config, env]
---

Secure Database Access and Credential Management


  Ensure your application follows best practices to securely connect and interact with databases,
  protecting credentials, enforcing least privilege, and securing the database environment.

Detect usage of database connection strings, credentials, or config files
Or SQL scripts used for deployment or initialization.

    pattern: 
      - pattern-either:
          - pattern: '"password=*"'  # generic pattern in config files or code
          - pattern: 'password: *'
          - pattern: 'PASSWORD=*'
          - pattern: /(["'])?pass(word)?(["'])?\s*=\s*["']?[^"'\s]+["']?/

      Avoid hardcoding database credentials in source code. Store credentials securely
      in protected configuration files outside the web root with strict permissions, or use secrets management tools.
    level: error


    pattern: 
      - pattern-inside: |
          connection.*(encrypt|ssl|tls)
      - pattern-not: /(encrypt|ssl|tls).*false/i

      Configure your database connections to enforce TLS encryption (TLS 1.2 or higher).
      Use trusted certificates and verify server identity to protect data in transit.
    level: warning


      Use dedicated database accounts per application or service with minimal permissions (e.g., only SELECT, UPDATE, DELETE).
      Avoid using highly privileged accounts (root, sa) and do not grant owner or admin roles to app accounts.
      Review and remove unused accounts regularly.
    level: warning

  - 

      Never allow untrusted clients to access the database backend directly.
      Always route database access through an API layer to enforce security policies.
    level: error
    languages: [general]  # Applies broadly

  - 

      Store database credentials in configuration files located outside web root directories.
      Restrict file permissions to prevent unauthorized access.
      Use built-in encryption for config files where available.
    level: warning

  - 

      Ensure your database server is regularly patched, runs with least privilege OS accounts, and default/sample data or accounts are removed.
      Separate data and log files on distinct disks and use encrypted backups.
      Follow vendor-specific hardening recommendations (e.g., disable xp_cmdshell on MSSQL, run mysql_secure_installation on MySQL).


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
