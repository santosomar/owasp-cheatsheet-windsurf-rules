```yaml
---
trigger: glob
globs: [java, kt, swift, m, cs, xml, js, ts]
---
id: owasp-pinning-001
name: Secure TLS Pinning Implementation and Best Practices
description: |
  TLS certificate or public key pinning helps prevent MitM attacks but is risky and rarely needed.
  Follow these best practices to implement pinning safely and effectively.
severity: HIGH
categories: [security, crypto, networking]
tags: [owasp, pinning, tls, mitm, certificate]

rule: |
  /** 
   * ACTIONABLE GUIDANCE FOR DEVELOPERS:
   * 
   * 1. Assess whether TLS pinning is truly required.
   *    - Avoid pinning unless your app controls both client and server endpoints.
   *    - Do not pin if you cannot securely update pins without app redeployment.
   * 
   * 2. Use platform-native or well-vetted libraries to implement pinning.
   *    - On Android, use Network Security Config XML or libraries like OkHTTP.
   *    - On iOS, use App Transport Security or TrustKit.
   *    - On .NET, use ServicePointManager callbacks.
   *    - On OpenSSL, use verify callbacks enforcing strict failure.
   *    - On Electron, use electron-ssl-pinning or ses.setCertificateVerifyProc.
   *    - DO NOT implement custom TLS or pinning code.
   * 
   * 3. Pin leaf certificates primarily; include backup pins for intermediate CAs.
   *    - Avoid pinning root CAs.
   *    - Prefer public key pinning for flexibility; do not rely on raw hashes without context.
   * 
   * 4. Embed ("preload") pins at build or development time, avoiding Trust On First Use (TOFU).
   *    - Plan for seamless pin updates to prevent app outages.
   * 
   * 5. On pin validation failure, never allow users to bypass warnings.
   * 
   * 6. In corporate environments with SSL proxies, whitelist proxy keys only after explicit risk acceptance.
   * 
   * 7. Thoroughly test your pinning implementation using OWASP MSTG network communication guidelines.
   * 
   * 8. Keep pinned keys and certificates updated in alignment with backend certificate lifecycles.
   * 
   * Following these helps mitigate MITM risks without sacrificing app availability.
   */
  
  // Additionally, search codebases for:
  // - Custom SSLContext, TrustManager, or CertVerifier implementations without known good libs.
  // - Pin sets hardcoded without fallback or update mechanisms.
  // - Allowing user bypass after pin failure in UI handling logic.
  // Flag these patterns for review and refactoring.

```