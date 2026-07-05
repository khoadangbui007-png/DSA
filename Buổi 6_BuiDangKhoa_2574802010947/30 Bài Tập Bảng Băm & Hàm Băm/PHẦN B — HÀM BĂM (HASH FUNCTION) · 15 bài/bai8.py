def hash_mod(k, m):
    return k % m


def hash_mul(k, m):
    A = 0.6180339887
    return int(m * ((k * A) % 1))


keys = list(range(100))
m = 10

bucket1 = [0] * m
bucket2 = [0] * m

for key in keys:
    bucket1[hash_mod(key, m)] += 1
    bucket2[hash_mul(key, m)] += 1

print("Modulo:")
print(bucket1)

print("Multiplication:")
print(bucket2)