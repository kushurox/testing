from itertools import cycle
from time import time
from hashlib import md5
import os



def hashit(x) :
    return md5(x).hexdigest()

def xor(a,b):
    return ''.join(chr(ord(i)^ord(j)) for i,j in zip(a,cycle(b)))

def generatekey(sz) :
    return hashit(os.urandom(sz))

def encrypt(m) :
    return xor("Message : " + m + ":e.o.m" ,generatekey(28))

if __name__ == "__main__" :
    with open("cipher.txt", "rb") as fp:
        d = fp.read()
    
    print(encrypt(hashit(d)))



