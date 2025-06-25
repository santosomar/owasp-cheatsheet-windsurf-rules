---
trigger: glob
globs: [java, js, py, php, rb, go, cs, sql, ldap, sh, bat]
---


  Injection flaws occur when untrusted input alters commands or queries.
  Follow best practices to prevent injection vulnerabilities across SQL, LDAP, and OS commands.

patterns:
  - pattern: '" + $UNTRUSTED + "'
    message: Avoid string concatenation with untrusted input to build queries or commands. Use parameterized APIs instead.
  - pattern-inside: |
      PreparedStatement ps = connection.prepareStatement($QUERY);
      ps.setString($IDX, $INPUT);
    message: Use prepared statements or parameterized queries to separate code from data.
  - pattern-inside: |
      CallableStatement cs = connection.prepareCall($PROC);
      cs.setString($IDX, $INPUT);
    message: Use stored procedures safely with parameters; avoid dynamic SQL inside procedures.
  - pattern-inside: |
      ProcessBuilder pb = new ProcessBuilder($CMD_WITH_ARGS);
    message: Use APIs that separate commands and arguments to avoid OS command injection.
  - pattern-inside: |
      ldapFilter = "(" + $UNTRUSTED + ")";
    message: Escape LDAP inputs correctly; do not insert raw untrusted data into LDAP queries.
  - pattern: $INPUT =~ /[&|;$><\\\s!]+/  # detect suspicious chars in user input going to commands
    message: Reject or strictly validate user input containing dangerous characters before using in commands.
  - pattern: |
      $INPUT =~ /^[a-z0-9]{3,10}$/
    message: Apply allow-list input validation for all parameters, especially when parameterization isn't possible.

fix: |
  - Always prefer parameterized queries, prepared statements, and safe API calls over string concatenation.
  - Validate all inputs with positive (allow-list) checks and perform canonicalization.
  - Escape user input contextually with interpreter-specific escaping if parameterization is not feasible.
  - Use LDAP escaping functions for DN and filter values.
  - Use ProcessBuilder or equivalent API passing command and args separately; avoid shell string concatenation.
  - Regularly scan and test your code with tools like SQLMap and OWASP ZAP.
  - For legacy or closed source apps where fixes are impractical, consider virtual patching and active monitoring.

---
```