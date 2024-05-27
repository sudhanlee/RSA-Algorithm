#!/usr/bin/env python3

from math import gcd

def rsa_key_generation(p,q):
    n = p*q # n with prime number

    z = (p - 1)*(q - 1)

    for i in range(2,z):
        if (gcd(i,z) == 1):
            e = i # public key e
            break

    j = 0
    while True:
        if (j * e) % z == 1:
            d = j #private key d
            break
        j += 1

    print("Public key: {{'e': {},'n': {}}}".format(e, n))
    print("Private key: {{'d': {},'n': {}}}".format(d, n))
    return n,e,d


def rsa_encrypt(plaintext,publickey):
    ciphertext = ""
    e,n = publickey
    for i in range(len(plaintext)):
        ciphertext += str((ord(plaintext[i]) ** e) % n)
        ciphertext += " "
    return ciphertext

def rsa_decrypt(ciphertext,privatekey):
    plaintext = ""
    d,n = privatekey
    ciphertext = ciphertext.split()
    for i in range(len(ciphertext)):
        plaintext += chr((int(ciphertext[i]) ** d)%n)
    return plaintext

while True:
    print("1.Generate Key\n2.Encrypt Plaintext\n3.Decrypt Ciphertext\n0.Exit\nEnter option: ",end="")
    opt = int(input())

    if (opt == 1):
        p,q = map(int,input("Enter p and q (p q): ").split())
        n,e,d = rsa_key_generation(p,q)

    elif (opt == 2):
        plaintxt = input("Enter Plaintext to encrypt: ")
        pubkey = tuple(map(int,input("Enter Public key (e n): ").split()))
        ciphertxt = rsa_encrypt(plaintxt,pubkey)
        print("Ciphertext: {}".format(ciphertxt))

    elif (opt == 3):
        ciphertxt = input("Enter Ciphertext to decrypt: ")
        privkey = tuple(map(int,input("Enter Private key (d n): ").split()))
        plaintxt = rsa_decrypt(ciphertxt,privkey)
        print("Plaintext: {}".format(plaintxt))

    elif (opt == 0):
        exit()

    else:
        print("\nInvaild Input!!")
    print()