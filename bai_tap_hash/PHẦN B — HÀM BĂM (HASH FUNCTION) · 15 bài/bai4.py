def hash_mod(k, m):
    return k % m


keys = [10, 20, 15, 25, 35, 40, 50]
m = 10

buckets = {}

for key in keys:
    h = hash_mod(key, m)
    if h not in buckets:
        buckets[h] = []
    buckets[h].append(key)

collisions = 0

for bucket in buckets.values():
    if len(bucket) > 1:
        collisions += len(bucket) * (len(bucket) - 1) // 2

print("So va cham:", collisions)

for index, bucket in buckets.items():
    print(index, ":", bucket)