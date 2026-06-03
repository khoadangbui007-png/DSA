def chia_mang(a, k):
    lo, hi = max(a), sum(a)
    def ok(limit):
        doan, tong = 1, 0
        for x in a:
            if tong + x > limit: doan += 1; tong = 0
            tong += x
        return doan <= k
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid): hi = mid
        else: lo = mid + 1
    return lo

print(chia_mang([7,2,5,10,8], 2))  # → 18