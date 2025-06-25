---
trigger: glob
globs: .js, .ts, .java, .py, .rb, .go, .cs, .cpp, .swift, .kotlin, .php, .html, .jsx, .tsx, .md, .txt
---

As a software engineer, integrating abuse case analysis into your development process is key to building secure applications. It helps shift from a purely technical to a business-logic-focused security mindset.

### Understanding and Defining Abuse Cases

1.  **Understand the Business Logic:** Before writing any code, deeply understand the business purpose of each feature. Many exploits arise from the misuse of business logic, not just technical flaws.

2.  **Collaborate to Identify Threats:** Participate in or advocate for abuse case workshops. These sessions should include people from business, security, risk, QA, and development to brainstorm how a feature could be misused.

3.  **Create Specific Security Requirements:** Translate the identified abuse cases into precise, feature-specific security requirements and acceptance criteria. This makes security a measurable part of the development process.

### Implementing and Tracking Mitigations

1.  **Traceability is Key:** Annotate your code, design documents, and infrastructure configurations with unique abuse case IDs. This creates a clear link between a security requirement and its implementation.

    **Example (in code comments):**
    ```java
    // Mitigation for ABUSE_CASE_001: Prevent excessive password reset requests.
    @RateLimit(key = "user.id", limit = 3, period = 3600)
    public void resetPassword(String username) { ... }
    ```

2.  **Prioritize Based on Risk:** Use a standardized risk-scoring system like CVSS to prioritize mitigation efforts. This ensures you're focusing on the threats with the highest potential business impact.

3.  **Automate Validation:** Integrate the validation of abuse case mitigations into your CI/CD pipeline. This can include:
    *   Unit and integration tests that simulate abuse scenarios.
    *   Static and dynamic analysis tools (SAST/DAST).
    *   Peer code reviews focused on security.
    *   Penetration testing.

### Fostering a Security Culture

1.  **Share Knowledge:** Maintain a centralized knowledge base of abuse cases and their countermeasures. This helps other teams learn from past experiences and build more secure products.

2.  **Security is a Team Sport:** Collaborate across departments. Security is a shared responsibility that involves business, risk management, development, QA, and security teams working together.

By transforming vague security goals into concrete, business-aligned tasks, you can build more robust and resilient applications that are protected against real-world threats.