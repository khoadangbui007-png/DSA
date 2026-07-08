def k_nho_matrix(matrix, k):
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[-1][-1]
    def dem_le(mid):
        cnt, j = 0, n - 1
        for i in range(n):
            while j >= 0 and matrix[i][j] > mid: j -= 1
            cnt += j + 1
        return cnt
    while lo < hi:
        mid = (lo + hi) // 2
        if dem_le(mid) < k: lo = mid + 1
        else: hi = mid
    return lo

mat = [[1,5,9],[10,11,13],[12,13,15]]
print(k_nho_matrix(mat, 8))  # → 13