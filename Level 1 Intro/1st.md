# Cryptography – Hierarchical Classification

## 1. Cryptography (Root)
The science of securing information using mathematical techniques.

---

## 2. Classical Cryptography
Techniques used before computers; mostly historical.

### 2.1 Substitution Ciphers
- Caesar Cipher
- Monoalphabetic Cipher
- Vigenère Cipher
- Playfair Cipher

### 2.2 Transposition Ciphers
- Rail Fence Cipher
- Columnar Transposition Cipher

### 2.3 Polyalphabetic Ciphers
- Vigenère Cipher
- Autokey Cipher

---

## 3. Modern Cryptography
Computer-based cryptography relying on mathematics and algorithms.

---

## 4. Symmetric-Key Cryptography
Same key used for encryption and decryption.

### 4.1 Block Ciphers
- DES (Data Encryption Standard)
- 3DES
- AES (Advanced Encryption Standard)
- Blowfish
- Twofish

### 4.2 Stream Ciphers
- One-Time Pad (OTP)
- RC4 (deprecated)
- ChaCha20
- Salsa20


### 4.3 Modes of Operation
- ECB (Electronic Codebook)
- CBC (Cipher Block Chaining)
- CFB (Cipher Feedback)
- OFB (Output Feedback)
- CTR (Counter Mode)
- GCM (Galois/Counter Mode)

---

## 5. Asymmetric-Key Cryptography (Public-Key Cryptography)
Uses a public key and a private key.

### 5.1 Encryption Algorithms
- RSA
- ElGamal
- ECC (Elliptic Curve Cryptography)

### 5.2 Key Exchange Algorithms
- Diffie–Hellman
- Elliptic Curve Diffie–Hellman (ECDH)

---

## 6. Cryptographic Hash Functions
One-way functions that produce fixed-size output.

### 6.1 General-Purpose Hash Functions
- MD5 (deprecated)
- SHA-1 (deprecated)
- SHA-2 (SHA-256, SHA-512)
- SHA-3

### 6.2 Password Hashing Functions
- bcrypt
- scrypt
- Argon2
- PBKDF2

---

## 7. Message Authentication & Integrity
Ensures data integrity and authenticity.

### 7.1 Message Authentication Codes (MAC)
- HMAC
- CMAC

### 7.2 Digital Signatures
- RSA Signatures
