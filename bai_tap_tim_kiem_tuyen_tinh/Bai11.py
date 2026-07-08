def tim_max(a):
    max_value = a[0]
    vi_tri = 0

    for i in range(1, len(a)):
        if a[i] > max_value:
            max_value = a[i]
            vi_tri = i

    return max_value, vi_tri


n = int(input("Nhap so phan tu cua mang: "))

a = []
print("Nhap cac phan tu cua mang:")
for i in range(n):
    value = int(input())
    a.append(value)

max_value, vi_tri = tim_max(a)

print("Gia tri lon nhat la:", max_value)
print("Vi tri cua gia tri lon nhat la:", vi_tri)