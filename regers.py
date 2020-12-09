import hashlib
import random

def Hash(a,b):
    x=a*31+b*31
    return x
def similar():
    while True:
        n=random.randint(1,100)
        d = 2
        if n % d != 0:
            break
    return 2*n+1

N=similar()
g=similar()

k=Hash(N,g)


s=523
x=Hash(s,228)
v=g^x%N
