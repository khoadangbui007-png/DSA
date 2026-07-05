import math

A = 0.6180339887
m = 10


def multiplication_hash(k):
    return math.floor(m * ((k * A) % 1))


keys = [5, 10, 15, 20, 25, 30, 35]

for key in keys:
    print(key, "->", multiplication_hash(key))