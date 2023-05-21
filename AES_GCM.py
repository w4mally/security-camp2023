from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def AES_GCM(key,nonce,text):
    c = AES.new(key, AES.MODE_GCM, nonce)
    cipher, tag = c.encrypt_and_digest(text)
    return cipher, tag

key = get_random_bytes(16)
nonce = get_random_bytes(12)

plaintext = input()
text_byte = plaintext.encode()

cipher, tag = AES_GCM(key,nonce,text_byte)

print(ciphertect, tag)
