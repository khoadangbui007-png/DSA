def polynomial_hash(s, p=31, mod=1000000007):
    h = 0

    for c in s:
        h = (h * p + ord(c)) % mod

    return h


print(polynomial_hash("hello"))