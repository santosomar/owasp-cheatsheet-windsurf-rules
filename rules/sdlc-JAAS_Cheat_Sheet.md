---
trigger: glob
globs: .java, .config
---

## Java Authentication and Authorization Service (JAAS) Best Practices

As a software engineer working with Java applications that require authentication and authorization, JAAS provides a flexible framework for securing your applications. This guide covers best practices for implementing and configuring JAAS correctly and securely.

### Understanding JAAS Architecture

JAAS consists of several key components:

1. **LoginContext**: The central class that coordinates the authentication process
2. **LoginModule**: Pluggable modules that implement specific authentication mechanisms
3. **CallbackHandler**: Interface for collecting authentication data from users
4. **Subject**: Represents the authenticated entity (user, service, etc.)

### Configuration Best Practices

#### JAAS Configuration File Syntax

JAAS configuration files define authentication contexts and their associated login modules:

```
LoginModuleApplication {
    com.example.security.CustomLoginModule REQUIRED
        debug="true"
        useFirstPass=true;
    com.sun.security.auth.module.LdapLoginModule SUFFICIENT
        userProvider="ldap://ldap.example.com:389/ou=people,dc=example,dc=com"
        userFilter="(&(uid={USERNAME})(objectClass=inetOrgPerson))";
};
```

Ensure your configuration follows these rules:

* Each application context must be terminated with a semicolon
* Each LoginModule entry must be terminated with a semicolon
* Options must be specified as key=value pairs
* Use appropriate control flags (REQUIRED, REQUISITE, SUFFICIENT, OPTIONAL) based on your security requirements

#### Secure Configuration Loading

```java
System.setProperty("java.security.auth.login.config", "/path/to/jaas.config");

// Alternatively, specify at runtime
try {
    Configuration config = new Configuration() {
        // Custom implementation
    };
    Configuration.setConfiguration(config);
} catch (SecurityException e) {
    // Handle exception
}
```

### Implementing LoginModule

When creating custom LoginModules, follow these security practices:

```java
public class CustomLoginModule implements LoginModule {
    private Subject subject;
    private CallbackHandler callbackHandler;
    private Map<String, ?> sharedState;
    private Map<String, ?> options;
    
    private boolean loginSucceeded = false;
    private boolean commitSucceeded = false;
    
    // Securely store principals
    private UserPrincipal userPrincipal;
    private List<RolePrincipal> rolePrincipals;
    
    @Override
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                         Map<String, ?> sharedState, Map<String, ?> options) {
        // Always store these for later use
        this.subject = subject;
        this.callbackHandler = callbackHandler;
        this.sharedState = sharedState;
        this.options = options;
    }
    
    @Override
    public boolean login() throws LoginException {
        // GOOD PRACTICE: Use callbacks to collect credentials
        if (callbackHandler == null) {
            throw new LoginException("No CallbackHandler provided");
        }
        
        Callback[] callbacks = new Callback[] {
            new NameCallback("Username: "),
            new PasswordCallback("Password: ", false)
        };
        
        try {
            callbackHandler.handle(callbacks);
            
            String username = ((NameCallback)callbacks[0]).getName();
            char[] password = ((PasswordCallback)callbacks[1]).getPassword();
            
            // Validate credentials securely
            loginSucceeded = validateCredentials(username, password);
            
            // SECURITY: Clear sensitive data immediately
            ((PasswordCallback)callbacks[1]).clearPassword();
            
            if (!loginSucceeded) {
                throw new FailedLoginException("Authentication failed");
            }
            
            return true;
        } catch (Exception e) {
            loginSucceeded = false;
            throw new LoginException("Authentication failed: " + e.getMessage());
        }
    }
    
    @Override
    public boolean commit() throws LoginException {
        if (!loginSucceeded) {
            return false;
        }
        
        // Add principals to the subject
        subject.getPrincipals().add(userPrincipal);
        subject.getPrincipals().addAll(rolePrincipals);
        
        commitSucceeded = true;
        return true;
    }
    
    @Override
    public boolean abort() throws LoginException {
        if (!loginSucceeded) {
            return false;
        }
        
        // Clean up state
        loginSucceeded = false;
        userPrincipal = null;
        rolePrincipals = null;
        
        commitSucceeded = false;
        return true;
    }
    
    @Override
    public boolean logout() throws LoginException {
        // Remove principals from subject
        subject.getPrincipals().remove(userPrincipal);
        subject.getPrincipals().removeAll(rolePrincipals);
        
        // Clean up state
        loginSucceeded = false;
        commitSucceeded = false;
        userPrincipal = null;
        rolePrincipals = null;
        
        return true;
    }
}
```

### Implementing CallbackHandler

Create secure CallbackHandlers that properly handle credentials:

```java
public class SecureCallbackHandler implements CallbackHandler {
    private String username;
    private char[] password;
    
    public SecureCallbackHandler(String username, char[] password) {
        this.username = username;
        this.password = password;
    }
    
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                NameCallback nameCallback = (NameCallback) callback;
                nameCallback.setName(username);
            } else if (callback instanceof PasswordCallback) {
                PasswordCallback passwordCallback = (PasswordCallback) callback;
                passwordCallback.setPassword(password);
            } else {
                throw new UnsupportedCallbackException(callback, "Callback not supported");
            }
        }
    }
    
    // SECURITY: Method to clear sensitive data
    public void clearCredentials() {
        username = null;
        if (password != null) {
            Arrays.fill(password, ' ');
            password = null;
        }
    }
}
```

### Using JAAS in Applications

```java
try {
    // Create LoginContext with the application name from config
    LoginContext loginContext = new LoginContext("LoginModuleApplication", 
                                               new SecureCallbackHandler(username, password));
    
    // Attempt authentication
    loginContext.login();
    
    // Get the authenticated subject
    Subject subject = loginContext.getSubject();
    
    // Execute code as the authenticated subject
    Subject.doAs(subject, new PrivilegedAction<Void>() {
        public Void run() {
            // Perform privileged operations
            return null;
        }
    });
    
    // Clean up when done
    loginContext.logout();
} catch (LoginException e) {
    // Handle authentication failure
}
```

### Security Best Practices

1. **Never store passwords in plaintext**
   * Always use char[] instead of String for passwords
   * Clear password arrays after use

2. **Implement proper error handling**
   * Avoid revealing sensitive information in error messages
   * Log authentication failures securely

3. **Use appropriate control flags**
   * REQUIRED: Module must succeed, authentication proceeds regardless
   * REQUISITE: Module must succeed, authentication fails immediately if module fails
   * SUFFICIENT: If module succeeds, authentication succeeds immediately
   * OPTIONAL: Authentication proceeds regardless of success or failure

4. **Protect configuration files**
   * Restrict access to JAAS configuration files
   * Consider encrypting sensitive configuration values

5. **Implement proper logout**
   * Always call logout() when a session ends
   * Clear all sensitive data

By following these best practices, you'll create more secure authentication systems using JAAS in your Java applications.
    - Adding Principals and Credentials only in commit() after successful authentication.
    - Clear cleanup/reset of sensitive information in abort().
    - Proper removal of principals and credentials in logout().
  - Use of CallbackHandler to abstract user credential input, separating UI logic from authentication logic.
  - Use of command line options to specify JAAS config file and stanza, avoiding hard-coded credentials.
  
recommendation: |
  1. Always terminate JAAS config stanzas and LoginModule entries with semicolons.
  2. Define options in JAAS config strictly as key="value" pairs using =.
  3. In LoginModule.initialize(), store provided parameters for later use; use sharedState to share info among modules.
  4. Use CallbackHandler to interactively and securely collect user credentials; do not hardcode usernames or passwords.
  5. Authenticate credentials against trusted repositories (e.g., LDAP), and do not store credentials in memory longer than needed.
  6. Add Principals and Credentials only after successful authentication in commit().
  7. On abort(), thoroughly clear any sensitive state to prevent leakage.
  8. On logout(), remove all Principals and Credentials to prevent lingering authorization artifacts.
  9. Use system properties (-Djava.security.auth.login.config) to specify config files at runtime, never embedding sensitive info in source.
  10. Enable debugging (e.g., debug="true") temporarily only during development; disable in production to avoid sensitive info leakage.

example-config: |
  Branches {
      USNavy.AppLoginModule required
      debug="true"
      succeeded="true";
  }

example-loginModule-initialize: |
  public void initialize(Subject subject, CallbackHandler callbackHandler, Map<String,Object> sharedState, Map<String,String> options) {
      this.subject = subject;
      this.callbackHandler = callbackHandler;
      this.sharedState = sharedState;
      this.options = options;
  }

example-login: |
  NameCallback nameCB = new NameCallback("Username");
  PasswordCallback passwordCB = new PasswordCallback("Password", false);
  Callback[] callbacks = new Callback[] { nameCB, passwordCB };
  callbackHandler.handle(callbacks);
  String username = nameCB.getName();
  char[] password = passwordCB.getPassword();
  // Validate username & password against secure store (e.g., LDAP)

example-commit: |
  public boolean commit() {
      if (userAuthenticated) {
          for (String group : UserService.findGroups(username)) {
              subject.getPrincipals().add(new UserGroupPrincipal(group));
          }
          subject.getPublicCredentials().add(new UsernameCredential(username));
          return true;
      }
      return false;
  }

example-logout: |
  public boolean logout() {
      if (!subject.isReadOnly()) {
          subject.getPrincipals().removeAll(subject.getPrincipals(UserGroupPrincipal.class));
          subject.getPublicCredentials().removeAll(subject.getPublicCredentials(UsernameCredential.class));
          return true;
      }
      return false;
  }
```