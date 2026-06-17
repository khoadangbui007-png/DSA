
def gnome_sort(a):
    arr = a.copy()
    n = len(arr)
    index = 0
    while index < n:
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

print("Bài 19:", gnome_sort([3, 2, 1]))