```yaml
---
trigger: glob
globs: [js, java, php, py, sh, bash, rb, pl]
---
id: os-command-injection-defense
message: >
  Avoid OS command injection vulnerabilities by following best practices:
  - Prefer built-in language functions/libraries over executing OS commands.
  - If OS commands are unavoidable, never concatenate user input into command strings.
  - Validate commands and arguments against strict allowlists and disallow shell metacharacters (& | ; $ > < ` ' " ( ) space tab newline).
  - Pass commands and arguments as separate parameters, not a single command line.
  - Use language-specific escaping (e.g., PHP's escapeshellarg()) for user input.
  - Run applications with least privilege, using isolated accounts for command execution.
  - Regularly audit and test for injection risks using OWASP guidelines.
help: |
  Critical points to secure OS command execution:
  1. Avoid executing OS commands where possible; use native APIs instead.
  2. When executing commands:
     - Use parameterized APIs (e.g., Java ProcessBuilder with argument arrays).
     - Validate commands and arguments strictly against known good patterns.
     - Escape inputs properly to prevent shell parsing.
  3. Never build commands by concatenating untrusted input.
  4. Separate commands from arguments clearly.
  5. Run processes with least privilege possible.
  6. Continuously review and test your codebase for injection risks.

tags: [security, injection, os-command-injection, defense-in-depth, validation]
severity: error
patterns:
  - pattern-either:
      # Detect risky concatenation with user input interpolated into commands
      - pattern: |
          system($X + ...)
      - pattern: |
          Runtime.exec($X + ...)
      - pattern: |
          Runtime.exec("$X ...")
      - pattern: |
          `...$X...`
      - pattern: |
          exec($X + ...)
      - pattern: |
          os.system("$X ...")
  - pattern-not:
      # Detect safe usage with parameter arrays or escaped args
      - pattern: |
          ProcessBuilder([..., $X, ...])
      - pattern: |
          escapeshellarg($X)
fix: |
  Review code that invokes OS commands with user input. Instead of concatenation, separate command and arguments explicitly. Validate inputs strictly, disallow shell metacharacters, and use escaping functions provided by your language. Where possible switch to internal APIs that do not invoke a shell. Run commands with minimal privileges and audit your code regularly.
```