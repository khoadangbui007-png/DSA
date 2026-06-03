def chia_sach(p, m):
    lo, hi = max(p), sum(p)
    def ok(limit):
        hs, tong = 1, 0
        for x in p:
            if tong + x > limit: hs += 1; tong = 0
            tong += x
        return hs <= m
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid): hi = mid
        else: lo = mid + 1
    return lo

print(chia_sach([12,34,67,90], 2))  # → 113