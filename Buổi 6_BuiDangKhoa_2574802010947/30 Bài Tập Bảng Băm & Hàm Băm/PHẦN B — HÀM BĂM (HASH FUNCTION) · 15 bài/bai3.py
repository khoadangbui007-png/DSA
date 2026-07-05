def polynomial_hash(s, p=31, m=1000000007):
    h = 0
    power = 1

    for c in reversed(s):
        h = (h + ord(c) * power) % m
        power = (power * p) % m

    return h


strings = ["abc", "hello", "python"]

for s in strings:
    print(s, "->", polynomial_hash(s))