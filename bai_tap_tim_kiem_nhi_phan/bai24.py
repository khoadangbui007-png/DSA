def tram_xang(x, k):
    lo, hi = 0.0, x[-1] - x[0]
    def ok(gap):
        them = 0
        for i in range(1, len(x)):
            import math
            them += math.ceil((x[i]-x[i-1])/gap) - 1
        return them <= k
    while hi - lo > 1e-6:
        mid = (lo + hi) / 2
        if ok(mid): hi = mid
        else: lo = mid
    return round(hi, 6)

print(tram_xang(list(range(1,11)), 9))  # → 0.5