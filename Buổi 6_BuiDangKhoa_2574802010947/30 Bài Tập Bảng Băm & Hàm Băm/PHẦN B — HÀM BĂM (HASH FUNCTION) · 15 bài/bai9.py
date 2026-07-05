import random

m = 10
p = 101

a = random.randint(1, p - 1)
b = random.randint(0, p - 1)


def universal_hash(k):
    return ((a * k + b) % p) % m


keys = [5, 10, 15, 20, 25, 30]

print("a =", a)
print("b =", b)

for key in keys:
    print(key, "->", universal_hash(key))