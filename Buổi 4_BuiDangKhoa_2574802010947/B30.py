
def count_insertion_shifts(a):
    arr = a.copy()
    n = len(arr)
    shift_count = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shift_count += 1
        arr[j + 1] = key
    return shift_count

a5 = [3, 2, 1]
print("Bài 5: Số lần dịch chuyển =", count_insertion_shifts(a5))