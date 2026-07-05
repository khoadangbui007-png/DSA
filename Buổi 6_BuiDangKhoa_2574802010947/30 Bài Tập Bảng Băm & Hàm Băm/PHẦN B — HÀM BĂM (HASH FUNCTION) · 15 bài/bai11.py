def unordered_hash(values):
    h = 0
    for value in values:
        h ^= hash(value)
    return h


set1 = {1, 2, 3}
set2 = {3, 2, 1}
set3 = {1, 2, 4}

print(unordered_hash(set1))
print(unordered_hash(set2))
print(unordered_hash(set3))