import random

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

num_hash = 20
max_val = 100

hash_functions = []

for _ in range(num_hash):
    a = random.randint(1, max_val)
    b = random.randint(0, max_val)
    hash_functions.append((a, b))


def minhash(s):
    signature = []

    for a, b in hash_functions:
        value = min((a * x + b) % 101 for x in s)
        signature.append(value)

    return signature


sigA = minhash(A)
sigB = minhash(B)

same = 0

for x, y in zip(sigA, sigB):
    if x == y:
        same += 1

estimate = same / num_hash

jaccard = len(A & B) / len(A | B)

print("MinHash:", estimate)
print("Jaccard:", jaccard)