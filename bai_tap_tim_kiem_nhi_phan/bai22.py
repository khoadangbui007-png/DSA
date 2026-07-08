def trung_vi(a, b):
    if len(a) > len(b): a, b = b, a
    m, n = len(a), len(b)
    lo, hi = 0, m
    while lo <= hi:
        pa = (lo + hi) // 2
        pb = (m + n + 1) // 2 - pa
        maxA = a[pa-1] if pa > 0 else float('-inf')
        minA = a[pa]   if pa < m else float('inf')
        maxB = b[pb-1] if pb > 0 else float('-inf')
        minB = b[pb]   if pb < n else float('inf')
        if maxA <= minB and maxB <= minA:
            if (m + n) % 2 == 1:
                return float(max(maxA, maxB))
            return (max(maxA,maxB) + min(minA,minB)) / 2
        elif maxA > minB: hi = pa - 1
        else: lo = pa + 1

print(trung_vi([1,2],[3,4]))  # → 2.5