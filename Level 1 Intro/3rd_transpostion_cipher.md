# Transposition Ciphers

## What is a Transposition Cipher?

A **transposition cipher** is a method of encryption where the **positions of characters are rearranged** according to a fixed system, but the **characters themselves are not changed**.

### Relation with Substitution Cipher

| Cipher Type | What Changes | Example |
|------------|--------------|---------|
| Substitution Cipher | Characters are replaced with other characters | Caesar Cipher |
| Transposition Cipher | Positions of characters are rearranged | Rail Fence Cipher |

### Relation with AES (Advanced Encryption Standard)

AES is a **modern symmetric encryption algorithm** that uses both:
- **Substitution** (via S-boxes)
- **Transposition / Permutation** (rearranging bits)

This structure is known as a **Substitution–Permutation Network (SPN)**, which provides strong security compared to classical ciphers.

---


Resource : [Transposition Cipher](https://www.geeksforgeeks.org/computer-networks/transposition-cipher-techniques-in-cryptography/)

## Double Transpostion
In the following example, we use the keys **JANEAUSTEN** and **AEROPLANES** to encrypt the following plaintext: "Transposition ciphers scramble letters like puzzle pieces to create an indecipherable arrangement".



---

<details>
<summary><strong>Step 1: Write plaintext into first grid (Key: JANEAUSTEN)</strong></summary>

The plaintext message is written row-wise into the first grid using the key **JANEAUSTEN**.

![step-1-img](https://github.com/izahs-sec/NetSecCry/blob/main/photo/dt1.png)

</details>

---

<details>
<summary><strong>Step 2: Read columns alphabetically (Key: JANEAUSTEN)</strong></summary>

The columns are read off in **alphabetical order of the key letters**, producing an intermediate ciphertext.

![step-2-img](https://github.com/izahs-sec/NetSecCry/blob/main/photo/dt2.png)

</details>

---

<details>
<summary><strong>Step 3: Write intermediate text into second grid (Key: AEROPLANES)</strong></summary>

The output from Step 2 is written row-wise into the second grid using the key **AEROPLANES**.

![step-3-img](https://github.com/izahs-sec/NetSecCry/blob/main/photo/dt3.png)

</details>

---

<details>
<summary><strong>Step 4: Read columns alphabetically (Key: AEROPLANES)</strong></summary>

The columns are read again in alphabetical order to produce the final ciphertext.

![step-4-img](https://github.com/izahs-sec/NetSecCry/blob/main/photo/dt4.png)

</details>

---

<details>
<summary><strong>Step 5: Final Ciphertext</strong></summary>

The result after two rounds of columnar transposition is the final encrypted message.

![step-5-img](https://github.com/izahs-sec/NetSecCry/blob/main/photo/dt5.png)

</details>
