def cuoi_cung(a, x):
    lo, hi = 0, len(a) - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            res = mid
            lo = mid + 1  # tiếp tục tìm phải
        elif a[mid] < x: lo = mid + 1
        else: hi = mid - 1
    return res

print(cuoi_cung([1,2,2,2,3], 2))  # → 3