def tim_tat_ca(a, x):
    vi_tri = []

    for i in range(len(a)):
        if a[i] == x:
            vi_tri.append(i)

    return vi_tri


n = int(input("Nhap so phan tu cua mang: "))

a = []
print("Nhap cac phan tu cua mang:")
for i in range(n):
    value = int(input())
    a.append(value)

x = int(input("Nhap gia tri can tim: "))

ket_qua = tim_tat_ca(a, x)

print("Tat ca vi tri cua", x, "la:", ket_qua)