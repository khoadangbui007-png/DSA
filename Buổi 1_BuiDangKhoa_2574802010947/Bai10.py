def tim_cuoi_cung(a, x):
    for i in range(len(a) - 1, -1, -1):
        if a[i] == x:
            return i
    return -1


n = int(input("Nhap so phan tu cua mang: "))

a = []
print("Nhap cac phan tu cua mang:")
for i in range(n):
    value = int(input())
    a.append(value)

x = int(input("Nhap gia tri can tim: "))

ket_qua = tim_cuoi_cung(a, x)

if ket_qua != -1:
    print("Vi tri xuat hien cuoi cung cua", x, "la:", ket_qua)
else:
    print("Khong tim thay")