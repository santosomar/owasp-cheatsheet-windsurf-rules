```yaml
---
trigger: glob
globs: [js, jsx, ts, tsx, java, py, rb, php, go, cs]
---

rule: Avoid_Using_Insecure_Security_Questions
name: Avoid Using Security Questions as Sole Authentication or Recovery Factor
message: |
  Security questions are no longer considered a strong authentication factor and should never stand alone for authentication or account recovery.

  Follow these best practices:
  1. Avoid relying solely on security questions for login or recovery; always use strong authentication like MFA.
  2. If security questions are needed for legacy reasons:
     - Choose questions that are memorable, consistent, confidential, applicable, and specific.
     - Provide a limited, strong predefined list of questions rather than free-form user-created ones.
     - Avoid common or easily discovered questions (e.g., birthdate, nickname).
  3. Validate and restrict answers:
     - Enforce minimum length but allow legitimate short answers.
     - Denylist weak or easily guessable answers like username, email, "123", or "password".
  4. Hash all answers securely using a password hashing algorithm (e.g., bcrypt) and normalize when comparing.
  5. Secure recovery flows:
     - Verify recovery email ownership before presenting questions.
     - Treat incorrect answers as failed attempts; apply lockouts.
  6. Require re-authentication (password or MFA) before allowing changes to security questions/answers.
  7. Use multiple questions to increase security but do not rotate questions on failure—lock to one question to prevent guessing.
  8. Periodically prompt users to review and update their answers (e.g., during password changes).

  Summary: Phase out security questions or replace them with stronger methods like MFA. If used, apply these controls rigorously to mitigate risks.

severity: warning
metadata:
  references:
    - https://pages.nist.gov/800-63-3/sp800-63b.html#sec5_authentication 
    - https://cheatsheetseries.owasp.org/cheatsheets/Security_Questions_Cheat_Sheet.html

pattern-either:
  - pattern: |
      $Q = prompt("Enter your security question:");
  - pattern-inside: |
      def validate_security_question($Q):
          ...
  - pattern: |
      user.setSecurityQuestion($Q)
  - pattern: |
      storeSecurityAnswer(hash($answer))
  - pattern: |
      if ($answer == $securityQuestionAnswer) {
  - pattern: |
      if (securityQuestionsEnabled and not using MFA)
  - pattern: |
      allowFreeFormSecurityQuestions()
  - pattern: |
      recoveryFlow.usesSecurityQuestionsOnly()
  - pattern: |
      updateSecurityQuestionsWithoutReauth()
```