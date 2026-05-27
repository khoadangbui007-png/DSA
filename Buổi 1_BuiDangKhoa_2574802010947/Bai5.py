# Tim kiem tuyen tinh
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def binary_search(a, x):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


A1 = [7, 3, 9, 12, 5]      # mang chua sap xep
A2 = [3, 5, 7, 9, 12]      # mang da sap xep
x = 5

print("Tim kiem tuyen tinh:", linear_search(A1, x))
print("Tim kiem nhi phan:", binary_search(A2, x))