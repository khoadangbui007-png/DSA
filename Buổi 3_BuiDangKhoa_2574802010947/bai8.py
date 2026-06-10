def check_sorted_after_k_passes(a, k):
    n = len(a)
    for i in range(min(k, n)):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                
    is_sorted = True
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            is_sorted = False
            break
            
    return is_sorted

a = [3, 2, 1]
print(check_sorted_after_k_passes(a, k=1))  