# Hash Functions in Cryptography

## Overview

A **hash function** is a mathematical algorithm that takes an input of **arbitrary (variable) length** and produces an output of **fixed length**, known as a *hash value* or *message digest*. Hash functions are widely used in cryptography for ensuring **data integrity**, **authentication**, and **security**.

Common cryptographic hash functions include **SHA-256**, **SHA-3**, **MD5** and **BLAKE2**.

---

### Terminology

<details>
<summary><strong>Variable-to-Fixed Length Coding</strong></summary>

- Maps input of any size to a **fixed-size hash**  
- Example: SHA-256 always outputs 256 bits regardless of input length  

</details>

<details>
<summary><strong>Pre-image Resistance</strong></summary>

- Given a hash `h`, it is **computationally infeasible** to find the original input `m` such that `hash(m) = h`  
- Protects against **reverse engineering** of hashed data  

</details>

<details>
<summary><strong>Second Pre-image Resistance</strong></summary>

- Given a message `m₁`, it is **computationally infeasible** to find a different message `m₂` such that `hash(m₁) = hash(m₂)`  
- Prevents **substituting one message for another** without detection  

</details>

<details>
<summary><strong>Collision Resistance</strong></summary>

- It is **computationally infeasible** to find **any two distinct messages** `m₁` and `m₂` with the same hash  
- Ensures **unique hashes** for different messages  

</details>

---

### Why use it?


<details>
<summary><strong>Answer</strong></summary>

Hash functions are used to **verify data integrity** by ensuring that a copy of a file or message matches the original.  

- Example: When downloading a Linux ISO or software from a repository, hashes confirm the file is identical to the original.  
- The property of **uniqueness** is critical: two different inputs producing the same hash is called a **collision**, which undermines security.  
  - Example: MD5 is now deprecated because collisions are easy to generate.  
- Hash functions also exhibit the **avalanche effect**: even a tiny change in input produces a drastically different hash.  

<details>
<summary><strong>Typical Uses of Hash Functions</strong></summary>

Hash functions are primarily used to **verify data integrity** and **authenticate files**:

- All digital data—text, executables, videos, images, databases—can be hashed.
- Comparing large files directly is slow; hashes allow **quick comparison**.
- Hashes are used in **digital signatures**, signing the hash instead of the full data.
- Before running a file, you can hash it and compare it to a known hash to ensure it hasn’t been tampered with.

</details>

</details>

<details>
<summary><strong>CHF Properties (Cryptographic Hash Function)</strong></summary>

An ideal cryptographic hash function has the following properties:

- **Deterministic:** The same input always produces the same hash.
- **Fast computation:** The hash value can be computed quickly for any message.
- **Pre-image resistance:** It is infeasible to generate a message that produces a given hash.
- **Collision resistance:** It is infeasible to find two different messages with the same hash.
- **Avalanche effect:** A small change in the input drastically changes the output, making it appear uncorrelated with the original hash.

</details>

