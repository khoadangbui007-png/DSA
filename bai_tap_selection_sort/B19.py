

a = [5, 1, 4, 2, 8]

left = 0
right = len(a) - 1

total_loops = 0
total_comparisons = 0

while left < right:
    total_loops += 1
    min_idx = left
    max_idx = left
    
    for i in range(left + 1, right + 1):
        total_comparisons += 1
        if a[i] < a[min_idx]:
            min_idx = i
            
        total_comparisons += 1
        if a[i] > a[max_idx]:
            max_idx = i
            
    a[left], a[min_idx] = a[min_idx], a[left]
    
    if max_idx == left:
        max_idx = min_idx
        
    a[right], a[max_idx] = a[max_idx], a[right]
    
    left += 1
    right -= 1

print("Mảng sau khi sắp xếp:", a)
print("Số vòng lặp (vòng quét):", total_loops)
print("Tổng số lần so sánh:", total_comparisons)