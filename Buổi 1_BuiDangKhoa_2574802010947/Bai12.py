def tim_min_max(a):
    min_value = a[0]
    max_value = a[0]
    vi_tri_min = 0
    vi_tri_max = 0

    for i in range(1, len(a)):
        if a[i] < min_value:
            min_value = a[i]
            vi_tri_min = i

        if a[i] > max_value:
            max_value = a[i]
            vi_tri_max = i

    return min_value, vi_tri_min, max_value, vi_tri_max


n = int(input("Nhap so phan tu cua mang: "))

a = []
print("Nhap cac phan tu cua mang:")
for i in range(n):
    value = int(input())
    a.append(value)

min_value, vi_tri_min, max_value, vi_tri_max = tim_min_max(a)

print("Gia tri nho nhat la:", min_value)
print("Vi tri cua Min la:", vi_tri_min)

print("Gia tri lon nhat la:", max_value)
print("Vi tri cua Max la:", vi_tri_max)