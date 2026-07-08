def find_min_index(a, i):
    min_idx = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    return min_idx

# Chạy thử nghiệm với ví dụ trong ảnh:
a = [9, 3, 7, 1, 5]
i = 1
result = find_min_index(a, i)
print(f"Ví dụ: a = {a}, i = {i} -> chỉ số {result}")