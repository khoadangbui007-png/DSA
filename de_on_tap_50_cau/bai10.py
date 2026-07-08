def binary_search(a, key, left, right):
    while left <= right:
        mid = (left + right) // 2

        if a[mid] <= key:
            left = mid + 1
        else:
            right = mid - 1

    return left


def binary_insertion_sort(a):
    shift = 0

    for i in range(1, len(a)):
        key = a[i]

        pos = binary_search(a, key, 0, i - 1)

        j = i
        while j > pos:
            a[j] = a[j - 1]
            shift += 1
            j -= 1

        a[pos] = key

    return a, shift


a = [5, 2, 4, 6, 1, 3]

sorted_a, shift = binary_insertion_sort(a)

print("Mảng:", sorted_a)
print("Shift:", shift)