def sentinel_search(a, x):
    a.append(x)
    i = 0

    while a[i] != x:
        i += 1

    a.pop()

    if i < len(a):
        return i
    return -1


a = [7, 3, 9, 5, 1]
x = 5

print("Vi tri:", sentinel_search(a, x))