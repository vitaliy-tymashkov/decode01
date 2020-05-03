import hashlib


expectedHash = '0xdecOde1'
exemplaryHash = '3928979165'

sha256 = hashlib.sha256()
sha256.update(exemplaryHash)
temporaryResult = sha256.digest()

#hashedValue =

print (temporaryResult)