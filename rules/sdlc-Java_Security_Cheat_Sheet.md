---
trigger: glob
globs: [java]
---

Ensure secure coding in Java by preventing injection attacks and following cryptographic best practices.


patterns:
  - pattern-either:
      - pattern: |
          # Avoid concatenating untrusted input in SQL queries. Use PreparedStatement with parameters.
          PreparedStatement.setString($param$, $_)
      - pattern-not: '"+"'
      - pattern-not: |
          Statement.executeQuery("SELECT " + $_ + " FROM " + $_)
      - pattern-not: |
          @Query("SELECT u FROM User u WHERE u.name = '" + $_ + "'")
  - pattern-not: |
      // Avoid building JPQL queries with string concatenation; use parameterized queries.
      @Query("SELECT u FROM User u WHERE u.name = :name")
  - pattern-not: |
      // Avoid passing user input directly into Runtime.exec or ProcessBuilder command strings.
      Runtime.getRuntime().exec($cmd$, $_)
  - pattern-not: |
      // Avoid XPath expressions concatenating untrusted input.
      xpath.evaluate("'" + $_ + "'", $_)
  - pattern-not: |
      // Do not build NoSQL queries by concatenating strings; always use driver/builders API with validated inputs.
      collection.find("{ name: '" + $_ + "' }")
  - pattern-not: |
      // Avoid unstructured log concatenation with untrusted input.
      logger.info("User input: " + $_)
  - pattern-not: |
      // Prefer parameterized logging over string concatenation.
      logger.info("User input: {}", $_)

  - pattern-either:
      - pattern: |
          // Always validate input early with allowlist regex before processing.
          if ($input$.matches($allowlistRegex$)) { $_ }
      - pattern-not: |
          // No raw input validation or only blacklisting patterns detected.
          $input$.matches(".*badpattern.*")
  - pattern: |
      // Use trusted cryptographic libraries (e.g., Google Tink) rather than custom implementations.
      Import com.google.crypto.tink.*

  - pattern-not: |
      // Avoid writing your own cryptographic algorithms or primitives.
      public class CustomCrypto { $_ }
  - pattern-either:
      - pattern: | 
          // For encryption, use AES-GCM mode with unique 12-byte nonce per encryption.
          cipher.init(Cipher.ENCRYPT_MODE, $key$, GCMParameterSpec(128, $nonce$));
      - pattern-not: |
          // Avoid AES in ECB mode or reuse of nonces with same key.
          cipher.getAlgorithm().contains("ECB")
  - pattern-either:
      - pattern: |
          // Employ secure key and nonce management and rotation.
          keyRotation.schedule($_)
      - pattern-not: |
          // Avoid hardcoded keys or fixed nonces.
          final static String KEY = "hardcodedkey"

fix: |
  - Use parameterized PreparedStatements or JPA named parameters instead of concatenating query strings.
  - Validate all inputs with allowlist regex patterns before processing or storage.
  - Sanitize and encode outputs (HTML, JS, CSS) with OWASP Encoder and Sanitizer libraries before rendering.
  - Use structured logging formats (JSON) and parameterized logging calls; limit logged input sizes to prevent injection.
  - Utilize trusted cryptographic libraries such as Google Tink for encryption and key management.
  - Avoid implementing your own cryptography; rely on vetted solutions and expert review when low-level APIs are needed.
  - Securely generate, store, and rotate cryptographic keys and nonces regularly.
  - Keep cryptography and other dependencies up to date with security patches.

risk: |
  Injection flaws, insecure cryptography, and improper logging lead to data breaches, remote code execution,
  privilege escalation, and breach of confidentiality and integrity.

