
def insertion_sort_k_steps(a, k):
    arr = a.copy()
    n = len(arr)
    for i in range(1, min(k + 1, n)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

a8 = [4, 3, 2, 1]
k8 = 1
print("Bài 8:", insertion_sort_k_steps(a8, k8))