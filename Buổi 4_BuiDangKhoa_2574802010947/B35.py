
def count_inversions_and_shifts(a):
    arr = a.copy()
    n = len(arr)
    
    inversion_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                inversion_count += 1
                
    shift_count = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shift_count += 1
        arr[j + 1] = key
        
    return inversion_count, shift_count

a10 = [2, 4, 1, 3]
inv, shift = count_inversions_and_shifts(a10)
print(f"Bài 10: Số cặp nghịch thế = {inv}, Số lần dịch chuyển (shift) = {shift}")