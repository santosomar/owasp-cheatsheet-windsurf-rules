---
trigger: glob
globs: .c, .cpp, .h, .java, .js, .py, .xml, .json, .ini, .cfg
---

As a software engineer working on automotive systems, you face unique and critical security challenges. Modern vehicles are complex networks of computers, and securing them is paramount for safety and reliability. Here are best practices to follow, based on the OWASP Automotive Security Top 10.

### 1. Secure In-Vehicle Networks

The Controller Area Network (CAN) bus and other in-vehicle networks were not originally designed with security in mind. It's your job to add it.

*   **Best Practice:** Use secure communication protocols like **Secure CAN** or **DoIP (Diagnostics over IP) with TLS** to authenticate and encrypt network traffic. This prevents attackers who have gained access to one part of the vehicle network from easily controlling other, more critical systems.

### 2. Secure Over-the-Air (OTA) Updates

OTA updates are a primary vector for large-scale attacks.

*   **Best Practice:** All firmware and software updates must be cryptographically signed. Your device must verify this signature before applying any update. Additionally, the update package itself should be delivered over an encrypted and authenticated channel (e.g., HTTPS).

    **Example:**
    ```c
    // Pseudo-code for a secure OTA update process
    if (verify_firmware_signature(ota_package, manufacturer_public_key)) {
      // Signature is valid, proceed with update
      apply_update(ota_package);
    } else {
      // Signature is invalid, discard the package
      log_error("Invalid OTA signature!");
    }
    ```

### 3. Harden APIs and External Interfaces

Telematics systems, mobile apps, and other cloud-connected components are gateways to the vehicle.

*   **Best Practice:** Harden all external APIs with strong authentication, authorization, and input validation. Never trust data coming from an external source. Avoid default or weak credentials, and enforce strong password policies and MFA where applicable.

### 4. Manage Third-Party Dependencies

Your software is only as secure as its weakest link, which is often a third-party library.

*   **Best Practice:** Keep a full inventory of all third-party dependencies (a Software Bill of Materials, or SBOM). Regularly scan for known vulnerabilities and have a plan to apply patches promptly.

### 5. Secure Physical Access

Physical access ports like the OBD-II connector can provide a direct line to critical systems.

*   **Best Practice:** Limit the functionality accessible via diagnostic ports and require strong authentication for any sensitive operations. This prevents an attacker with physical access from easily compromising the vehicle.

### 6. Protect Data

Vehicles collect a vast amount of potentially sensitive user and operational data.

*   **Best Practice:** Encrypt all sensitive data, both at rest (stored on the device) and in transit (when communicating with the cloud). Minimize the data you collect to only what is strictly necessary for the feature to function (data minimization).

By focusing on these key areas, you can significantly improve the security posture of your automotive software and protect against the most common and critical threats.
