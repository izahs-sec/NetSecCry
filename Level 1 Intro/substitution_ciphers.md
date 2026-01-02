### Substitution Ciphers

<details> 
<summary><strong><a href="https://www.geeksforgeeks.org/python/substitution-cipher/">Caesar Cipher</a></strong></summary>

The Caesar Cipher is a basic substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

</details>

<details>
<summary><strong><a href="https://www.geeksforgeeks.org/computer-networks/what-is-monoalphabetic-cipher/">Monoalphabetic Cipher</a></strong></summary>

### Types of Monoalphabetic Ciphers
- Additive Cipher (Caesar Cipher)
- Multiplicative Cipher
- Affine Cipher

---

### How Monoalphabetic Cipher Works
A **Monoalphabetic Cipher** uses a **single fixed substitution alphabet** for encryption.  
Each letter in the plaintext is replaced by a corresponding letter from the cipher alphabet.  
Once a letter is substituted, the **same substitution is applied throughout the entire message**.

The mapping between plaintext letters and ciphertext letters **does not change**, which makes encryption simple but predictable.

---

### Short Description of Monoalphabetic Cipher Types

#### 1. Additive Cipher (Caesar Cipher)
Each plaintext letter is shifted by a fixed number of positions.

**Formula:**  
C = (P + K) mod 26  

#### 2. Multiplicative Cipher
Each plaintext letter is multiplied by a key value.

**Formula:**  
C = (P × K) mod 26  

#### 3. Affine Cipher
A combination of multiplicative and additive operations.

**Formula:**  
C = (P × K₁ + K₂) mod 26  

---

### Advantages of Monoalphabetic Cipher
- Simple and easy to understand  
- Easy to implement  
- Faster encryption and decryption  
- Requires minimal computational resources  

### Disadvantages of Monoalphabetic Cipher
- Vulnerable to frequency analysis attacks  
- Same letter always maps to the same ciphertext letter  
- Low level of security  
- Not suitable for modern secure communication  

</details>

<details> 
<summary><strong><a href="">Polyalphabetic Cipher</a></strong></summary>

A Polyalphabetic Cipher uses multiple substitution alphabets to encrypt the plaintext, making frequency analysis more difficult.

</details>

<details> 
<summary><strong><a href="https://www.tutorialspoint.com/cryptography/cryptography_playfair_cipher.htm">Playfair Cipher</a></strong></summary>

The Playfair Cipher encrypts pairs of letters (digraphs) using a 5×5 key matrix generated from a keyword.

Problem-1: [Playfair Cipher ](https://www.youtube.com/watch?v=z4hrHlVvUu4)

</details>

<details> 
<summary><strong><a href="https://www.tutorialspoint.com/cryptography/cryptography_hill_cipher.htm">Hill Cipher</a></strong></summary>

The Hill Cipher is a polygraphic substitution cipher that uses **matrix multiplication** and linear algebra to encrypt blocks of plaintext. 



Problem-1: [Playfair Cipher ](https://www.youtube.com/watch?v=ytJAdBLNjn0)

Problem-2: [GFG](https://www.geeksforgeeks.org/dsa/hill-cipher/)


</details>

<details> 
<summary><strong><a href="https://www.tutorialspoint.com/cryptography/cryptography_one_time_pad_cipher.htm">One-Time Pad</a></strong></summary>

Vernam Cipher (general idea)

Invented by Gilbert Vernam (1917)

Uses:

A plaintext

A key

Encryption is done using XOR (⊕) or modular addition

The key does not have to be truly random and may be reused

📌 Because of this, Vernam cipher is not always secure.

One-Time Pad (OTP)

OTP is the secure version of the Vernam cipher, with strict rules:

Key is truly random

Key length = message length

Key is used only once

Key is kept secret

When these conditions are met:
✔ OTP is unbreakable (perfect secrecy – proved by Claude Shannon)

| Feature           | Vernam Cipher  | One-Time Pad         |
| ----------------- | -------------- | -------------------- |
| Encryption method | XOR / addition | XOR / addition       |
| Key length        | Can be shorter | Same as message      |
| Key randomness    | Not required   | Required             |
| Key reuse         | Allowed        | **Not allowed**      |
| Security          | Conditional    | **Perfect security** |




Problem-1: [OTP Cipher](https://www.youtube.com/watch?v=2JzhqHxUy5E)

[Resource](hhttps://www.geeksforgeeks.org/dsa/implementation-of-vernam-cipher-or-one-time-pad-algorithm/)

</details>

<details> 
<summary><strong><a href="https://www.tutorialspoint.com/cryptography/cryptography_vigenere_cipher.htm">Vigenere Cipher</a></strong></summary>

The Vigenere Cipher uses multiple Caesar ciphers based on a keyword to encrypt the plaintext.  

Problem-1: [Vigenere Cipher Video](https://www.youtube.com/watch?v=GQrKEwLZcPY)

**Handle negative values:**  
For example:  -7 mod 26 = (-7 + 26) mod 26 = 19

**Tabula Recta**
![CIA Triad](https://github.com/izahs-sec/NetSecCry/blob/main/photo/tabula-recta.png)