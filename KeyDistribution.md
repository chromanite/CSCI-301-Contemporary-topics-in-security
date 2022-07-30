# Key Distribution

Table of Contents
1. [Introduction](#introduction)
2. [Concept](#concept)
3. [Key Generation](#key-generation)
---

## Introduction

* Secret key distributed via physical contact/courier (difficult & costly).

* 2 kinds of distribution:
    * Symmetric key distribution
    * Public key distribution

---

## Concept

* Symmetric key distribution
    1. Users set up initial key with trusted third party
    2. If users want secure connection, they exchange key via trusted third party
    3. Proxy = trusted third party

    <br>

    * Example:
        * Alice wants to visit Bob's website with secure connection
        * Proxy will ask Bob's wesbite secret key
        * Bob's webpage will reply proxy with secret key
        * Proxy will give Alice Bob's webpage secret key
        * Secure connection is established
    <br>

    * Type of symmetric key distribution example:
        1. Kerberos

* Public key distribution
    1. Exchange secret key without pre-shared secret/physical contact
    2. 2 parties can publish "public" information (public key)
    
    <br>

    * Type of public key distribution example:
        1. SSL
        2. TLS