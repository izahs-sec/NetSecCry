---

## Classical Ciphers


---

## Classical Ciphers

Classical ciphers are early methods of encryption that rely on simple mathematical or logical transformations of text. They form the foundation of modern cryptography.

## 🔐 Scytale Cipher

The **Scytale** is one of the earliest known encryption techniques, used by the **ancient Spartans** (around 5th century BCE).

### How it works
- A strip of parchment is wrapped around a rod (the *scytale*)
- The message is written along the rod
- When unwrapped, the letters appear scrambled
- Only someone with a rod of the **same diameter** can read the message

### Key Points
- Type: **Transposition cipher**
- Security depends on the rod size
- Vulnerable to brute-force guessing of rod diameter

---

## 🔄 Substitution Cipher

In a **substitution cipher**, each letter in the plaintext is replaced with another letter.

### Example


### Characteristics
- Type: **Monoalphabetic cipher**
- Same substitution used throughout the message
- Easy to implement but weak by modern standards

---

### 🧠 Breaking Substitution Ciphers
Substitution ciphers can be broken using **frequency analysis**.

#### Frequency Analysis
- Certain letters appear more often in a language
  - English: `E, T, A, O, I, N`
- By analyzing letter frequencies in the ciphertext, attackers can guess substitutions

---

## 🔁 Polyalphabetic Cipher

A **polyalphabetic cipher** uses **multiple substitution alphabets**, making it harder to break with frequency analysis.

### Historical Background
- First described by **Al-Kindi** in the **9th century**
  - He also developed frequency analysis
- Later formally explained by **Leon Battista Alberti** in **1467**

### Advantages
- Same plaintext letter can encrypt to different ciphertext letters
- More secure than monoalphabetic ciphers

---

## 📊 Tabula Recta

The **Tabula Recta** is a table used in many polyalphabetic ciphers, most notably the **Vigenère cipher**.

### Description
- A 26×26 table of alphabets
- Each row is a shifted version of the alphabet
- Rows represent plaintext letters
- Columns represent key letters

### Why it matters
- Enables systematic encryption and decryption
- Foundation of many classical cipher systems

---

<details>
<summary>📌 Summary (Click to expand)</summary>

- **Scytale** → Transposition cipher using a physical rod  
- **Substitution cipher** → One-to-one letter replacement  
- **Frequency analysis** → Method to break substitution ciphers  
- **Polyalphabetic cipher** → Uses multiple alphabets  
- **Tabula Recta** → Alphabet table used in encryption  

</details>

---
