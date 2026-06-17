
def insertion_sort_absolute(a):
    arr = a.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # So sánh dựa trên giá trị trị tuyệt đối abs()
        while j >= 0 and abs(arr[j]) > abs(key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

a15 = [-3, 1, -2, 2]
print("Bài 15:", insertion_sort_absolute(a15))