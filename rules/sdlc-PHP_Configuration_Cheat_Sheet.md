---
trigger: glob
globs: .ini, .php
---

## PHP Secure Configuration Best Practices

As a software engineer working with PHP applications, properly configuring your PHP environment is crucial for security. This guide covers essential PHP configuration settings that should be implemented to harden your applications against common vulnerabilities.

### Basic Security Settings

#### Hide PHP Information

Prevent attackers from gathering information about your PHP version and configuration:

```ini
; Disable PHP version exposure in HTTP headers and error messages
expose_php = Off
```

#### Error Handling

Configure proper error handling to prevent information disclosure while ensuring errors are logged:

```ini
; Report all errors in development
error_reporting = E_ALL

; Hide errors from end users in production
display_errors = Off

; Enable error logging
log_errors = On

; Set a secure path for error logs (outside web root)
error_log = /var/log/php/error.log
```

In your application code, consider implementing environment-specific error handling:

```php
// In development environment
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// In production environment
ini_set('display_errors', 0);
ini_set('log_errors', 1);
ini_set('error_log', '/var/log/php/app_errors.log');
```

### Remote File Access

Restrict PHP's ability to access remote files to prevent Remote File Inclusion (RFI) attacks:

```ini
; Disable ability to open remote files
allow_url_fopen = Off

; Disable remote file inclusion
allow_url_include = Off
```

### File Upload Security

Manage file upload capabilities based on application requirements:

```ini
; Enable only if your application needs file uploads
file_uploads = On

; Limit upload size
upload_max_filesize = 2M
post_max_size = 8M

; Specify temporary upload directory (outside web root)
upload_tmp_dir = /var/php/uploads_tmp
```

When handling file uploads in your application, always implement additional validation:

```php
// Example of secure file upload handling
function secureFileUpload($file) {
    // Validate file type
    $allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
    if (!in_array($file['type'], $allowedTypes)) {
        return false;
    }
    
    // Generate safe filename
    $extension = pathinfo($file['name'], PATHINFO_EXTENSION);
    $safeFilename = bin2hex(random_bytes(16)) . '.' . $extension;
    
    // Move to secure location outside web root
    $uploadPath = '/var/www/uploads/' . $safeFilename;
    
    return move_uploaded_file($file['tmp_name'], $uploadPath) ? $safeFilename : false;
}
```

### Disable Dangerous Functions

Restrict potentially dangerous PHP functions that could be exploited for remote code execution:

```ini
; Disable functions that can execute system commands
disable_functions = exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,show_source,eval,assert
```

For applications requiring specific functions from this list, carefully review and only enable what's absolutely necessary.

### Session Security

Implement secure session handling to protect against session-based attacks:

```ini
; Prevent session fixation
session.use_strict_mode = 1

; Use cookies for session management (not URL parameters)
session.use_only_cookies = 1

; Secure cookie settings
session.cookie_secure = 1      ; Only send cookies over HTTPS
session.cookie_httponly = 1    ; Prevent JavaScript access to cookies
session.cookie_samesite = Strict  ; Mitigate CSRF attacks

; Set appropriate session lifetime
session.gc_maxlifetime = 3600  ; Session timeout (seconds)
```

Implement additional session security in your application code:

```php
// Regenerate session ID periodically
function secureSession() {
    if (!isset($_SESSION['last_regeneration'])) {
        regenerateSession();
    } else if ($_SESSION['last_regeneration'] < (time() - 1800)) {
        // Regenerate session ID every 30 minutes
        regenerateSession();
    }
}

function regenerateSession() {
    // Save current session data
    $sessionData = $_SESSION;
    
    // Clear session and generate new ID
    session_destroy();
    session_start();
    session_regenerate_id(true);
    
    // Restore session data
    $_SESSION = $sessionData;
    $_SESSION['last_regeneration'] = time();
}
```

### Open_basedir Restriction

Limit PHP's file system access to specific directories:

```ini
; Restrict PHP file operations to specific directories
open_basedir = /var/www/html:/var/php/uploads:/tmp
```

### Memory and Execution Limits

Set appropriate resource limits to prevent DoS attacks:

```ini
; Memory limit per script
memory_limit = 128M

; Maximum execution time for scripts (seconds)
max_execution_time = 30

; Maximum time for input processing
max_input_time = 60

; Limit POST data size
post_max_size = 8M
```

### Additional Security Measures

#### Content Security Policy

Implement Content Security Policy headers in your application:

```php
// Set CSP header
header("Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';");
```

#### Environment-Specific Configuration

Use different PHP configuration files for development and production environments:

```bash
# Development php.ini settings
php_admin_value[display_errors] = On
php_admin_value[error_reporting] = E_ALL

# Production php.ini settings
php_admin_value[display_errors] = Off
php_admin_value[error_reporting] = E_ALL & ~E_DEPRECATED & ~E_STRICT
```

#### Regular Security Audits

Regularly audit your PHP configuration using security scanning tools:

```bash
# Example command to check PHP configuration
php -i | grep -E "expose_php|allow_url|disable_functions|open_basedir"
```

By implementing these security best practices in your PHP configuration, you'll significantly reduce the attack surface of your PHP applications and protect against common vulnerabilities.
  - pattern-not: |
      session.name\s*=\s*myPHPSESSID
    message: 'Change the default session.name to a custom value to hinder session guessing.'
  - pattern: |
      enable_dl\s*=\s*On
    message: 'Set enable_dl = Off to prevent dynamic loading of PHP extensions at runtime.'
  - pattern-not: |
      memory_limit\s*=\s*\d+[MmGg]
    message: 'Set a reasonable memory_limit (e.g., 50M) to prevent resource exhaustion.'
  - pattern-not: |
      max_execution_time\s*=\s*\d+
    message: 'Set a reasonable max_execution_time (e.g., 60) to limit script runtime.'
  - pattern: |
      display_startup_errors\s*=\s*On
    message: 'Set display_startup_errors = Off on production servers to avoid leaking startup errors.'
  - pattern-not: |
      session.save_path\s*=\s*\/[^ ]+
    message: 'Set session.save_path to a secure directory accessible only by your application.'
  - pattern-not: |
      session.cookie_domain\s*=\s*[^ ]+
    message: 'Set session.cookie_domain to your actual domain to restrict cookie scope.'
  - pattern-not: |
      session.cookie_lifetime\s*=\s*\d+
    message: 'Configure session.cookie_lifetime according to your application needs (e.g., 14400 for 4 hours).'

recommendation: |
  Review and apply the recommended PHP configuration settings in your `php.ini`:
  - Keep `expose_php` OFF to hide PHP version.
  - Turn off `display_errors` and `display_startup_errors` in production.
  - Enable error logging with a secure `error_log` location.
  - Disable `allow_url_fopen` and `allow_url_include` to prevent remote file inclusion.
  - Disable all dangerous functions that your codebase doesn't need.
  - Harden session settings: use strict mode, secure and httponly cookies, set SameSite, customize session name.
  - Limit resource usage with memory_limit and max_execution_time.
  - Disable dynamic function loading (`enable_dl`).
  - Use secure paths for sessions and uploads.
  Additionally, consider deploying Snuffleupagus for advanced PHP protection.
