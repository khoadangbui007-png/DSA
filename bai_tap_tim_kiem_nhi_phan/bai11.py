def min_xoay(a):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] > a[hi]: lo = mid + 1
        else: hi = mid
    return a[lo]

print(min_xoay([3,4,5,1,2]))  # → 1