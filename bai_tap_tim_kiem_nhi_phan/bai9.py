def vi_tri_chen(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x: lo = mid + 1
        else: hi = mid
    return lo

print(vi_tri_chen([1,3,5,6], 4))  # → 2