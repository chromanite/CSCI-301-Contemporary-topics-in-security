# Public Key Encrpytion

Table of Contents
1. [Introduction](#introduction)
2. [Concept](#concept)
3. [Key Generation](#key-generation)
---

## Introduction

* Share secret between two users who do not share secret in advance

* Public Key:
    * Published to public

* Secret Key:
    * Owner must keep secret key

---

## Concept

* Alice and Bob creates PK and SK each

* Alice and Bob share their PK with each other
    * Alice: Bob's PK and her own SK
    * Bob: Alice's PK and his own SK

* Alice wants to send message to Bob
    1. Ciphertext = encrypt(Alice's Message, Bob's PK)

* Bob wants to receive message from Alice
    1. Alice's Message = decrypt(Ciphertext, Alice's SK)

* Bob replies to Alice's message
    1. Ciphertext = encrypt(Bob's Message, Alice's PK)

* Alice wants to receive message from Bob
    1. Bob's Message = decrypt(Ciphertext, Bob's SK)

---

## Key Generation

* `C`: ciphertext 

* `M`: message to be encrypted be the integer M with 0 <= M < pq.

* `N` = p * q, p and q are prime numbers

* `e`: positive integer that is relatively prime to (p-1) * (q-1) 

* `Public Key`: (N, e)

* `Secret Key`: (N, d)

* encryption(Public Key, Message) = `M^e` (mod `N`)

* decryption(Secret Key, Ciphertext) = `C^d` (mod `N`)
