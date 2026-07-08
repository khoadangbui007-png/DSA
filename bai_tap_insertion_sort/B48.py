# Bài 23. Phân tích best / average / worst
def analyze_insertion_sort_cases(a):
    arr = a.copy()
    n = len(arr)
    compare_count = 0
    shift_count = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        has_compared = False
        while j >= 0:
            compare_count += 1
            has_compared = True
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                shift_count += 1
            else:
                break
        arr[j + 1] = key
    return compare_count, shift_count

print("Bài 23:")
print("Best case [1, 2, 3, 4, 5] (So sanh, Shift):", analyze_insertion_sort_cases([1, 2, 3, 4, 5]))
print("Average case [3, 1, 4, 2, 5] (So sanh, Shift):", analyze_insertion_sort_cases([3, 1, 4, 2, 5]))
print("Worst case [5, 4, 3, 2, 1] (So sanh, Shift):", analyze_insertion_sort_cases([5, 4, 3, 2, 1]))