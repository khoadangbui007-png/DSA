a = [1, 2, 3]

swap_count = 0
n = len(a)

for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if a[j] < a[min_idx]:
            min_idx = j
            
    if min_idx != i:
        a[i], a[min_idx] = a[min_idx], a[i]
        swap_count += 1

print("Mảng sau khi sắp xếp:", a)
print("Số lần hoán đổi thực sự xảy ra:", swap_count)