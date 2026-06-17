
def insertion_sort_chars(a):
    arr = a.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

a7 = ['d', 'a', 'c', 'b']
print("Bài 7:", insertion_sort_chars(a7))