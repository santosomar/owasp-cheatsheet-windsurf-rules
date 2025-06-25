---
trigger: glob
globs: [*]
---

# Deprecated TLS Cipher String Usage Detected

This file references the deprecated TLS Cipher String Cheat Sheet. The TLS Cipher String Cheat Sheet has been deprecated and is no longer maintained.

**Actionable Advice:**

- Do **not** rely on or implement cipher string configurations based on this deprecated guide.
- For modern and secure TLS configurations, review and adopt best practices from the current [Transport Layer Security Cheat Sheet](Transport_Layer_Security_Cheat_Sheet.md).
- Ensure your TLS cipher suites prioritize strong algorithms and omit weak or vulnerable ones (e.g., avoid RC4, DES, 3DES, MD5).
- Regularly update your TLS configuration to align with current security recommendations and patch any vulnerabilities.
- Test your TLS setup with tools like SSL Labs or testssl.sh to validate compliance with modern standards.

**Summary:**

- Deprecated guidance can lead to insecure configurations.
- Always use up-to-date resources for configuring TLS.
- Maintain vigilant security posture by following active OWASP resources.
```