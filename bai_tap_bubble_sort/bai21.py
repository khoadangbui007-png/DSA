def stable_bubble_sort_pairs(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):

            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

data = [(2, 'A'), (1, 'C'), (2, 'B')]
print("Kết quả Bài 21:", stable_bubble_sort_pairs(data))
