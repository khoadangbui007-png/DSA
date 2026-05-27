def ton_tai(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    return False


n = int(input("Nhap so phan tu cua mang: "))

a = []
print("Nhap cac phan tu cua mang:")
for i in range(n):
    value = int(input())
    a.append(value)

x = int(input("Nhap gia tri can tim: "))

if ton_tai(a, x):
    print("True - x co trong mang")
else:
    print("False - x khong co trong mang")