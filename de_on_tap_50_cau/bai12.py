def bubble_sort(a):
    n = len(a)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


a = [(3, "A"), (2, "B"), (3, "C"), (1, "D")]

print(bubble_sort(a))