def k_gan_nhat(a, k, x):
    lo, hi = 0, len(a) - k
    while lo < hi:
        mid = (lo + hi) // 2
        if x - a[mid] > a[mid + k] - x:
            lo = mid + 1
        else:
            hi = mid
    return a[lo : lo + k]

print(k_gan_nhat([1,2,3,4,5], 4, 3))  # → [1,2,3,4]