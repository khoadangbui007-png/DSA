a = [5, 3, 8, 4, 2]

compare_count = 0
n = len(a)

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        compare_count += 1
        if a[j] < a[min_idx]:
            min_idx = j
            
    a[i], a[min_idx] = a[min_idx], a[i]

print("Mảng sau khi sắp xếp:", a)
print("Số lần so sánh:", compare_count)