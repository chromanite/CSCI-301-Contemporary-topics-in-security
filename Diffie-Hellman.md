# Diffe-Hellman

Table of Contents
1. [Introduction](#introduction)
2. [Concept](#concept)
3. [Key Generation](#key-generation)
---

## Introduction

* Allows 2 parties to agree on secret key over insecure channel without 3rd party/physical contract

---

## Concept

* Alice and Bob have a random number as private key `a` and `b`

* Alice sends her public key `g^a mod p` to Bob

* Bob sends his public key `g^b mod p` to Alice

* Alice and Bob then compute `g^(ba)` and `g^(ab)` to get K(bob) and K(alice) respectively

* Both parties can use `K(alice)` and `K(bob)` to encrypt and decrypt messages

---

## Key Generation

* `p`: prime number

* `g`: generator

* `a`: Alice's private key containing a random number

* `b`: Bob's private key containing a random number

* Alice's public key = `g^a mod p`

* Bob's public key = `g^b mod p`

* K(alice) = `g^(ab) mod p`

* K(bob) = `g^(ba) mod p`


