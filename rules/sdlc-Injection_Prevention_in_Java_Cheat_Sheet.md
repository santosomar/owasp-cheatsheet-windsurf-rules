---
trigger: glob
globs: [java]
---

name: Injection Prevention in Java
message: "Ensure your Java code prevents injection attacks by following these best practices."

patterns:
  - pattern-either:
      - pattern: |
          Statement.executeQuery($SQL)
      - pattern: |
          Statement.executeUpdate($SQL)
      - pattern: |
          Statement.execute($SQL)
  - pattern-not: 
      pattern: |
        PreparedStatement.prepareStatement($SQL)
fix: |
  Avoid constructing SQL queries via string concatenation or Statement objects.
  Use PreparedStatement with parameterized queries instead. Example:

    // Vulnerable code:
    // String sql = "SELECT * FROM users WHERE id = " + userId;
    // Statement stmt = connection.createStatement();
    // ResultSet rs = stmt.executeQuery(sql);

    // Secure code:
    String sql = "SELECT * FROM users WHERE id = ?";
    PreparedStatement pstmt = connection.prepareStatement(sql);
    pstmt.setInt(1, userId);
    ResultSet rs = pstmt.executeQuery();

additional:
  - Avoid mixing query logic and data input.
  - Validate and sanitize all user inputs even when using prepared statements.
  - Use ORM frameworks or query builders that support safe parameterization.
  - Similarly, prevent injection in LDAP, XML, and OS commands by avoiding direct concatenation of untrusted data.
```