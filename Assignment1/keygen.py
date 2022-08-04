from Crypto.PublicKey import RSA

key = RSA.generate(2048)

with open("public.pem", "wb") as f:
    f.write(key.publickey().export_key())

with open("ransomprvkey.pem", "wb") as f:
    f.write(key.export_key())