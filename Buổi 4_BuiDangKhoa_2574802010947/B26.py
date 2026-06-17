
def insert_into_sorted_array(a, x):

    arr = a.copy()
    arr.append(x)
    i = len(arr) - 2
    while i >= 0 and arr[i] > x:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = x
    return arr

a1 = [1, 3, 5, 7]
x1 = 4
print("Bài 1:", insert_into_sorted_array(a1, x1))