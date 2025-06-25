---
trigger: glob
globs: [java, js, rb, php, cs, groovy, scala]
---

rule: Mass Assignment Protection

  Mass Assignment vulnerabilities occur when untrusted input can overwrite unintended object fields, especially sensitive ones like 'isAdmin'. To prevent exploits:

  1. **Never bind user input directly to domain objects with sensitive fields.**

  2. Use Data Transfer Objects (DTOs) to expose only safe, editable fields.

  3. Apply allow-listing or block-listing in frameworks to control bindable properties:
     - **Spring MVC:** Use @InitBinder with setAllowedFields or setDisallowedFields.
     - **NodeJS (Mongoose):** Use _.pick() to allow-list fields or plugins to block-list.
     - **Laravel Eloquent:** Use $fillable (allow-list) or $guarded (block-list).
     - **Ruby on Rails:** Use strong parameters or attr_accessible.

  4. Avoid exposing sensitive fields like 'isAdmin' in HTTP request bindings.

  5. Regularly review models and DTOs for sensitive attributes.

  For more framework-specific guidance, consult official docs (e.g., Spring, Laravel, Rails). Protecting against mass assignment is critical to avoid unauthorized privilege escalation.


patterns:
  - pattern: |
      $OBJ = new $CLASS($INPUT);
    condition: pattern_match($OBJ, $INPUT) and
               exists_sensitive_field($CLASS)
  - pattern-either:
      - pattern: |
          binder.setAllowedFields($FIELDS)
          $SENSITIVE_FIELDS in $FIELDS
      - pattern: |
          binder.setDisallowedFields($FIELDS)
          not $SENSITIVE_FIELDS in $FIELDS
      - pattern: |
          protected $fillable = $FIELDS;
          $SENSITIVE_FIELDS in $FIELDS
      - pattern: |
          protected $guarded = $FIELDS;
          not $SENSITIVE_FIELDS in $FIELDS
  # (Add framework-specific patterns to detect mass assignment risks)
fix: |
  - Implement DTOs exposing only safe fields.
  - Use framework allow-list/block-list binding mechanisms to exclude sensitive fields.
  - Explicitly exclude sensitive fields such as 'isAdmin' from user input binding.
  - Validate and sanitize user data before binding.
```