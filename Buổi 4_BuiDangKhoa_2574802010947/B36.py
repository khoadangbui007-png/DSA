
def demo_insertion_sort_stability(a):
    arr = a.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Điều kiện arr[j][0] > key[0] đảm bảo giữ nguyên thứ tự các phần tử cùng khóa
        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

a11 = [(2, 'a'), (2, 'b'), (1, 'c')]
print("Bài 11:", demo_insertion_sort_stability(a11))