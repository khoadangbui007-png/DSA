def tim_so_chan_dau_tien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i
    return -1


n = int(input("Nhap so phan tu cua mang: "))

a = []
print("Nhap cac phan tu cua mang:")
for i in range(n):
    value = int(input())
    a.append(value)

ket_qua = tim_so_chan_dau_tien(a)

if ket_qua != -1:
    print("So chan dau tien la:", a[ket_qua])
    print("Vi tri:", ket_qua)
else:
    print("Mang khong co so chan")