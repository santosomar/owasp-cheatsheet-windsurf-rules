---
trigger: glob
globs: [.java, .js, .ts, .py, .go, .rb, .php]
---

  SSRF vulnerabilities arise when untrusted input controls destination of network requests.
  Follow these best practices to protect your application:

    1. Never accept raw URLs from users. Only accept validated IP addresses or domain names.
    2. Use trusted, battle-tested libraries to validate IP and domain formats; avoid homemade regex.
    3. In internal/allowlist-based scenarios:
       - Implement strict allowlists of IPs and domains (case-sensitive exact matches).
       - Disable HTTP client auto-redirects to prevent bypasses.
       - Reject full URLs; accept only IP or domain strings.
    4. For dynamic external targets:
       - Reject IPs from private, localhost, or link-local ranges.
       - Validate that domains do not resolve to internal/private IPs by checking DNS resolution at runtime.
       - Restrict allowed protocols strictly to HTTP and HTTPS.
       - Require a secure token (random 20-char alphanumeric) passed as a POST parameter to verify legitimacy.
    5. Apply network-layer protections:
       - Use firewalls and network segmentation to block access to unauthorized IPs/domains.
    6. Regularly monitor allowlisted domains’ DNS resolutions to detect suspicious internal IP mappings.
    7. Disable HTTP redirects in all outgoing HTTP client libraries.
    8. In cloud environments, migrate to secure metadata services (e.g., AWS IMDSv2) and disable vulnerable versions.
    9. Integrate static analysis and automated scanning tools to detect SSRF risks early.

  
  languages: [java, javascript, typescript, python, go, ruby, php]
  patterns:
    - pattern-either:
     Flag potentially dangerous usage of raw URLs from user input in request code
      - pattern: |
          $client.$method($url, ...)
        where:  
          $url = $inputUser
      - pattern: |
          new URL($url)
        where:
          $url = $inputUser
      Flag usage of dangerous risky protocols
      - pattern-regex: \b(file|ftp|gopher|smb):\/\/
      Flag absence of redirect disabling config or calls disabling redirects
      - pattern-not: |
          $client.setFollowRedirects(false)
          OR
          http_client.set_allow_redirects(False)
      Flag missing token parameter in POST requests to dynamic external URLs
      - pattern: |
          $client.post($url, $params)
        where:
          not contains($params, $tokenParam)
  fix: |
    - Validate and accept only IP addresses or domain names as input—do not accept raw URLs.
    - Use established libraries for IP/domain format validation to avoid encoding or format bypass.
    - Implement allowlists (case-sensitive exact matches) for internal destination IPs/domains.
    - Reject private, link-local, localhost IP addresses and internal domains resolving to private IPs for external dynamic requests.
    - Restrict protocols to HTTP and HTTPS only.
    - Disable automatic HTTP redirects in client libraries.
    - Require caller-supplied tokens on sensitive POST calls to verify request legitimacy.
    - Apply firewall rules and network segmentation to prevent unauthorized network requests.
    - Regularly monitor DNS resolution of allowlisted domains to detect unexpected internal IP resolutions.
    - Migrate to secure cloud metadata services (e.g., AWS IMDSv2), disabling older, vulnerable versions.
    - Use static analysis tools to detect SSRF risks early.
