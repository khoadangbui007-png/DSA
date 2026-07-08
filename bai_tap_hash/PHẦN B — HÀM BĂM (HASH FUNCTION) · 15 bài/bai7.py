def pair_hash(a, b):
    c = 31
    return (hash(a) * c) ^ hash(b)


pairs = [(1, 2), (2, 3), (5, 7), ("a", "b")]

for p in pairs:
    print(p, "->", pair_hash(p[0], p[1]))