def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n-m+1):
        if text[i:i+m] == pattern:
            return i

    return -1


text = "zabcd"
pattern = "abc"

print(rabin_karp(text,pattern))