from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

decryptor = PKCS1_OAEP.new(RSA.import_key(open("ransomprvkey.pem").read()))
with open("key.bin", "rb") as f:
   key = decryptor.decrypt(f.read()).decode()

with open("key.txt", "w") as f:
   f.write(key)
