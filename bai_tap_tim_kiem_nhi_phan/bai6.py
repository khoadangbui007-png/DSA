def lower_bound(a, x):
    lo, hi = 0, len(a)  # hi = n (ngoài mảng)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid  # a[mid] >= x → có thể là đáp án
    return lo

print(lower_bound([1,3,5,7], 4))  # → 2 (a[2]=5)