

def verify_fixed_comparisons(arr):
    n = len(arr)
    compare_count = 0
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            compare_count += 1  
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    theoretical_comparisons = int(n * (n - 1) / 2)
    return compare_count, theoretical_comparisons


test_cases = {
    "Mảng ngẫu nhiên": [3, 5, 1, 4, 2],
    "Mảng đã sắp xếp (Best case)": [1, 2, 3, 4, 5],
    "Mảng ngược (Worst case)": [5, 4, 3, 2, 1]
}

for name, case in test_cases.items():
    actual, theoretical = verify_fixed_comparisons(case.copy())
    print(f"{name}: Số lần so sánh thực tế = {actual}, Công thức n(n-1)/2 = {theoretical}")