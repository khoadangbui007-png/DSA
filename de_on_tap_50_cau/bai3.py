def lower_bound(a, x):
    left, right = 0, len(a)

    while left < right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(a, x):
    left, right = 0, len(a)

    while left < right:
        mid = (left + right) // 2
        if a[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left


a = [1, 3, 5, 7]
x = 4

print(lower_bound(a, x))
print(upper_bound(a, x))