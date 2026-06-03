def thieu_thu_k(a, k):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        thieu = a[mid] - (mid + 1)
        if thieu < k: lo = mid + 1
        else: hi = mid
    return lo + k

print(thieu_thu_k([2,3,4,7,11], 5))  # → 9