def bad_hash(key):
    return 0


keys = ["a", "b", "c", "d", "e", "f"]

table = {}

for key in keys:
    h = bad_hash(key)

    if h not in table:
        table[h] = []

    table[h].append(key)

print(table)

for bucket, values in table.items():
    print("Bucket", bucket, ":", values)