---
trigger: glob
globs: [java, cs, sql, py, js, ts, php, rb, go]
---

Prevent SQL Injection by Using Safe Query Practices

  Ensure your database access code is protected against SQL injection vulnerabilities by following these best practices.
details: |
  1. **Use Prepared Statements / Parameterized Queries**  
     Always define SQL with placeholders and bind user inputs as parameters. Avoid building queries via string concatenation with user input.

  2. **Safe Stored Procedures**  
     Use stored procedures only if inputs are parameterized and no dynamic SQL from user input is involved. Assign minimal execute permissions to the application DB user.

  3. **Strict Allow-listing for SQL Identifiers**  
     When user input controls table names, column names, or order clauses, map inputs against a hard-coded allow-list to prevent injection.

  4. **Avoid Relying on Escaping Alone**  
     Escaping is error-prone and database-specific; do not depend on it as your sole defense.

  5. **Enforce Least Privilege Principles**  
     Use database accounts with the least permissions necessary. Avoid admin-level accounts in applications and separate users for different functionalities.

  6. **Complement with Input Validation**  
     Validate inputs for expected format and length before database operations, but never assume validation alone prevents SQL injection.

recommendation: |
  - Prefer prepared statements or ORM parameterization in your code.
  - When using stored procedures, ensure all inputs are parameters; avoid unsafe dynamic SQL inside them.
  - Implement explicit allow-lists if user input drives SQL identifiers.
  - Assign minimal database permissions and avoid using highly privileged accounts in your application.
  - Use input validation as a secondary guard, never as a replacement for parameterization.
---

# Rule logic (example pseudo-patterns illustrating unsafe usage to warn about)

patterns:
  - pattern: |
      $DB.execute("SELECT * FROM users WHERE name = '" + $input + "'")
    
      Avoid dynamic SQL concatenation with user input. Use prepared statements or parameterized queries instead to prevent SQL injection.

  - pattern: |
      "EXECUTE IMMEDIATE " + $input
    
      Dynamic SQL inside stored procedures or database commands with user input is unsafe. Use parameterized inputs only.

  - pattern: |
      db.query("SELECT * FROM " + $tableName)
    
      User input in SQL identifiers like table or column names must be checked against a strict allow-list, never inserted directly.

  - pattern: |
      escapeSql($input)
    
      Escaping user input alone is not reliable; prefer parameterized queries.

  - pattern: |
      db.connect(user='admin', password=$pass)
    
      Avoid using admin or elevated privilege accounts for application database access. Use least privilege accounts instead.