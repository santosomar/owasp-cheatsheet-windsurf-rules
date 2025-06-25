---
trigger: glob
globs: [java, cs, csharp, php, rb, pl, sql, cfml, rs]
---

  Detect and prevent risks of SQL Injection by always using parameterized queries or prepared statements, and avoid unsafe string concatenation for SQL commands.


  Use parameterized queries or prepared statements instead of concatenating user input into SQL queries. This prevents attackers from altering the intended SQL commands.


  - Always use language- or framework-specific parameterized queries or prepared statements to pass user input as parameters, not literals in query strings.
  - Validate and sanitize inputs before using them, especially if inputs are used in query parameters.
  - Avoid dynamic SQL where possible. If dynamic SQL is necessary, use bind variables or parameter binding features of your database driver or API.
  - Confirm that parameterization is done server-side; client-side parameterization libraries may still build unsafe queries.
  - For stored procedures:
    - Pass parameters directly without string concatenation.
    - Use bind variables when constructing any dynamic SQL inside stored procedures.
  - Consult your framework's or language's database access documentation to implement safe query practices.

examples:
  - language: java
    code: |
      // Safe: using PreparedStatement with parameters
      String query = "SELECT * FROM users WHERE username = ?";
      PreparedStatement pstmt = connection.prepareStatement(query);
      pstmt.setString(1, userInput);
      ResultSet rs = pstmt.executeQuery();

  - language: csharp
    code: |
      // Safe: using parameterized queries with SqlCommand
      string sql = "SELECT * FROM Customers WHERE CustomerId = @CustomerId";
      using var command = new SqlCommand(sql, connection);
      command.Parameters.AddWithValue("@CustomerId", customerId);

  - language: php
    code: |
      // Safe: using PDO prepared statements with named parameters
      $stmt = $dbh->prepare("SELECT * FROM users WHERE name = :name");
      $stmt->bindParam(':name', $name);
      $stmt->execute();

  - language: sql
    code: |
      -- Safe stored procedure using parameters without dynamic SQL
      CREATE PROCEDURE GetBalance @UserID VARCHAR(20), @Dept VARCHAR(10) AS
      BEGIN
          SELECT balance FROM accounts WHERE user_ID = @UserID AND department = @Dept;
      END;

  - language: sql
    code: |
      -- Safe dynamic SQL in stored procedure using sp_executesql with parameters
      CREATE PROCEDURE GetBalance @UserID VARCHAR(20), @Dept VARCHAR(10) AS
      BEGIN
          DECLARE @sql NVARCHAR(200) = 'SELECT balance FROM accounts WHERE user_ID = @UID AND department = @DPT';
          EXEC sp_executesql @sql, N'@UID VARCHAR(20), @DPT VARCHAR(10)', @UID=@UserID, @DPT=@Dept;
      END;

```