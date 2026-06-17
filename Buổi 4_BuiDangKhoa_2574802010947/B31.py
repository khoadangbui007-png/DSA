
def count_insertion_sort_comparisons(a):
    arr = a.copy()
    n = len(arr)
    compare_count = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            compare_count += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return compare_count

a6 = [1, 2, 3]
print("Bài 6:", count_insertion_sort_comparisons(a6))