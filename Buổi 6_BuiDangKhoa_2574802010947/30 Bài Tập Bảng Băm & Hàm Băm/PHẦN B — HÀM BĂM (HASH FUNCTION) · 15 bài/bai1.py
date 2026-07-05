def hash_mod(k, m):
    return k % m


m = 10
keys = [37, 15, 28, 99, 42, 71]

for k in keys:
    print(k, "->", hash_mod(k, m))