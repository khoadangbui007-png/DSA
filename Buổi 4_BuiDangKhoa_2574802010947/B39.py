
def insertion_sort_string(s):
    chars = list(s)
    n = len(chars)
    for i in range(1, n):
        key = chars[i]
        j = i - 1
        while j >= 0 and chars[j] > key:
            chars[j + 1] = chars[j]
            j -= 1
        chars[j + 1] = key
    return "".join(chars)

s14 = "python"
print("Bài 14:", insertion_sort_string(s14))