def bubble_sort_nearly_sorted(a, k):
    n = len(a)
    total_passes = 0
    
    for i in range(n):
        swapped = False
        total_passes += 1
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
            
    return a, total_passes

arr = [1, 2, 4, 3, 5] 
sorted_arr, passes = bubble_sort_nearly_sorted(arr, k=1)
print(f"Kết quả Bài 22: {sorted_arr} (Số lượt chạy: {passes})")