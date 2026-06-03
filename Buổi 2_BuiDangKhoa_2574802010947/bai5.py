def dem(a, x):
    first = dau_tien(a, x)
    if first == -1: return 0
    last = cuoi_cung(a, x)
    return last - first + 1

print(dem([1,2,2,2,3], 2))  # → 3