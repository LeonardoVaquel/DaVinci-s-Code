from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto import Random
from Crypto.Cipher import AES
import fcntl, os, sys

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

class Encryptor():

    def run (self, aKey, message):
        key = md5(aKey.encode('utf8')).hexdigest()
        raw = pad(message)
        iv = Random.new().read(AES.block_size)
        aesAlgorithm = AES.new(key, AES.MODE_CBC, iv)
        return b64encode(iv + aesAlgorithm.encrypt(raw))

class Decryptor():

    def run (self, aKey, message):
        key = md5(aKey.encode('utf8')).hexdigest()
        enc = b64decode(message)
        iv = enc[:16]
        aesAlgorithm = AES.new(key, AES.MODE_CBC, iv)
        return unpad(aesAlgorithm.decrypt(enc[16:])).decode('utf8')
