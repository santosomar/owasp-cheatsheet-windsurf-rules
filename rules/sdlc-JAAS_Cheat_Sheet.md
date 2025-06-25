```yaml
---
trigger: glob
globs: [.java, .config]
---

rule: JAAS Authentication Best Practices

description: |
  This rule guides developers on how to properly implement and configure JAAS authentication in Java applications, emphasizing secure handling of credentials, proper lifecycle management, and configuration syntax.

check: |
  Detect usage of JAAS LoginContext, LoginModule, and CallbackHandler patterns in Java source (.java) and JAAS configuration files (.config). Check for:

  - Correct JAAS config file syntax:
    - LoginModule stanzas terminated with semicolons.
    - Options defined as key=value pairs, e.g., debug="true".
  - In LoginModule implementations:
    - Proper saving of initialize() arguments (subject, callbackHandler, sharedState, options).
    - Secure handling of credentials in login() method using CallbackHandler.
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