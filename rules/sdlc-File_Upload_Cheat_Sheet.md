---
trigger: glob
globs: [js, ts, py, java, cs, rb, php, go, html, htaccess]
---

name: Secure File Upload Handling

  Enforce robust file upload security controls to prevent malicious files and abuse,
  based on OWASP File Upload best practices.

tags: [security, file-upload, injection, dos, malware]

pattern-either:
  - pattern: |
      # Detect patterns of trusting user-supplied filenames without sanitization, e.g. direct usage in file writes:
      $FILENAME = $_FILES['*']['name'];
      file_put_contents("uploads/$FILENAME", $_FILES['*']['tmp_name']);
  - pattern: |
      # Usage of user-supplied Content-Type header as definitive validation:
      if ($_FILES['*']['type'] == 'image/png') { ... }
  - pattern: |
      # Missing file extension validation before processing uploads:
      move_uploaded_file($_FILES['*']['tmp_name'], "uploads/" . $_FILES['*']['name']);
  - pattern-not: |
      # Enforcing max file size checks or limits:
      if ($_FILES['*']['size'] > $MAX_SIZE) { throw ...; }
  - pattern: |
      # Storing uploaded files in web root or directly accessible locations:
      move_uploaded_file($_FILES['*']['tmp_name'], "/var/www/html/uploads/...");
  - pattern-not: |
      # Using safe filename generation (UUID or sanitized) for storage:
      $safeName = uuid4() + extension;

message:
  File upload handling must enforce multiple security controls:

  1. Restrict allowed file extensions and validate remapped sanitized filenames.
  2. Never trust client-supplied Content-Type; validate file signatures (magic numbers) server-side.
  3. Generate safe unique filenames (e.g., UUID) instead of user-supplied names, or strictly sanitize them.
  4. Enforce and verify file size limits, including post decompression for archives.
  5. Store uploads out of webroot or on isolated storage servers, serving files via controlled handlers.
  6. Apply malware scans and leverage content sanitization libraries for images/docs.
  7. Authenticate and authorize users before accepting uploads; protect endpoints against CSRF and XSS.
  8. Limit upload request rates to avoid DoS attacks.
  9. Provide abuse reporting and moderation workflows.

  Follow OWASP File Upload Security Cheat Sheet for comprehensive defense-in-depth.

recommendation:
  - Use well-reviewed libraries to validate file extensions and magic numbers.
  - Rename uploaded files to random safe identifiers to prevent injection and traversal.
  - Reject or sanitize dangerous filenames strictly if preservation is required.
  - Validate file size limits both client and server side; for compressed files, verify post-extraction size.
  - Store uploads outside webroot; serve via application logic enforcing access controls.
  - Integrate antivirus/Content Disarm & Reconstruct (CDR) scanning pipelines.
  - Authenticate users before uploads and protect against CSRF.
  - Monitor upload rates and implement logging and abuse reporting.
  - Do not solely rely on client-provided MIME types.