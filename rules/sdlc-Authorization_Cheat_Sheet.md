---
trigger: glob
globs: .js, .ts, .java, .py, .rb, .php, .cs, .go, .swift, .yml, .yaml, .json, .config
---

As a software engineer, implementing robust authorization is critical to ensure users can only access the data and features they are permitted to. While authentication confirms who a user is, authorization determines what they can do.

### Core Principles of Secure Authorization

1.  **Deny by Default:** The default for any access request should be 'deny'. Explicitly grant permissions to roles or users rather than explicitly denying them.
2.  **Principle of Least Privilege:** Grant users the minimum level of access required to perform their job functions. Regularly audit permissions to ensure they are not excessive.

### Server-Side Enforcement is Non-Negotiable

All authorization decisions must be enforced on the server-side for every request. Client-side checks are for user experience only and can be easily bypassed.

**What to Avoid (Anti-Pattern):**

```javascript
// Insecure: Client-side check that can be bypassed by an attacker.
if (currentUser.isAdmin) {
  showAdminDashboard();
} // The server must also check if the user is an admin before returning data.
```

**Best Practice:**

Use centralized middleware or decorators in your backend framework to enforce authorization checks consistently across all relevant endpoints.

**Example (Express.js middleware):**

```javascript
function canViewProject(req, res, next) {
  const project = await db.getProject(req.params.id);
  if (project.ownerId === req.user.id || req.user.isAdmin) {
    return next();
  }
  return res.status(403).send('Forbidden');
}

app.get('/projects/:id', isAuthenticated, canViewProject, (req, res) => {
  // return project data
});
```

### Prevent Insecure Direct Object References (IDOR)

An IDOR vulnerability occurs when an application uses a user-supplied identifier (like a database ID) to access an object directly, without verifying the user has permission to access *that specific object*.

**What to Avoid (Anti-Pattern):**

```javascript
// Insecure: The code checks if the user is authenticated, but not if they
// are authorized to view the invoice with the given ID.
app.get('/invoices/:id', isAuthenticated, (req, res) => {
  const invoice = await db.getInvoice(req.params.id); // Attacker can cycle through IDs
  res.json(invoice);
});
```

**Best Practice:**

Always verify that the authenticated user has the necessary permissions for the specific object they are requesting.

### Additional Best Practices

*   **Use Centralized Failure Handling:** When an authorization check fails, return a generic error message and a standard HTTP status code (e.g., `403 Forbidden` or `404 Not Found`) to avoid leaking information about the resource's existence.
*   **Log Authorization Events:** Log all authorization failures. This is crucial for monitoring and detecting potential attacks.
*   **Automate Testing:** Write unit and integration tests for your access control logic. Test cases should cover both users who should have access and those who should be denied.
*   **Consider Advanced Models:** For complex applications, consider using Attribute-Based Access Control (ABAC) or other fine-grained authorization models.