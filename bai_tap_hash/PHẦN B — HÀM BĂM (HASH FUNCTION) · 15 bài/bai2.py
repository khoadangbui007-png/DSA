def string_hash(s, m):
    return sum(ord(c) for c in s) % m


m = 10
strings = ["abc", "cba", "hello", "world"]

for s in strings:
    print(s, "->", string_hash(s, m))