def hash_mod(k, m):
    return k % m


keys = list(range(0, 64, 4))

for m in [16, 17]:
    buckets = [0] * m

    for key in keys:
        buckets[hash_mod(key, m)] += 1

    print("m =", m)
    print(buckets)