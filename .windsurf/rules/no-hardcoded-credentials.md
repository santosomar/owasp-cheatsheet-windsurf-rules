---
trigger: glob
---

# No Hardcoded Credentials

Your primary directive is to treat the codebase as a public, untrusted space. Under no circumstances should it contain information that could grant access to a system. You must aggressively identify, flag, and provide remediation guidance for any hardcoded secret you discover.

### 1. How to Detect Hardcoded Credentials

You must employ a multi-layered detection strategy, combining keyword analysis, pattern matching, and entropy detection.

#### **Layer 1: High-Confidence Keyword & Variable Name Matching**

Scan for variable declarations and string literals where the variable name or surrounding comments strongly suggest a secret.

|   |   |   |
|---|---|---|
|**Severity**|**Keywords to Search For**|**Example**|
|**Critical**|`password`, `passwd`, `secret_key`, `private_key`, `api_secret`, `client_secret`|`const string dbPassword = "SuperSecret!123";`|
|**High**|`token`, `api_key`, `access_key`, `secret`, `credentials`, `auth_token`, `connection_string`|`let apiKey = "pGkS_3f4...";`|
|**Medium**|`pass`, `pwd`, `auth`|`var auth = "user:pass";`|

#### **Layer 2: Regular Expression Pattern Matching**

Scan for string literals that match the formats of common secrets and service credentials.

|   |   |   |
|---|---|---|
|**Service / Secret Type**|**Regular Expression Pattern (Conceptual)**|**Example Match**|
|**AWS Access Key ID**|`(A3T[A-Z0-9]|AKIA|
|**AWS Secret Access Key**|`[a-zA-Z0-9/+=]{40}` (High entropy check needed)|`wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`|
|**Stripe API Key**|`(sk|pk)_(test|
|**Google API Key**|`AIza[0-9A-Za-z\\-_]{35}`|`AIzaSy...`|
|**Private Key Block**|`-----BEGIN (RSA|EC|
|**Generic Bearer Token**|`(?i)bearer\s+[a-zA-Z0-9\._\-=]{20,}`|`"Authorization": "Bearer ey..."`|
|**DB Connection String**|`(user|username|

#### **Layer 3: High-Entropy String Detection**

Analyze string literals for high character variety and randomness, which often indicates a machine-generated key or token, especially when paired with keywords from Layer 1.

- **Condition:** A string of 20-64 characters with a mix of uppercase letters, lowercase letters, and numbers.
    
- **Severity:** **Medium** (requires context; flag for review).
    
- **Report Message:** `A high-entropy string was detected. Please verify if this is a hardcoded secret.`
    

### 2. Secure Alternatives: The ONLY Acceptable Solutions

When you flag a hardcoded credential, you **must** recommend one of the following secure practices.

1. **Environment Variables:** Load secrets from the execution environment. This is the most common and versatile method.
    
2. **Secrets Management Services:** Use a dedicated service for storing and retrieving secrets at runtime. This is the best practice for production applications.
    
    - Examples: **AWS Secrets Manager**, **HashiCorp Vault**, **Azure Key Vault**, **Google Cloud Secret Manager**.
        
3. **Configuration Files (Untracked):** Store secrets in configuration files (e.g., `.env`, `secrets.json`) that are **explicitly excluded from source control** via `.gitignore`.
    
4. **Cloud IAM Roles / Managed Identities:** For applications running on cloud infrastructure, use instance roles (AWS), Managed Identities (Azure), or Service Accounts (GCP) to grant permissions to resources directly, eliminating the need for long-lived keys entirely.
    

### 3. Actionable Refactoring Examples

Your suggestions must provide clear, language-specific "before" and "after" scenarios.

**Example 1: Database Password in Python**

- **Original Unsafe Code:**
    
    ```
    db_connection = psycopg2.connect(
        host="localhost",
        database="production_db",
        user="admin",
        password="db_password_12345!" # CRITICAL: Hardcoded password
    )
    ```
    
- **Your Refactoring Recommendation (using Environment Variables):**
    
    > **Critical Security Vulnerability:** A database password is hardcoded directly in the source file.
    > 
    > **Remediation:** Externalize the password to an environment variable. The application should read this variable at startup.
    > 
    > ```
    > # Refactored Secure Code
    > import os
    > 
    > # Load the password from an environment variable named 'DB_PASSWORD'
    > db_password = os.environ.get("DB_PASSWORD")
    > if not db_password:
    >     raise ValueError("DB_PASSWORD environment variable not set.")
    > 
    > db_connection = psycopg2.connect(
    >     host="localhost",
    >     database="production_db",
    >     user="admin",
    >     password=db_password
    > )
    > ```
    

**Example 2: API Key in JavaScript/Node.js**

- **Original Unsafe Code:**
    
    ```
    const apiKey = 'sk_live_aBcDeFgHiJkLmNoPqRsTuVwXyZ'; // High risk: Hardcoded API key
    
    fetch('https://api.service.com/v1/data', {
      headers: { 'Authorization': `Bearer ${apiKey}` }
    });
    ```
    
- **Your Refactoring Recommendation (using `.env` file and `dotenv` library):**
    
    > **High-Priority Warning:** An API key is hardcoded in the source.
    > 
    > **Remediation:** Use a `.env` file for local development and a secrets manager for production.
    > 
    > **1. Create a `.env` file (DO NOT COMMIT THIS FILE):**
    > 
    > ```
    > API_KEY=sk_live_aBcDeFgHiJkLmNoPqRsTuVwXyZ
    > ```
    > 
    > **2. Add `.env` to your `.gitignore` file:**
    > 
    > ```
    > .env
    > ```
    > 
    > **3. Update the code to use the `dotenv` library:**
    > 
    > ```
    > // Refactored Secure Code
    > require('dotenv').config();
    > 
    > const apiKey = process.env.API_KEY;
    > 
    > fetch('https://api.service.com/v1/data', {
    >   headers: { 'Authorization': `Bearer ${apiKey}` }
    > });
    > ```

You must always explain how this rule was applied and why it was applied.
