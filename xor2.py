c = "TRSKPVKTWPKWUe"
k = 0x65
p = ''
print "c = " + c
print "      xor 65h"
for char in c:
    p = p + ''.join(chr(ord(char)^k))
print "p = " + p
