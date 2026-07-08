

def stable_selection_sort_inplace(arr):
    n = len(arr)
    shift_count = 0
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
                
        
        key = arr[min_idx]
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
            shift_count += 1
        arr[i] = key
        
    return shift_count


a = [(2, 'a'), (2, 'b'), (1, 'c')]
print("Mảng trước khi sắp xếp:", a)

total_shifts = stable_selection_sort_inplace(a)
print("Mảng sau khi sắp xếp ổn định:", a)
print("Tổng số thao tác dịch chuyển phần tử phải đánh đổi:", total_shifts)