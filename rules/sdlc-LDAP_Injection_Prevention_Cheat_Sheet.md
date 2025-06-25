---
trigger: glob
globs: .java, .cs, .py, .js, .ts
---

## Preventing LDAP Injection Vulnerabilities

As a software engineer working with directory services, you need to be aware of LDAP injection vulnerabilities. These occur when untrusted user input is improperly incorporated into LDAP queries, potentially allowing attackers to bypass authentication, access unauthorized data, or modify directory information.

### Understanding LDAP Injection

LDAP (Lightweight Directory Access Protocol) queries consist of two main components that are vulnerable to injection:

1. **Distinguished Names (DNs)**: Unique identifiers for directory entries (e.g., `cn=admin,dc=example,dc=com`)
2. **Search Filters**: Criteria for finding entries (e.g., `(uid=jsmith)`)

Injection can occur when user input is directly concatenated into either component without proper validation and escaping.

### Best Practices for Prevention

#### 1. Use Parameterized LDAP APIs

Many modern LDAP libraries provide safe methods for building queries:

```java
// UNSAFE: Direct string concatenation
String username = request.getParameter("username");
String filter = "(uid=" + username + ")";  // VULNERABLE

// SAFE: Using parameterized methods
import javax.naming.directory.SearchControls;
import javax.naming.directory.DirContext;

String username = request.getParameter("username");
// Create properly escaped filter
String filter = "(uid={0})";
SearchControls ctls = new SearchControls();
ctls.setSearchScope(SearchControls.SUBTREE_SCOPE);
NamingEnumeration<SearchResult> results = ctx.search(
    "dc=example,dc=com",
    filter,
    new Object[]{username},  // Parameter is safely handled
    ctls
);
```

#### 2. Input Validation with Allowlists

Restrict input to known-safe characters before using it in LDAP operations:

```csharp
// C# example
public bool IsValidLdapUsername(string input)
{
    // Only allow alphanumeric characters and some safe symbols
    Regex regex = new Regex("^[a-zA-Z0-9._-]+$");
    return regex.IsMatch(input);
}

// Validate before use
if (!IsValidLdapUsername(username))
{
    throw new SecurityException("Invalid username format");
}
```

#### 3. Context-Specific Escaping

Different LDAP contexts require different escaping rules:

##### For Distinguished Names (DN)

Escape special characters according to RFC 2253:

```javascript
// JavaScript example
function escapeDN(input) {
    // Escape special chars: \ # + < > , ; " = and leading/trailing spaces
    return input.replace(/[\\#+<>,;"=]/g, char => '\\' + char.charCodeAt(0).toString(16))
                .replace(/^\s/, '\\ ')
                .replace(/\s$/, '\\ ');
}

// Usage
const safeDN = `cn=${escapeDN(username)},dc=example,dc=com`;
```

##### For Search Filters

Escape special characters according to RFC 4515:

```python
# Python example
def escape_filter(input):
    # Escape special chars: * ( ) \ NUL
    if input is None:
        return None
    s = str(input)
    s = s.replace('\\', '\\\\')  # \ -> \\
    s = s.replace('(', '\\28')    # ( -> \(
    s = s.replace(')', '\\29')    # ) -> \)
    s = s.replace('*', '\\2a')    # * -> \*
    s = s.replace('\0', '\\00')   # NUL -> \0
    return s

# Usage
safe_filter = f"(uid={escape_filter(user_input)})"
```

#### 4. Use Established Security Libraries

Leverage well-maintained security libraries for LDAP encoding:

* **Java**: OWASP ESAPI or Apache Directory API
  ```java
  import org.owasp.esapi.ESAPI;
  String safeInput = ESAPI.encoder().encodeForLDAP(userInput);
  ```

* **.NET**: Microsoft's `System.Text.Encodings.Web`
  ```csharp
  using System.Text.Encodings.Web;
  string safeFilter = Encoder.LdapFilterEncode(userInput);
  string safeDN = Encoder.LdapDistinguishedNameEncode(userInput);
  ```

#### 5. Implement Least Privilege

* Use read-only LDAP bind accounts for search operations
* Create separate service accounts with minimal permissions for each application
* Avoid using administrative accounts for application connections

```java
// Example of setting up a minimal-privilege connection
Hashtable<String, Object> env = new Hashtable<>();
env.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
env.put(Context.PROVIDER_URL, "ldap://ldap.example.com:389");
env.put(Context.SECURITY_AUTHENTICATION, "simple");
env.put(Context.SECURITY_PRINCIPAL, "cn=app-readonly,dc=example,dc=com");
env.put(Context.SECURITY_CREDENTIALS, "app-password");

DirContext ctx = new InitialDirContext(env);
```

#### 6. Additional Security Measures

* **Normalize inputs** before validation to prevent evasion techniques
* **Use bind operations** for authentication rather than comparing password attributes
* **Implement proper error handling** to avoid leaking directory information
* **Regularly audit LDAP queries** in your application for potential injection points
* **Test your application** using LDAP injection testing tools and techniques

By implementing these defensive practices, you can significantly reduce the risk of LDAP injection vulnerabilities in your applications.
