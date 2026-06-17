
def binary_insertion_sort(a):
    arr = a.copy()
    n = len(arr)
    compare_count = 0
    
    for i in range(1, n):
        key = arr[i]
        low = 0
        high = i - 1
        
        while low <= high:
            mid = (low + high) // 2
            compare_count += 1
            if key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        for j in range(i - 1, low - 1, -1):
            arr[j + 1] = arr[j]
        arr[low] = key
        
    return arr, compare_count

a9 = [5, 2, 4, 6, 1]
sorted_a9, comp_a9 = binary_insertion_sort(a9)
print(f"Bài 9: Mảng sau sắp xếp: {sorted_a9}, Tổng số lần so sánh: {comp_a9}")