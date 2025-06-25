```yaml
---
trigger: glob
globs: [.c, .cpp, .h, .hpp, .py, .go, .java, .js, .rs, .mavlink, .yaml, .yml]
---

rule: Drone Security Best Practices
msg: Apply strong security controls for drone communication, authentication, physical security, and monitoring.
severity: high
languages: [c, cpp, python, go, java, javascript, rust]
author: OWASP Drone Security Cheat Sheet

description: |
  Ensuring security in drone software is critical to prevent unauthorized access, data manipulation, and attacks on communication channels.
  Follow these best practices to safeguard drone operations and software components.

recommendations:
  - Always encrypt communication links between drones and Ground Control Stations using strong protocols such as TLS or DTLS.
  - Implement MAVLink 2.0 message signing and protect heartbeat messages to prevent spoofing, replay, and command injection.
  - Enforce Wi-Fi security with WPA3 and 802.11w Management Frame Protection; disable weak protocols like WEP.
  - For ZigBee integration, enable AES-128 encryption and rotate keys frequently.
  - Use Bluetooth LE Secure Connections (Bluetooth 4.2+) and avoid insecure pairing modes like "Just works".
  - Harden companion computers by closing unnecessary ports (e.g., SSH, FTP), applying multi-factor authentication, and regularly rotating strong credentials.
  - Physically secure drones to prevent unauthorized hardware access and properly sanitize devices when decommissioning.
  - Protect sensor data integrity by verifying GPS, camera, and altimeter inputs; consider advanced validation like dynamic watermarking.
  - Enable secure and comprehensive logging and monitoring to detect security incidents promptly.
  - Utilize trusted protocol implementations (e.g., ArduPilot, PX4) and keep firmware updated.
  - Defend against common attack vectors like replay, jamming, and MITM by applying timestamps, frequency hopping, and traffic filtering.
  - Train operators to recognize social engineering and phishing attempts, and maintain vigilance against emerging threats.

impact: |
  Following these recommendations significantly reduces risks of drone compromise, unauthorized control, data breaches, and ensures mission safety and integrity.

references:
  - https://cheatsheetseries.owasp.org/cheatsheets/Drone_Security_Cheat_Sheet.html
  - https://mavlink.io/en/
  - https://www.arduPilot.org
  - https://px4.io
```