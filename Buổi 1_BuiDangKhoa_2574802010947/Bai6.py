def linear_search(a, x):
    for i in range(len(a)):
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

result = linear_search(a, x)

if result != -1:
    print("Tim thay x tai vi tri:", result)
else:
    print("Khong tim thay x")