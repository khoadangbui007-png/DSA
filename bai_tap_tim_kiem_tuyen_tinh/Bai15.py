def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def tim_so_nguyen_to_dau_tien(a):
    for i in range(len(a)):
        if la_so_nguyen_to(a[i]):
            return a[i], i

    return -1, -1


n = int(input("Nhap so phan tu cua mang: "))

a = []
print("Nhap cac phan tu cua mang:")
for i in range(n):
    value = int(input())
    a.append(value)

so_nt, vi_tri = tim_so_nguyen_to_dau_tien(a)

if so_nt != -1:
    print("So nguyen to dau tien la:", so_nt)
    print("Vi tri:", vi_tri)
else:
    print("Khong co so nguyen to trong mang")