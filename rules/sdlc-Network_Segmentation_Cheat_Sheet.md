---
trigger: glob
globs: .yaml, .yml, .json, .conf, .ini, .tf, .sh, .env
---

## Network Segmentation Best Practices for Software Engineers

As a software engineer, how you design your application's architecture and network connectivity patterns has a significant impact on security. Proper network segmentation is essential to contain breaches, limit lateral movement, and protect sensitive resources.

### Multi-Layer Architecture Design

Implement a three-tier architecture model to enforce security boundaries:

1. **FRONTEND Layer** (Internet-facing)
   * Web servers, load balancers, CDNs, and API gateways
   * Receives external traffic and handles presentation logic
   * Limited to communicating only with the middleware layer

2. **MIDDLEWARE Layer** (Business Logic)
   * Application servers, authentication services, and business logic
   * Mediates all communication between frontend and backend
   * Enforces access control and validates requests

3. **BACKEND Layer** (Sensitive Data)
   * Databases, storage systems, and internal services
   * Contains sensitive data and critical systems
   * Never directly accessible from the frontend layer

### Implementation Guidelines

#### 1. Enforce Communication Patterns

Design your application to follow strict communication flows:

```
External Users → FRONTEND → MIDDLEWARE → BACKEND
                                 ↑
                                 ↓
                              BACKEND
```

**Incorrect Implementation:**
```yaml
# AVOID: Frontend service directly accessing database
frontend_service:
  environment:
    DATABASE_URL: "postgres://user:password@db.internal:5432/app_db"
```

**Correct Implementation:**
```yaml
# RECOMMENDED: Frontend only connects to middleware API
frontend_service:
  environment:
    API_ENDPOINT: "https://api.middleware.internal/v1"

# Middleware handles database access
middleware_service:
  environment:
    DATABASE_URL: "postgres://user:password@db.internal:5432/app_db"
```

#### 2. Network Access Control

* Define explicit allow rules rather than broad network access
* Implement host-based firewalls on all systems
* Use security groups or network policies in cloud/container environments

```terraform
# Example AWS security group for middleware tier
resource "aws_security_group" "middleware_sg" {
  # Allow incoming traffic only from frontend security group
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    security_groups = [aws_security_group.frontend_sg.id]
  }
  
  # Allow outgoing traffic only to backend security group
  egress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    security_groups = [aws_security_group.backend_sg.id]
  }
}
```

#### 3. Secure Service-to-Service Communication

* Implement mutual TLS (mTLS) between services
* Use service mesh technologies (like Istio, Linkerd) to enforce traffic policies
* Apply the principle of least privilege to all service accounts

```yaml
# Example Kubernetes network policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-policy
spec:
  podSelector:
    matchLabels:
      tier: backend
  ingress:
  - from:
    - podSelector:
        matchLabels:
          tier: middleware
    ports:
    - port: 5432
```

#### 4. Monitoring and Logging

* Forward all logs to a secure, centralized logging system
* Implement network traffic monitoring at segment boundaries
* Set up alerts for unusual cross-segment traffic patterns

```shell
# Example log forwarding configuration
auditd_conf="\
# Send logs to secure log server
log_format = ENRICHED
freq = 50
name = AUDIT_LOGS
max_log_file = 8
max_log_file_action = ROTATE
remote_server = log-collector.secure.internal
remote_port = 514
tcp_listen_port = 60
"

echo "$auditd_conf" > /etc/audit/auditd.conf
```

### Collaboration with Security Teams

* Work closely with network and security teams when designing application architecture
* Document network flows and security requirements for your application
* Participate in threat modeling sessions to identify potential network-based attacks

### Remember

Network segmentation is a critical defense-in-depth strategy, but it must be complemented by:

* Strong authentication and authorization at the application level
* Data encryption both in transit and at rest
* Regular security testing and vulnerability management
* Proper secret management and access control

By following these network segmentation principles, you'll significantly reduce the attack surface of your applications and limit the potential damage from security breaches.