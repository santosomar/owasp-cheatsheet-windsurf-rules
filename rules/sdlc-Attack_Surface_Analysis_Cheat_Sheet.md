---
trigger: glob
globs: .md, .txt, .yml, .yaml, .tf, .json, .js, .ts, .java, .py, .go, .rb, .php, .cs
---

As a software engineer, understanding and managing your application's attack surface is a fundamental part of building secure software. Your application's attack surface is the sum of all points where an unauthorized user (an attacker) can try to enter data, extract data, or invoke execution. Here’s how to approach it:

### 1. Identify and Document Your Attack Surface

You can't protect what you don't know about. The first step is to map out all the entry and exit points of your application.

**Best Practices:**

*   **Catalog Entry Points:** Identify all user interfaces (UIs), APIs (REST, GraphQL, etc.), file uploads, database connections, and message queue consumers. Don't forget third-party integrations.
*   **Map Data Flows:** Document how data enters, is processed, and exits your system. This includes data formats being used (e.g., JSON, XML, serialized objects).
*   **Keep Documentation Current:** Maintain a living document, such as a `ATTACK_SURFACE.md` file in your repository, that details these components. Update it whenever the application architecture changes.

### 2. Analyze and Prioritize

Once you have a map, you need to assess the risk associated with each part of the attack surface.

**Best Practices:**

*   **Categorize Components:** Classify each entry point based on its exposure (e.g., public-facing vs. internal) and the sensitivity of the data it handles.
*   **Prioritize Reviews:** Focus your security efforts, such as code reviews and penetration testing, on the most exposed and highest-risk components. An unauthenticated public API handling user data is a higher priority than an internal admin dashboard.
*   **Threat Model:** Use threat modeling to think like an attacker and identify potential vulnerabilities in your design.

### 3. Reduce and Monitor

A smaller attack surface is easier to defend.

**Best Practices:**

*   **Principle of Least Privilege:** If a feature, endpoint, or dependency is not needed, remove it. Disable unused features and interfaces.
*   **Minimize Dependencies:** Every third-party library you add can potentially increase your attack surface. Regularly audit and remove unused dependencies.
*   **Continuously Reassess:** Your application is always evolving. Make attack surface analysis a regular part of your development lifecycle, not a one-time activity.

### 4. Complement with Operational Controls

Secure coding is essential, but it should be part of a defense-in-depth strategy.

**Best Practices:**

*   **Leverage Infrastructure:** Use Web Application Firewalls (WAFs), firewalls, and network segmentation to protect your application at the operational level. These are often defined in Infrastructure-as-Code (IaC) files (e.g., Terraform, CloudFormation), which should be reviewed for security.
