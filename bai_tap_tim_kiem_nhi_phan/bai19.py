def bo_chuong(x, c):
    x.sort()
    lo, hi = 1, x[-1] - x[0]
    def ok(d):
        cnt, last = 1, x[0]
        for pos in x[1:]:
            if pos - last >= d:
                cnt += 1; last = pos
        return cnt >= c
    res = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if ok(mid): res = mid; lo = mid + 1
        else: hi = mid - 1
    return res

print(bo_chuong([1,2,4,8,9], 3))  # → 3