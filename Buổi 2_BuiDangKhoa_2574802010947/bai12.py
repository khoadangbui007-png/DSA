def tim_dinh(a):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < a[mid + 1]: lo = mid + 1
        else: hi = mid
    return lo

print(tim_dinh([1,2,3,1]))  # → 2