
def insertion_sort_nearly_sorted(a):
    arr = a.copy()
    n = len(arr)
    shifts = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = key
    return arr, shifts

print("Bài 17:", insertion_sort_nearly_sorted([1, 2, 4, 3, 5]))