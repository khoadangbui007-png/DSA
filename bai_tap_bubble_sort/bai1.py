def one_pass_bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    return a

a = [5, 1, 4, 2, 8]
print(one_pass_bubble_sort(a))  