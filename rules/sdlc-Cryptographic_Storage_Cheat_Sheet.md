---
trigger: glob
globs: .js, .ts, .java, .py, .rb, .go, .cs, .cpp, .c, .swift, .kt, .m
---

## Secure Cryptographic Storage: A Guide for Software Engineers

Implementing cryptography correctly is challenging but essential for protecting sensitive data. This guide covers best practices for secure cryptographic storage in your applications.

### 1. Password Storage: Special Considerations

Passwords require special handling and should never use standard encryption:

* **Use Dedicated Password Hashing Algorithms:**
  * Argon2id (preferred): Designed to be resistant against both GPU and ASIC attacks
  * bcrypt: Still strong, widely available, use cost factor ≥ 10
  * PBKDF2: Use only when other options aren't available, with 310,000+ iterations

```java
// Java example using jBCrypt
String hashedPassword = BCrypt.hashpw(password, BCrypt.gensalt(12)); // Cost factor 12

// Verification
boolean matched = BCrypt.checkpw(candidatePassword, hashedPassword);
```

### 2. Selecting Cryptographic Algorithms

* **Symmetric Encryption:**
  * Use AES-256 for most use cases
  * ChaCha20-Poly1305 is a good alternative, especially on mobile/low-power devices

* **Asymmetric Encryption:**
  * Elliptic Curve Cryptography (ECC): Use Curve25519 for encryption, Ed25519 for signatures
  * RSA: Use ≥ 2048 bits (3072+ preferred for long-term security)

* **Hashing:**
  * Use SHA-256 or SHA-3 for general purpose hashing
  * BLAKE2 or BLAKE3 are excellent modern alternatives

### 3. Authenticated Encryption: Always Required

Always use authenticated encryption modes to ensure both confidentiality and integrity:

```python
# Python example using authenticated encryption with AES-GCM
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# Generate a key
key = AESGCM.generate_key(bit_length=256)

# Generate a random nonce
nonce = os.urandom(12)

# Encrypt data with associated data for authentication
cipher = AESGCM(key)
encrypted_data = cipher.encrypt(nonce, plaintext, associated_data)

# Decryption will raise an exception if authentication fails
decrypted = cipher.decrypt(nonce, encrypted_data, associated_data)
```

### 4. Secure Random Number Generation

Never use standard random functions for cryptographic purposes:

```javascript
// JavaScript: WRONG
const insecureRandom = Math.random(); // Never use for crypto!

// JavaScript: RIGHT
const secureRandom = new Uint8Array(16);
window.crypto.getRandomValues(secureRandom);
```

### 5. Key Management Lifecycle

Implement a complete key management lifecycle:

* **Key Generation:** Use a cryptographically secure random number generator (CSPRNG)
* **Key Storage:** Use dedicated key management systems (AWS KMS, HashiCorp Vault, Azure Key Vault)
* **Key Rotation:** Establish policies for regular key rotation (e.g., annually or after staff changes)
* **Key Revocation:** Have procedures ready for compromised key scenarios

### 6. Secure Key Storage

* **Never hardcode keys** in source code or configuration files
* **Use envelope encryption** - encrypt data keys with key encryption keys
* **Implement access controls** on key access

```go
// Go example of envelope encryption
func encryptData(plaintext []byte, kek []byte) ([]byte, []byte, error) {
    // Generate a data encryption key (DEK)
    dek := make([]byte, 32)
    if _, err := rand.Read(dek); err != nil {
        return nil, nil, err
    }
    
    // Encrypt the DEK with the key encryption key (KEK)
    encryptedDek := encryptWithAESGCM(dek, kek)
    
    // Encrypt the actual data with the DEK
    encryptedData := encryptWithAESGCM(plaintext, dek)
    
    return encryptedData, encryptedDek, nil
}
```

### 7. Defense in Depth

* **Minimize sensitive data storage** - don't store what you don't need
* **Implement proper access controls** alongside encryption
* **Log and monitor** access to encrypted data
* **Use TLS** for data in transit

### 8. Common Pitfalls to Avoid

* **Don't implement your own crypto** - use vetted libraries
* **Don't use ECB mode** - it doesn't hide data patterns
* **Don't reuse IVs/nonces** - this can completely break encryption security
* **Don't store encryption keys alongside encrypted data**

By following these guidelines, you'll significantly improve the security of sensitive data in your applications. Remember that cryptography is just one layer in a comprehensive security strategy.
