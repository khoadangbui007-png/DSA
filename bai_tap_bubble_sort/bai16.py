def count_inversions(a):
    n = len(a)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                inversions += 1
    return inversions

a = [2, 3, 1]
print(count_inversions(a)) 