from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from Crypto.Util import Counter

# key = Random.new().read(16)
# print(key)
key = b'\xab\xe6\x7f\xd1\xce\xae\xd5\xe8\xbc\x0b\x1a\x93\xca\x8a\xca/'

# encryption
counter = Counter.new(128)
cipher = AES.new(key, AES.MODE_CTR, counter=counter)
with open(r'C:\Users\GAMALELDIN\Desktop\test.txt', 'r+b') as f:
    plaintext = f.read(16)
    while plaintext:
        f.seek(-len(plaintext), 1)
        f.write(cipher.decrypt(plaintext))
        plaintext = f.read(16)

