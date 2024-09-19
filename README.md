# Length Extension Attacks

## Cryptographic Hash Function Vulnerabilities: Length Extension Attacks
This presentation explores the concept of **length extension attacks**, a vulnerability that exploits weaknesses in the design of cryptographic hash functions. These attacks enable malicious actors to forge digital signatures and tamper with data, compromising data integrity and security.

**Author**: Salvatore Adduci  
**Student ID**: 247514

---

### Overview of Cryptographic Hash Functions
1. **One-way Functions**: Hash functions take input data and produce a fixed-length hash value, making it computationally infeasible to reverse engineer the original data.
2. **Collision Resistance**: It's computationally infeasible to find two different inputs that produce the same hash value.
3. **Preimage Resistance**: Given a hash value, it’s extremely difficult to find the original input.
4. **Second Preimage Resistance**: For a given input, it’s nearly impossible to find a different input that produces the same hash value.

---

### Vulnerabilities in Hash Functions
1. **Iterative Structure**: Functions like MD5 and SHA-1 use the Merkle-Damgård construction, making them vulnerable if the internal state is exposed.
2. **Length Extension Attack**: Attackers can compute valid hashes for extended data without knowing the secret key by exploiting the iterative nature of the hash construction.

---

### Length Extension Attack Explained
In a typical scenario:
- The server hashes a message with a secret key (`H(K || M)`).
- The attacker, who doesn’t know the key, can extend the message (`M || M2`) and compute a valid hash for it.

---

### Mitigation Techniques
1. **HMAC**: By using HMAC, the hash is protected, preventing attackers from extending the message.
2. **Stronger Hash Functions**: SHA-3, based on sponge construction, is immune to length extension attacks.
3. **Secure Code Practices**: Ensuring secure coding practices is crucial to prevent these vulnerabilities.

---

### Case Study: Flickr API Vulnerability
In 2014, the **Flickr API** was found vulnerable to length extension attacks due to the use of unsalted MD5 hashes. Attackers could append data to API requests and generate valid hashes, compromising user data.

---

### Demo
A demonstration of the length extension attack can be found [here](https://docs.google.com/file/d/19yz_0rmNW-91iqT8UvfQNqhzAW9KiHDN/preview).

---

### Conclusion
To mitigate length extension attacks, developers should use modern hash functions like SHA-3 and implement HMAC for secure message authentication.

---

**Thank you for your attention!**

