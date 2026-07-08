def tim_ten(ds, x):
    x = x.lower()

    for i in range(len(ds)):
        if ds[i].lower() == x:
            return i

    return -1


n = int(input("Nhap so luong sinh vien: "))

ds = []
print("Nhap danh sach ten:")
for i in range(n):
    ten = input()
    ds.append(ten)

x = input("Nhap ten can tim: ")

ket_qua = tim_ten(ds, x)

if ket_qua != -1:
    print("Tim thay tai vi tri:", ket_qua)
else:
    print("Khong tim thay")