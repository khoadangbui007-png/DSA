
def selection_sort_with_swaps(arr):
    a = arr.copy()
    swap_count = 0
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap_count += 1
    return swap_count

def bubble_sort_with_swaps(arr):
    a = arr.copy()
    swap_count = 0
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap_count += 1
    return swap_count


data = [5, 4, 3, 2, 1]

selection_swaps = selection_sort_with_swaps(data)
bubble_swaps = bubble_sort_with_swaps(data)

print(f"Dữ liệu đầu vào: {data}")
print(f"Số lần hoán đổi của Selection Sort: {selection_swaps}")
print(f"Số lần hoán đổi của Bubble Sort: {bubble_swaps}")