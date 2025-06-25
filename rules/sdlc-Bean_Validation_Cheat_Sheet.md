---
trigger: glob
globs: .java, .xml, .gradle
---

As a Java developer, using a declarative, centralized approach to validation is crucial for security and maintainability. The Java Bean Validation standard (now Jakarta Validation) and its primary implementation, Hibernate Validator, provide a powerful way to handle this.

### Why Use Bean Validation?

Instead of scattering validation logic throughout your business layer, you define validation rules directly on your domain models (your "beans"). This keeps your validation logic in one place, making it consistent and easy to manage.

### 1. Setting Up Your Project

First, add the Hibernate Validator dependency to your project.

**Maven (`pom.xml`):**
```xml
<dependency>
    <groupId>org.hibernate.validator</groupId>
    <artifactId>hibernate-validator</artifactId>
    <version>8.0.0.Final</version>
</dependency>
```

If you're using Spring Boot, the `spring-boot-starter-web` dependency includes Hibernate Validator automatically.

### 2. Annotating Your Beans

Apply standard validation annotations directly to the fields of your model classes.

**Example (`UserRegistrationForm.java`):**
```java
public class UserRegistrationForm {

    @NotNull
    @Size(min = 2, max = 50, message = "Name must be between 2 and 50 characters")
    private String name;

    @NotNull
    @Email(message = "Please provide a valid email address")
    private String email;

    @Pattern(regexp = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\\S+$).{8,}$")
    private String password;

    // ... getters and setters
}
```

### 3. Triggering Validation

In a web context (like a Spring MVC controller), use the `@Valid` annotation on your model attribute to trigger the validation process automatically.

**Example (Spring Controller):**
```java
@RestController
public class RegistrationController {

    @PostMapping("/register")
    public ResponseEntity<String> registerUser(@Valid @RequestBody UserRegistrationForm form, BindingResult bindingResult) {
        if (bindingResult.hasErrors()) {
            // Validation failed. Collect errors and return a 400 Bad Request.
            String errors = bindingResult.getAllErrors().stream()
                .map(DefaultMessageSourceResolvable::getDefaultMessage)
                .collect(Collectors.joining(", "));
            return ResponseEntity.badRequest().body(errors);
        }

        // Validation succeeded, proceed with user registration.
        userService.register(form);
        return ResponseEntity.ok("User registered successfully!");
    }
}
```

### 4. Validating Nested Objects

If your model contains other objects that also need validation, just annotate them with `@Valid`.

**Example:**
```java
public class Order {

    @Valid // This will trigger validation on the Address object
    @NotNull
    private Address shippingAddress;

    // ... other fields
}
```

### Best Practices Summary

*   **Centralize Rules:** Define validation constraints on your domain models.
*   **Use Standard Annotations:** Leverage the rich set of built-in annotations (`@NotNull`, `@Size`, `@Pattern`, `@Min`, `@Max`, `@Email`, etc.).
*   **Automate with `@Valid`:** Let your framework trigger validation automatically in your controllers.
*   **Handle Errors Gracefully:** Use `BindingResult` to capture validation errors and return a meaningful `400 Bad Request` response. Never expose sensitive system information in error messages.
*   **Create Custom Constraints:** For complex business rules that aren't covered by standard annotations, create your own custom validation constraints.