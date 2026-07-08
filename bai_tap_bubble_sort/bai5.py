def count_comparisons(a):
    n = len(a)
    comparisons = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1 
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return comparisons

a = [1, 2, 3]
print(count_comparisons(a)) 