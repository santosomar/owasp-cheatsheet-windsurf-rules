```yaml
---
trigger: glob
globs: [.java, .xml]
---

rule:
  id: java-bean-validation-best-practices
  message: |
    Ensure consistent and secure input validation using Java Bean Validation (Jakarta Validation) with Hibernate Validator.
    - Annotate your domain model fields, getters, constructors, and classes with built-in constraints like @Pattern, @Size, @Min/@Max, @Email, @URL, @Past/@Future, @Digits.
    - Use @Valid on nested beans and controller method parameters to cascade validation and trigger checks automatically.
    - Integrate Hibernate Validator by adding its dependency (e.g., in pom.xml) and enable validation in Spring MVC (<mvc:annotation-driven />).
    - Handle validation failures gracefully: capture errors with BindingResult, return HTTP 400 status, and provide user-friendly, non-sensitive error messages.
    - Avoid deprecated constraints such as @SafeHtml; prefer supported, tested constraints.
    - Customize validation messages via message keys and configure Spring's MessageSource for proper localization.
    - Implement custom constraints for business logic beyond built-in validators following official specifications.
  severity: warning
  languages: [java]
  patterns:
    - pattern-not-inside-comment: '@Valid'
    - pattern-not-inside-comment: '@Pattern'
    - pattern-not-inside-comment: '@Size'
    - pattern-not-inside-comment: '@Min'
    - pattern-not-inside-comment: '@Max'
    - pattern-not-inside-comment: '@Email'
    - pattern-not-inside-comment: '@URL'
  validations:
    - when: "file.name.endsWith('.java')" 
      then:
        - check: "Use of annotations for bean validation (@Pattern, @Size, @Min, @Max, @Email, @URL, @Past, @Future, @Digits)."
        - check: "Use @Valid on nested beans and controller parameters to cascade validation."
    - when: "file.name.endsWith('.xml')"
      then:
        - check: "Presence of <mvc:annotation-driven /> to enable validation in Spring MVC."
        - check: "Presence of Hibernate Validator dependency in pom.xml for Maven projects."
  remediation: |
    - Define validation constraints directly on your Java domain model using standard annotations to ensure central and consistent validation.
    - Use @Valid to trigger validation on nested objects and controller inputs.
    - Add Hibernate Validator dependency to your build configuration and enable Spring MVC validation support.
    - Capture validation failures with BindingResult and respond with HTTP 400 and safe, user-friendly messages.
    - Avoid deprecated annotations like @SafeHtml.
    - Externalize messages using keys in annotations and configure MessageSource for localization.
    - For specialized validation logic, implement custom constraints per Hibernate Validator guidelines.
```