def can_bac_hai(n):
    if n == 0: return 0
    lo, hi = 1, n
    res = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= n:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res

print(can_bac_hai(8))   # → 2
print(can_bac_hai(16))  # → 4