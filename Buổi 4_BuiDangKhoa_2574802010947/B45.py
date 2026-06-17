
def shell_sort(a):
    arr = a.copy()
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap //= 2
    return arr

print("Bài 20:", shell_sort([9, 8, 3, 7, 5, 6, 4, 1]))