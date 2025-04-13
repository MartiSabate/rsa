from Crypto.PublicKey import RSA
from pwn import *

f = open("idrsa.pub", "r")

# https://www.pycryptodome.org/src/public_key/public_key

key = RSA.importKey(f.read())

# https://www.pycryptodome.org/src/public_key/rsa#Crypto.PublicKey.RSA.RsaKey

e = key.e
n = key.n

log.info(f"e: {e}")
log.info(f"n: {n}")

RSA.construct((n, e, d, p, q))
