def tim_xoay(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x: return mid
        # Nửa trái đang sắp xếp
        if a[lo] <= a[mid]:
            if a[lo] <= x < a[mid]: hi = mid - 1
            else: lo = mid + 1
        # Nửa phải đang sắp xếp
        else:
            if a[mid] < x <= a[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1

print(tim_xoay([4,5,6,7,0,1,2], 0))  # → 4