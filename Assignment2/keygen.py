#!/usr/bin/python3

from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

import os

for index in range(3):
    scriptSig = "OP_1"
    scriptPubkey = "OP_2"
    keygen_list = list()

    key = DSA.generate(2048)
    domain_param = key.domain()

    for _ in range(4):
        keygen = DSA.generate(bits=2048, domain=domain_param)
        scriptPubkey += " " + keygen.public_key().export_key().hex()
        keygen_list.append(keygen)

    for i in range(2):
        hash_msg = SHA256.new(b'Contemporary topic in security')
        signer = DSS.new(keygen_list[i], 'fips-186-3')
        scriptSig += " " + signer.sign(hash_msg).hex()

    os.mkdir(f"Pair{index + 1}")

    with open(f"Pair{index + 1}/scriptPubKey.txt", "w") as f:
        f.write(scriptPubkey + " OP_4 OP_CHECKMULTISIG")

    with open(f"Pair{index + 1}/scriptSig.txt", "w") as f:
        f.write(scriptSig)
