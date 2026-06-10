def bubble_sort_k_passes(a, k):
    n = len(a)
    for i in range(k):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

a = [3, 1, 4, 1, 5]
print(bubble_sort_k_passes(a, k=2))  