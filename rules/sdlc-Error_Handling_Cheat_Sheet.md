---
trigger: glob
globs: [java, jsp, cs, config, json, xml]
---


message: Secure Error Handling - avoid leaking sensitive details, log errors securely, and return generic error messages.

languages: [java, csharp, xml, json]
categories: [security, error-handling, best-practice]

description: >
  Ensure all unhandled exceptions are caught by a global error handler that returns generic error responses 
  without exposing sensitive information such as stack traces, server paths, or technology versions.
  Log full error details securely on the server for diagnostics and monitoring. Use correct HTTP status codes 
  (4xx for client errors, 5xx for server errors) and follow standards like RFC 7807 for API error payloads.

recommendation: >
  - Implement a centralized/global error handler to catch all exceptions.
  - Return user-friendly, generic error messages without internal details.
  - Log detailed error info securely on the server (stack traces, request context).
  - Use HTTP status codes correctly to distinguish client vs server errors.
  - For REST APIs, adopt RFC 7807 Problem Details format for consistent error responses.
  - In production, disable detailed error pages or debug info visible to clients.
  - Follow your framework-specific guidelines (e.g., @RestControllerAdvice in Spring Boot, UseExceptionHandler middleware in ASP.NET Core).
  - Monitor and alert on 5xx errors for proactive issue detection.
  
examples:
  - language: java
    example: |
      // Spring Boot global exception handler example
      @RestControllerAdvice
      public class GlobalExceptionHandler {
      
          private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
      
          @ExceptionHandler(Exception.class)
          public ResponseEntity<ProblemDetail> handleAllExceptions(Exception ex) {
              logger.error("Unhandled exception caught: ", ex);
              ProblemDetail problem = ProblemDetail.forStatus(HttpStatus.INTERNAL_SERVER_ERROR);
              problem.setTitle("Unexpected error");
              problem.setDetail("An internal error occurred. Please try again later.");
              return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(problem);
          }
      }

  - language: csharp
    example: |
      // ASP.NET Core error handling middleware setup
      app.UseExceptionHandler("/api/error");
      
      [ApiController]
      [Route("api/error")]
      public class ErrorController : ControllerBase {
          private readonly ILogger<ErrorController> _logger;
          public ErrorController(ILogger<ErrorController> logger) {
              _logger = logger;
          }
      
          [HttpGet]
          public IActionResult HandleError() {
              var exception = HttpContext.Features.Get<IExceptionHandlerFeature>()?.Error;
              _logger.LogError(exception, "Unhandled exception caught");
              Response.Headers.Add("X-ERROR", "true");
              return Problem(title: "Unexpected error", statusCode: 500, detail: "An internal error occurred. Please try again later.");
          }
      }
  
  - language: xml
    example: |
      <!-- web.xml sample for Java Servlets -->
      <error-page>
          <exception-type>java.lang.Exception</exception-type>
          <location>/error.jsp</location>
      </error-page>
      
      <!-- web.config fragment for ASP.NET Web API -->
      <configuration>
          <system.web>
              <customErrors mode="RemoteOnly" defaultRedirect="Error.htm">
                  <error statusCode="500" redirect="Error.htm"/>
              </customErrors>
          </system.web>
      </configuration>

notes: >
  Avoid showing any technical detail in error responses. Use server logs and secure monitoring tools to troubleshoot.
  Remember to disable detailed error messages on production environments.
```
