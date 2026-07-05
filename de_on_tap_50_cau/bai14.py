def shell_sort(a):
    gap = len(a) // 2

    while gap > 0:
        for i in range(gap, len(a)):
            temp = a[i]
            j = i

            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap

            a[j] = temp

        gap //= 2

    return a


a = [12, 34, 54, 2, 3]

print(shell_sort(a))