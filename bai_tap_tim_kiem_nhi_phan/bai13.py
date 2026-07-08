def don_le(a):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if mid % 2 == 1: mid -= 1  # đảm bảo mid chẵn
        if a[mid] == a[mid + 1]: lo = mid + 2
        else: hi = mid
    return a[lo]

print(don_le([1,1,2,3,3,4,4]))  # → 2