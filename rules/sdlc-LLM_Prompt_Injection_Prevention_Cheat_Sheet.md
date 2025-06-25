```yaml
---
trigger: glob
globs: [js, ts, py, java, go, rb, cs, php, swift, kt, scala]
---

id: avoid-llm-prompt-injection
name: Prevent Prompt Injection in LLM Integrations
description: |
  Detects unsafe prompt construction patterns and encourages best practices to prevent prompt injection attacks that could hijack LLM behavior, leak sensitive information, or trigger unauthorized actions.

severity: high
categories: [security, injection, llm, ai]

patterns:
  - pattern-either:
      # Flag unsafe concatenation of user input and system prompt
      - pattern: |
          system_prompt + user_input
      - pattern: |
          "${system_prompt}${user_input}"
      - pattern: |
          prompt = system_instructions + input_data
      - pattern: |
          prompt = `${system_instructions}${user_data}`
      # Patterns suggesting prompt parts are concatenated without separation

  - pattern-inside-string: >
      system_instructions
      # catch naive interpolations where user data is directly appended

  - pattern: |
      raw_input = input()
      prompt = system_instruction + raw_input
      # unsanitized direct user input concatenation

  - pattern-regex: '.*(eval|exec|shell_exec)\(.*(user_input|request\.GET|input\(.+?\)).*\).*'
      message: Avoid executing user input directly in prompt or code execution contexts.

  - pattern: |
      def build_prompt(user_input):
          prompt = system_instructions + user_input
  - pattern: |
      prompt = f"{system_prompt}{user_input}"

fixes:
  - message: >
      Separate system instructions explicitly from user input and avoid direct concatenation.
      Use structured prompts with clear labels, e.g.:

      SYSTEM_INSTRUCTIONS:
      [your rules and constraints]

      USER_DATA_TO_PROCESS:
      [sanitized user input]

      Also, implement robust input validation, normalization, and human review for risky inputs.

advice: |
  KEY ACTIONS TO MITIGATE PROMPT INJECTION RISKS:

  1. Do NOT build prompts by simply concatenating user input with system instructions.
  2. Separate system instructions and user data clearly in your prompt construction.
  3. Sanitize and normalize user inputs to detect obfuscated injection attempts.
  4. Implement fuzzy matching to catch typoglycemia and encoded payloads.
  5. Apply input filtering and reject suspicious inputs before forwarding to the LLM.
  6. Monitor model outputs for evidence of prompt leakage or data exfiltration.
  7. Use human-in-the-loop for high-risk inputs flagged by your detection.
  8. Follow least privilege principles for LLM API access and external tool invocation.
  9. Log all LLM interactions for forensic review and anomaly detection.
  10. Regularly test your system against updated attack patterns and encodings.
  11. Educate developers and operators about prompt injection risks and response plans.
  12. Accept that defenses are partial: stay vigilant and update protections continuously.

  By applying this layered defense approach and strict prompt architecture, you can greatly reduce prompt injection vectors and protect your LLM-powered features from abuse.
```