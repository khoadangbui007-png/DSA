def first_pos(a, x):
    left, right = 0, len(a) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            ans = mid
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return ans


def last_pos(a, x):
    left, right = 0, len(a) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            ans = mid
            left = mid + 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return ans


a = [1, 2, 2, 2, 3]
x = 2

first = first_pos(a, x)
last = last_pos(a, x)

print("Đầu:", first)
print("Cuối:", last)

if first == -1:
    print("Đếm:", 0)
else:
    print("Đếm:", last - first + 1)