import random

p = 101
m = 10

a = random.randint(1,p-1)
b = random.randint(0,p-1)

def universal_hash(key):
    return ((a*key+b)%p)%m

for i in [5,10,15,20]:
    print(i,"->",universal_hash(i))