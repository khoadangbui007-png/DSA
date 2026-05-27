def tuyen_tinh(array, n, x):
    for i in range(0, n):
        if array[i] == x:
            return i
    return -1


array = [15, 25, 80, 30, 60, 50, 110, 100, 130, 180]
n = len(array)

# Truong hop 1
x = 110
result = tuyen_tinh(array, n, x)

if result != -1:
    print("Phan tu tim thay duoc tai vi tri la:", result)
else:
    print("Phan tu ko duoc tim thay trong arr[]")


# Truong hop 2
x = 185
result = tuyen_tinh(array, n, x)

if result != -1:
    print("Phan tu tim thay duoc tai vi tri la:", result)
else:
    print("Phan tu ko duoc tim thay trong arr[]")