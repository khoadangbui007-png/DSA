def bubble_sort(a):
    swap = 0
    n = len(a)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1

    return a, swap


a = [2, 3, 1]

sorted_a, swap = bubble_sort(a)

print("Mảng sau khi sắp xếp:", sorted_a)
print("Số lần swap:", swap)