#!/usr/bin/python3

from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

stack = list()
sig_list = list()                     # create a list to store the signatures
key_list = list()                     # create a list to store the keys
log_file = open("log.txt", "w")       # create a log file


def read_file(signature_file, publickey_file) -> list():
    try:
        with open(f"{signature_file}.txt", "r") as scriptSig, open(f"{publickey_file}.txt", "r") as scriptPubKey:
            scriptSig_List = scriptSig.readline().split(" ")
            scriptPubKey_List = scriptPubKey.readline().split(" ")
            return scriptSig_List, scriptPubKey_List
    except FileNotFoundError:
        print("File not found! Terminating...")
        exit()


def extract_signature() -> None:
    if sig_list.pop(0) == "OP_1":
        fprint("Start of scriptSig")
        while sig_list:
            stack.append(sig_list.pop(0))
            fprint(f"stack: {stack}",)
        fprint("End of script signature")
    else:
        print("[!] Error: OP_1 not found, wrong scriptSig file?")


def extract_keys() -> None:
    fprint("\n\nStart of script Public Key")
    sig_num = int(key_list.pop(0).split("OP_")[1])
    if len(stack) == sig_num:
        stack.append(sig_num)
        fprint(f"stack: {stack}",)
        while stack:
            key = key_list.pop(0)
            if key.startswith("OP_"):
                opcode = key.split("OP_")[1]
                if opcode == "CHECKMULTISIG":
                    checkmultisig()
                else:
                    key_num = int(opcode)
                    if (len(stack) - (sig_num + 1)) == key_num:
                        stack.append(key_num)
                        fprint(f"stack: {stack}",)
                    else:
                        print("[!] Error: wrong number of keys, wrong scriptPubkey file?")
                        exit()
            else:
                stack.append(key)
                fprint(f"stack: {stack}",)
        fprint("End of script public key\n")
    else:
        print("[!] Error: wrong number of signatures, wrong scriptPubkey file?")
        exit()


def checkmultisig() -> None:
    fprint("\n\nStart of OP_CHECKMULTISIG")
    verified_counter = 0
    key_stack = list()
    sig_stack = list()
    unverified_stack = list()
    while stack:
        key_num = int(stack.pop())
        fprint(f"stack: {stack}")
        for _ in range(key_num):
            key_stack.append(stack.pop())
            fprint(f"stack: {stack}")
        
        sig_num = int(stack.pop())
        fprint(f"stack: {stack}")
        for _ in range(0, sig_num):
            sig_stack.append(stack.pop())
            fprint(f"stack: {stack}")
    fprint("\n")

    key_stack.reverse()
    sig_stack.reverse()

    for sig_range in range(len(sig_stack)):
        sig = bytes.fromhex(sig_stack[sig_range])
        for key_range in range(len(key_stack)):
            if key_stack[key_range] not in unverified_stack:
                pub_key = DSA.import_key(bytes.fromhex(key_stack[key_range]))
                hash_msg = SHA256.new(b'Contemporary topic in security')
                verifier = DSS.new(pub_key, 'fips-186-3')
                try:
                    verifier.verify(hash_msg, sig)
                    fprint(f"Signature verified")
                    verified_counter += 1
                    unverified_stack.append(key_stack[key_range])
                    break
                except ValueError:
                    fprint(f"Signature not verified")
                    unverified_stack.append(key_stack[key_range])
                    continue

    if verified_counter == len(sig_stack):
        fprint("Multisig verified")
        stack.append("1")
        fprint(f"stack: {stack}")
    else:
        fprint("Multisig not verified")
        stack.append("0")
        fprint(f"stack: {stack}")
    fprint("\n\nEnd of script Public Key")
    exit()

def fprint(msg) -> None:
    print(msg)
    print(msg, file=log_file)


if __name__ == '__main__':
    scriptSigFile = input("Enter scriptSig file: ")
    scriptPubkeyFile = input("Enter scriptPubkey file: ")
    sig_list, key_list = read_file(scriptSigFile, scriptPubkeyFile)
    extract_signature()
    extract_keys()
