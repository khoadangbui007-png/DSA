def bubble_sort_optimized(a):
    n = len(a)
    rounds = 0

    for i in range(n - 1):
        swapped = False
        rounds += 1

        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if not swapped:
            break

    return a, rounds


a = [1, 2, 3, 4]

sorted_a, rounds = bubble_sort_optimized(a)

print("Mảng:", sorted_a)
print("Số lượt:", rounds)