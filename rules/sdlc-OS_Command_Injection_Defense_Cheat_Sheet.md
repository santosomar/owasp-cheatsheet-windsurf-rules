---
trigger: glob
globs: .js, .java, .php, .py, .sh, .bash, .rb, .pl
---

 Preventing OS Command Injection Vulnerabilities

As a software engineer, you should be extremely cautious when executing operating system commands from your application. OS Command Injection vulnerabilities occur when untrusted input is incorporated into system commands, potentially allowing attackers to execute arbitrary commands on the host system.

 Best Practices for Secure Command Execution

 1. Avoid OS Commands When Possible

The safest approach is to not execute OS commands at all:

* Use built-in language functions and libraries instead of shell commands
* Look for native APIs that provide the functionality you need

**Example: Instead of calling external commands**

```javascript
// UNSAFE: Using OS command to list files
const { exec } = require('child_process');
exec('ls -la ' + userProvidedPath); // VULNERABLE

// SAFER: Using native Node.js API
const fs = require('fs');
fs.readdir(userProvidedPath, (err, files) => {
  // Process files safely
});
```

 2. Use Parameterized Command Execution

If you must execute OS commands, never build command strings through concatenation:

```java
// UNSAFE: Command string concatenation
String userData = request.getParameter("userData");
Runtime.getRuntime().exec("find /users -name " + userData); // VULNERABLE

// SAFE: Using arrays to separate command and arguments
String[] cmd = new String[] {"find", "/users", "-name", userData};
ProcessBuilder pb = new ProcessBuilder(cmd);
Process p = pb.start();
```

 3. Implement Strict Input Validation

Validate all inputs that will be used in command execution:

```python
import re
import subprocess

def is_safe_filename(filename):
     Only allow alphanumeric characters, underscore, hyphen, and period
    return bool(re.match(r'^[a-zA-Z0-9_.-]+$', filename))

def get_file_info(filename):
    if not is_safe_filename(filename):
        raise ValueError("Invalid filename")
    
     Safe execution with arguments as list
    result = subprocess.run(["file", filename], capture_output=True, text=True)
    return result.stdout
```

 4. Use Language-Specific Security Features

Many languages provide built-in functions to help secure command execution:

```php
// PHP example using escapeshellarg
$userFile = $_GET['file'];
$safeArg = escapeshellarg($userFile);
exec("file $safeArg", $output);
```

```ruby
 Ruby example using shell escape
require 'shellwords'
user_input = params[:filename]
safe_input = Shellwords.escape(user_input)
`file {safe_input}`
```

 5. Run with Least Privilege

* Configure your application to run with the minimum permissions needed
* Use dedicated service accounts with limited access
* Consider containerization or sandboxing for command execution

 6. Implement Command Allowlisting

Only allow specific, pre-approved commands to be executed:

```javascript
function executeAllowedCommand(command, args) {
  // Define allowed commands
  const allowedCommands = {
    'convert': '/usr/bin/convert',
    'ffmpeg': '/usr/bin/ffmpeg'
  };
  
  // Check if command is allowed
  if (!allowedCommands[command]) {
    throw new Error('Command not allowed');
  }
  
  // Execute with full path and arguments as array
  const { spawn } = require('child_process');
  return spawn(allowedCommands[command], args);
}
```

 7. Avoid Shell Execution Mode

Many programming languages offer a "shell" mode that invokes the system shell, which is particularly dangerous:

```python
 UNSAFE: Shell=True allows shell metacharacters
subprocess.run(f"grep {user_input} file.txt", shell=True)  VULNERABLE

 SAFE: Shell=False (default) and arguments as list
subprocess.run(["grep", user_input, "file.txt"])
```

 8. Detect and Block Shell Metacharacters

If you must accept user input that will be used in commands, consider blocking shell metacharacters:

```javascript
function containsShellMetacharacters(input) {
  const dangerousChars = /[;&|`\\\"'$*?~<>^()\[\]{}\s\n\r]/;
  return dangerousChars.test(input);
}

if (containsShellMetacharacters(userInput)) {
  throw new Error('Potentially dangerous input detected');
}
```

By implementing these defensive practices, you can significantly reduce the risk of OS command injection vulnerabilities in your applications.
          os.system("$X ...")
  - pattern-not:
       Detect safe usage with parameter arrays or escaped args
      - pattern: |
          ProcessBuilder([..., $X, ...])
      - pattern: |
          escapeshellarg($X)
fix: |
  Review code that invokes OS commands with user input. Instead of concatenation, separate command and arguments explicitly. Validate inputs strictly, disallow shell metacharacters, and use escaping functions provided by your language. Where possible switch to internal APIs that do not invoke a shell. Run commands with minimal privileges and audit your code regularly.