---
trigger: glob
globs: .php, .blade.php, .env
---

## Laravel Security Best Practices

As a Laravel developer, following these security best practices will help you build robust and secure web applications. Laravel provides many security features out of the box, but they need to be configured and used correctly.

### Environment Configuration

#### Disable Debug Mode in Production

Exposing detailed error messages in production can reveal sensitive information to attackers.

```env
# CORRECT: Production environment setting
APP_ENV=production
APP_DEBUG=false

# INCORRECT: Never use this in production
APP_DEBUG=true
```

#### Generate and Secure Application Key

The application key is used for encrypting sessions, cookies, and other sensitive data.

```bash
# Generate a secure application key
php artisan key:generate
```

Verify your `.env` file contains a valid `APP_KEY` value that is 32 characters long.

### File System Security

Set appropriate file permissions to prevent unauthorized access:

* Files: `644` or `664` (owner read/write, group read/write, others read)
* Directories: `755` or `775` (owner read/write/execute, group read/write/execute, others read/execute)
* Storage and cache directories may need write permissions for the web server user

### Cookie and Session Security

#### Enable Cookie Encryption

Ensure the `EncryptCookies` middleware is registered in `app/Http/Kernel.php`:

```php
protected $middlewareGroups = [
    'web' => [
        \App\Http\Middleware\EncryptCookies::class,
        // other middleware...
    ],
];
```

#### Configure Secure Cookie Settings

Update your `.env` and `config/session.php` files:

```env
# Recommended settings for production
SESSION_DRIVER=redis  # or another secure driver
SESSION_SECURE_COOKIE=true  # for HTTPS sites
SESSION_HTTP_ONLY=true
SESSION_SAME_SITE=lax  # or 'strict' for higher security
```

```php
// In config/session.php
return [
    'lifetime' => 30,  // 30 minutes is a good balance
    'secure' => env('SESSION_SECURE_COOKIE', true),
    'http_only' => true,
    'same_site' => 'lax',
];
```

### Authentication

Leverage Laravel's official authentication packages instead of building custom solutions:

* **Laravel Breeze**: Lightweight authentication with Blade templates
* **Laravel Fortify**: Backend authentication without opinions on the frontend
* **Laravel Jetstream**: Full authentication and team management with either Livewire or Inertia.js

### Input Validation and Mass Assignment Protection

#### Never Trust User Input

Always validate user input using Laravel's validation features:

```php
// GOOD: Validate input before using
$validated = $request->validate([
    'name' => 'required|string|max:255',
    'email' => 'required|email|unique:users',
]);

// BETTER: Create a dedicated Form Request
class UserRequest extends FormRequest
{
    public function rules()
    {
        return [
            'name' => 'required|string|max:255',
            'email' => 'required|email|unique:users',
        ];
    }
}
```

#### Prevent Mass Assignment Vulnerabilities

```php
// UNSAFE: Using all request data without filtering
$user = User::create($request->all());  // AVOID THIS

// SAFE: Explicitly specify allowed fields
$user = User::create($request->only(['name', 'email']));

// BETTER: Use validated data
$user = User::create($validated);
```

Always define either `$fillable` or `$guarded` properties in your models.

### SQL Injection Prevention

Use Eloquent ORM or query builder with parameter binding:

```php
// UNSAFE: Raw concatenated query
$results = DB::select("SELECT * FROM users WHERE email = '" . $email . "'");  // VULNERABLE

// SAFE: Using query builder with parameter binding
$results = DB::table('users')->where('email', $email)->get();

// SAFE: If raw queries are necessary, use bindings
$results = DB::select("SELECT * FROM users WHERE email = ?", [$email]);
```

### XSS Prevention

Use Blade's automatic escaping for all untrusted data:

```blade
{{-- SAFE: Automatically escaped --}}
<div>{{ $userInput }}</div>

{{-- UNSAFE: Avoid this with untrusted input --}}
<div>{!! $userInput !!}</div>
```

### File Upload Security

Implement strict validation for file uploads:

```php
$request->validate([
    'document' => 'required|file|mimes:pdf,docx|max:2048',  // 2MB max
]);

// Sanitize the filename
$filename = basename($file->getClientOriginalName());

// Store in a non-public location when possible
$path = $request->file('document')->store('documents');
```

### CSRF Protection

Ensure the `VerifyCsrfToken` middleware is enabled and add CSRF tokens to all forms:

```blade
<form method="POST" action="/profile">
    @csrf
    <!-- Form fields -->
</form>
```

For AJAX requests, include the CSRF token in the header:

```javascript
axios.defaults.headers.common['X-CSRF-TOKEN'] = document.querySelector('meta[name="csrf-token"]').content;
```

### Command Injection Prevention

Never pass unescaped user input to shell commands:

```php
// UNSAFE: Direct user input in shell command
shell_exec('convert ' . $userInput . ' output.jpg');  // VULNERABLE

// SAFE: Escape shell arguments
$safeInput = escapeshellarg($userInput);
shell_exec('convert ' . $safeInput . ' output.jpg');
```

### Security Headers

Implement security headers using middleware:

```php
// In a middleware
public function handle($request, Closure $next)
{
    $response = $next($request);
    
    $response->headers->set('X-Frame-Options', 'SAMEORIGIN');
    $response->headers->set('X-Content-Type-Options', 'nosniff');
    $response->headers->set('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
    
    return $response;
}
```

### Regular Security Auditing

* Use the Enlightn Security Checker to scan for vulnerabilities
* Keep Laravel and all dependencies updated
* Run `composer audit` regularly to check for known vulnerabilities
* Consider integrating security scanning into your CI/CD pipeline

By following these best practices, you'll significantly improve the security posture of your Laravel applications.
