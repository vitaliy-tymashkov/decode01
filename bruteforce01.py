#http://www.voidspace.org.uk/python/modules.shtml#pycrypto
#https://stackoverflow.com/questions/2979174/how-do-i-compute-the-approximate-entropy-of-a-bit-string

import math
# import entropy
from Crypto.Cipher import AES
"""
Crypto works unstable on Windows (and on Linux also)
1) pip install crypto
2) find the package - usually python/libs/dist-packages and rename "crypto" as "Crypto"
3) copy folder to projects libs also
"""
# from scipy.stats import entropy
import numpy as np
import hashlib
# from pycryptodome import AES
# import crypto
#import Pycrypto
#from Crypto.Cipher import AES
# import EntroPy


def entropy(string):
    "Calculates the Shannon entropy of a string"

    # get probability of chars in string
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]

    # calculate the entropy
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])

    return entropy

def bruteforce(msg):
    iv = msg[:16]
    #for pin in xrange(62628180, 62628190):
    for pin in xrange(00000000, 99999999):

        key = hashlib.sha256(str(pin)).digest()
        aes = AES.new(key, AES.MODE_CBC, iv)
        decryptedData = aes.decrypt(msg[16:])

        ent = entropy(decryptedData)
        # ent = EntroPy.shannon_entropy(decryptedData)

        # print pin, ent, '\r'
        if ent < 7:
            print pin, ent, '\r'





print "************* START BRUTEFORCE *************"

with open('crack.me.output',"rb") as f:
    enc = f.read(512)

bruteforce(enc)

print "************* STOP  BRUTEFORCE *************"
