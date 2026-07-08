def dem_xuat_hien(a, x):
    dem = 0

    for i in range(len(a)):
        if a[i] == x:
            dem += 1

    return dem


n = int(input("Nhap so phan tu cua mang: "))

a = []
print("Nhap cac phan tu cua mang:")
for i in range(n):
    value = int(input())
    a.append(value)

x = int(input("Nhap gia tri can dem: "))

ket_qua = dem_xuat_hien(a, x)

print("So lan xuat hien cua", x, "la:", ket_qua)