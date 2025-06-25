---
trigger: glob
globs: .rb, .erb, .haml, .slim, .yml, .yaml, .js, .jsx, .ts, .tsx
---

## Ruby on Rails Security Best Practices

As a Ruby on Rails developer, implementing proper security measures is essential to protect your application and its users. This guide covers key security best practices to help you build robust and secure Rails applications.

### Command Execution Security

Never use dangerous methods with untrusted input:

```ruby
# DANGEROUS - Never do this
eval(params[:code])                 # Executes arbitrary Ruby code
system("rm -rf #{params[:dir]}")   # Command injection vulnerability
`echo #{params[:input]}`            # Backticks execute shell commands
exec(params[:command])              # Direct command execution
```

Instead, use whitelisting and validation:

```ruby
# SAFE - Whitelist allowed commands
def restart_service
  allowed_services = %w[nginx postgresql redis]
  service_name = params[:service]
  
  if allowed_services.include?(service_name)
    system("service", service_name, "restart")  # Pass as separate arguments
  else
    flash[:error] = "Invalid service specified"
    redirect_to admin_path
  end
end
```

### SQL Injection Prevention

Always use parameterized queries and ActiveRecord methods:

```ruby
# DANGEROUS - SQL injection vulnerability
User.where("email = '#{params[:email]}'")  # DON'T DO THIS

# SAFE - Use parameterized queries
User.where("email = ?", params[:email])     # Good
User.where(email: params[:email])          # Better - hash syntax

# For LIKE queries, sanitize the input
search_term = ActiveRecord::Base.sanitize_sql_like(params[:query])
User.where("name LIKE ?", "%#{search_term}%")
```

### Cross-Site Scripting (XSS) Prevention

Rails automatically escapes HTML in ERB templates with `<%= %>`, but be careful with these exceptions:

```erb
<%# DANGEROUS - Bypasses HTML escaping %>
<%= raw user_provided_content %>
<%= user_provided_content.html_safe %>
<%== user_provided_content %>

<%# SAFE - Use default escaping %>
<%= user_provided_content %>
```

When you need to allow some HTML, use a proper sanitizer:

```ruby
# In your controller or helper
def sanitized_content(html_content)
  Rails::Html::Sanitizer.safe_list_sanitizer.sanitize(
    html_content,
    tags: %w[p br strong em ul li h1 h2 h3],
    attributes: %w[href title]
  )
end

# In your view
<%= sanitized_content(@user.profile_description) %>
```

### Content Security Policy

Implement a strong Content Security Policy:

```ruby
# In config/initializers/content_security_policy.rb
Rails.application.config.content_security_policy do |policy|
  policy.default_src :self
  policy.font_src    :self, 'https://fonts.gstatic.com'
  policy.img_src     :self, 'https://secure.example.com'
  policy.object_src  :none
  policy.script_src  :self
  policy.style_src   :self, 'https://fonts.googleapis.com'
  
  # Report CSP violations to this URL
  policy.report_uri  "/csp-violation-report"
end

# Enable automatic nonce generation for inline scripts
Rails.application.config.content_security_policy_nonce_generator = -> (request) { SecureRandom.base64(16) }
```

### Session Security

For applications with sensitive data, use a database-backed session store:

```ruby
# In config/initializers/session_store.rb
Rails.application.config.session_store :active_record_store, 
  key: '_app_session',
  secure: Rails.env.production?,
  httponly: true
```

Ensure proper session configuration:

```ruby
# In config/initializers/session_store.rb
Rails.application.config.session = {
  expire_after: 12.hours,
  key: '_secure_session',
  secure: Rails.env.production?,
  httponly: true
}
```

### Transport Layer Security

Force HTTPS in production:

```ruby
# In config/environments/production.rb
Rails.application.configure do
  config.force_ssl = true  # Enforces HTTPS, HSTS, and secure cookies
end
```

### Authentication Best Practices

Use established authentication gems like Devise:

```ruby
# In your Gemfile
gem 'devise'

# Configure password complexity
class User < ApplicationRecord
  devise :database_authenticatable, :registerable, :recoverable, :trackable,
         :validatable, :lockable, :timeoutable, :confirmable
         
  # Add custom password validation
  validate :password_complexity
  
  def password_complexity
    return if password.blank? || password =~ /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{12,}$/
    
    errors.add :password, 'must include uppercase, lowercase, number, and special character'
  end
end
```

### Authorization

Implement proper authorization using libraries like Pundit:

```ruby
# In your Gemfile
gem 'pundit'

# In app/policies/article_policy.rb
class ArticlePolicy < ApplicationPolicy
  def show?
    true  # Anyone can view articles
  end
  
  def create?
    user.present?  # Must be logged in to create
  end
  
  def update?
    user.present? && (user.admin? || record.user_id == user.id)
  end
  
  def destroy?
    user.present? && (user.admin? || record.user_id == user.id)
  end
end

# In your controller
class ArticlesController < ApplicationController
  before_action :authenticate_user!, except: [:index, :show]
  
  def update
    @article = Article.find(params[:id])
    authorize @article  # Checks policy
    
    if @article.update(article_params)
      redirect_to @article
    else
      render :edit
    end
  end
end
```

### CSRF Protection

Ensure CSRF protection is enabled:

```ruby
# In ApplicationController
class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  
  # For API endpoints that use token auth instead of session cookies
  protect_from_forgery with: :null_session, if: -> { request.format.json? }
end
```

Include CSRF tokens in forms:

```erb
<%= form_for @user do |f| %>
  <%# Rails automatically adds CSRF token with form_for/form_with %>
  <%= f.text_field :name %>
  <%= f.submit %>
<% end %>
```

For JavaScript requests:

```javascript
// In your application.js
const token = document.querySelector('meta[name="csrf-token"]').content;

fetch('/articles', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': token
  },
  body: JSON.stringify({ article: { title: 'New Article' } })
});
```

### Safe Redirects

Never redirect to user-provided URLs without validation:

```ruby
# DANGEROUS - Open redirect vulnerability
def after_sign_in
  redirect_to params[:return_to]  # DON'T DO THIS
end

# SAFE - Whitelist allowed redirect targets
def after_sign_in
  allowed_paths = [dashboard_path, profile_path, settings_path]
  redirect_path = params[:return_to]
  
  if redirect_path.present? && allowed_paths.include?(redirect_path)
    redirect_to redirect_path
  else
    redirect_to dashboard_path
  end
end
```

### Secure Rendering

Avoid user input in render paths:

```ruby
# DANGEROUS - Template injection vulnerability
def show
  render params[:template]  # DON'T DO THIS
end

# SAFE - Whitelist templates
def show
  allowed_templates = %w[basic detailed print]
  template = params[:template]
  
  if template.present? && allowed_templates.include?(template)
    render template
  else
    render :basic
  end
end
```

### CORS Configuration

Configure CORS carefully:

```ruby
# In Gemfile
gem 'rack-cors'

# In config/initializers/cors.rb
Rails.application.config.middleware.insert_before 0, Rack::Cors do
  allow do
    # Be specific with origins - avoid wildcards in production
    origins 'https://trusted-app.example.com', 'https://admin.example.com'
    
    resource '/api/*',
      headers: :any,
      methods: [:get, :post, :put, :patch, :delete, :options],
      credentials: true
  end
end
```

### Security Headers

Implement security headers:

```ruby
# In config/initializers/security_headers.rb
Rails.application.config.action_dispatch.default_headers = {
  'X-Frame-Options' => 'SAMEORIGIN',
  'X-XSS-Protection' => '1; mode=block',
  'X-Content-Type-Options' => 'nosniff',
  'X-Download-Options' => 'noopen',
  'X-Permitted-Cross-Domain-Policies' => 'none',
  'Referrer-Policy' => 'strict-origin-when-cross-origin'
}
```

### Secure Routing

Avoid catch-all routes that might expose unintended actions:

```ruby
# DANGEROUS - Exposes all actions
resources :users, controller: 'users'

# SAFE - Explicitly define allowed actions
resources :users, only: [:index, :show, :edit, :update]
```

### Sensitive Data Management

Use Rails credentials for sensitive data:

```ruby
# Edit credentials
$ EDITOR="vim" bin/rails credentials:edit

# In credentials file
aws:
  access_key_id: 123456
  secret_access_key: abcdef

stripe:
  publishable_key: pk_test_123
  secret_key: sk_test_456

# In your code
Rails.application.credentials.aws[:access_key_id]
```

### Dependency Management

Regularly update and audit dependencies:

```bash
# Update gems
bundle update --conservative

# Check for vulnerabilities
bundle audit

# Add to your CI pipeline
bundle exec bundler-audit check --update
```

### Security Testing Tools

Integrate security scanning into your development workflow:

```bash
# Install Brakeman
gem install brakeman

# Run scan
brakeman -o security_report.html

# Add to your CI pipeline
bundle exec brakeman -z
```

By following these security best practices, you'll build Rails applications that are significantly more resistant to common security vulnerabilities.

    Prefer sanitized markdown
    <%= markdown(user_input) %>

  session_store_setup: |
    # config/initializers/session_store.rb
    Rails.application.config.session_store :active_record_store, key: '_your_app_session'

  force_ssl: |
    # config/environments/production.rb
    config.force_ssl = true

  protect_from_forgery: |
    # app/controllers/application_controller.rb
    class ApplicationController < ActionController::Base
      protect_from_forgery with: :exception
    end

  safe_redirect: |
    Validate redirect URL or restrict to internal paths
    redirect_to(params[:return_to]) if allowed_url?(params[:return_to])
    # or
    redirect_to root_path, only_path: true

  authorization_example: |
    # Using Pundit
    def show
      @post = Post.find(params[:id])
      authorize @post
    end
