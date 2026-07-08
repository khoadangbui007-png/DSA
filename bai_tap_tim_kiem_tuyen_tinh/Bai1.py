def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


n = int(input("Nhap so phan tu cua mang: "))

a = []
print("Nhap cac phan tu cua mang:")
for i in range(n):
    x = int(input())
    a.append(x)

k = int(input("Nhap gia tri can tim: "))

ket_qua = linear_search(a, k)

if ket_qua != -1:
    print("Tim thay tai vi tri:", ket_qua)
else:
    print("Khong tim thay")