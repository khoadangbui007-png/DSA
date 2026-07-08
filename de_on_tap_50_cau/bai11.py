def selection_sort(a):
    compare = 0
    n = len(a)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            compare += 1
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a, compare


a = [64, 25, 12, 22, 11]

sorted_a, compare = selection_sort(a)

print("Mảng:", sorted_a)
print("Số phép so sánh:", compare)