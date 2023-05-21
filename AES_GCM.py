from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# 暗号化を行う関数
def AES_GCM(key,nonce,text):
    c = AES.new(key, AES.MODE_GCM, nonce)
    cipher, tag = c.encrypt_and_digest(text)
    return cipher, tag

# 乱数を用いて鍵とノンスを生成
key = get_random_bytes(16)
nonce = get_random_bytes(12)

# 暗号化したい文の入力
plaintext = input()
text_byte = plaintext.encode()

cipher, tag = AES_GCM(key,nonce,text_byte)

print(cipher, tag)
