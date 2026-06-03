import math

def koko(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        gio = sum(math.ceil(p / mid) for p in piles)
        if gio <= h: hi = mid  # mid đủ tốt, thử nhỏ hơn
        else: lo = mid + 1
    return lo

print(koko([3,6,7,11], 8))  # → 4