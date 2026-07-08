def suc_chua_tau(w, D):
    lo, hi = max(w), sum(w)
    while lo < hi:
        mid = (lo + hi) // 2
        ngay, tai = 1, 0
        for x in w:
            if tai + x > mid:
                ngay += 1; tai = 0
            tai += x
        if ngay <= D: hi = mid
        else: lo = mid + 1
    return lo

print(suc_chua_tau(list(range(1,11)), 5))  # → 15