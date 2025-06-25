---
trigger: glob
globs: [js, ts, java, py, rb, go, c, cpp, cs, config, yml, yaml, pem, crt, key, conf, nginx, apache, toml]
---


  Ensure your application uses modern, strong TLS protocols and cipher suites,
  manages certificates securely, enforces HTTPS site-wide, and protects sensitive data in transit.
  This prevents common TLS vulnerabilities and enhances communication security.


patterns:
  - pattern-not: |
      # Disallow deprecated TLS protocols and insecure cipher suites in config or code, e.g. TLS 1.0/1.1, SSLv2/3
      # TLS_FALLBACK_SCSV must be enabled if any fallback to older versions occurs.
      disable_tls_1_0: true
      disable_tls_1_1: true
      disable_ssl: true
      enable_tls_fallback_scsv: true
  - pattern-not: |
      # Ciphers must be strong: AEAD GCM preferred; no NULL, anonymous, EXPORT ciphers
      cipher_suites: *(AEAD_GCM*, !NULL, !ANON, !EXPORT)*
  - pattern-not: |
      # Enable secure DH groups (ffdhe2048/3072) for TLS<=1.2 and preferred ECDHE curves (x25519, prime256v1)
      dh_group: (ffdhe2048|ffdhe3072)
      ecdhe_curve: (x25519|prime256v1)
  - pattern-not: |
      # Disable TLS compression to prevent CRIME attacks
      tls_compression_enabled: false
  - pattern-not: |
      # Private keys should have strong encryption and strict filesystem permissions
      private_key_length: >=2048
      private_key_protected: true
  - pattern-not: |
      # Certificates use SHA-256 or stronger hashing, include correct FQDNs in CN and SAN
      cert_hash_algorithm: sha256|sha384|sha512
      cert_fqdn_validation: true
  - pattern-not: |
      # Avoid wildcard certificates unless limited in scope and not shared across trust zones
      use_wildcard_certificates: false
  - pattern: |
      # HTTPS enforced site-wide, HTTP to HTTPS redirects use 301 status, HSTS headers include preload and includeSubDomains
      use_https_everywhere: true
      http_redirect_status: 301
      hsts_enabled: true
      hsts_preload: true
      hsts_include_subdomains: true
  - pattern-not: |
      # Prevent mixed content by loading all resources over HTTPS
      mixed_content: false
  - pattern-not: |
      # Set Secure flag on all cookies
      cookie_secure_flag: true
  - pattern: |
      # Disable caching of sensitive data with appropriate HTTP headers
      cache_control: no-cache,no-store,must-revalidate
      pragma: no-cache
      expires: 0
  - pattern-not: |
      # Avoid pinning public keys in browsers, limit to controlled environments only
      public_key_pinning: false
  - pattern: |
      # Recommend testing TLS configuration regularly with SSL Labs, testssl.sh, etc.
      tls_testing_practices: true


  Follow these critical TLS security best practices:
  - Use TLS 1.3 by default; fallback to 1.2 only if necessary, disable older protocols and SSL.
  - Configure strong cipher suites (AEAD GCM), secure DH groups, and disable TLS compression.
  - Securely manage certificates: use SHA-256+, correct FQDN in CN/SAN, avoid wildcard certs unless scoped.
  - Enforce HTTPS site-wide with 301 redirects and HSTS (including preload and subdomains).
  - Load all page resources securely to prevent mixed content issues.
  - Set Secure flag on cookies to restrict to HTTPS.
  - Prevent caching of sensitive data via HTTP headers.
  - Avoid public key pinning in browsers.
  - Regularly test TLS settings using recommended online and offline tools.
  Keeping TLS configurations up to date and secure protects user data confidentiality, integrity, and authenticity.

fix: |
  - Update your TLS configuration files/code to enable TLS 1.3 and disable TLS 1.0/1.1 and SSL v2/v3.
  - Restrict cipher suites to AEAD GCM modes; disable weak and anonymous ciphers.
  - Use strong DH groups and favored ECDHE curves.
  - Disable TLS compression features.
  - Ensure private keys are at least 2048-bit and file permissions restrict access.
  - Obtain certificates with SHA-256+ hashing and correct domain names.
  - Use HTTPS for all pages; configure 301 HTTP→HTTPS redirects and HSTS with preload.
  - Review and correct all page resources and script includes to load over HTTPS only.
  - Mark all cookies Secure and set cache-control headers to prevent sensitive data caching.
  - Remove HPKP headers in public web apps; consider pinning only in closed environments.
  - Integrate TLS configuration testing tools into your CI/CD pipeline to catch regressions early.
```