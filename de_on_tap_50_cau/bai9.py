def insertion_sort(a):
    shift = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shift += 1
            j -= 1

        a[j + 1] = key

    return a, shift


a = [3, 2, 1]

sorted_a, shift = insertion_sort(a)

print("Mảng:", sorted_a)
print("Shift:", shift)