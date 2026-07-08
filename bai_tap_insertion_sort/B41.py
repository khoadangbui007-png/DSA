
def online_insertion_sort_stream(stream):
    arr = []
    steps = []
    for x in stream:
        arr.append(x)
        i = len(arr) - 2
        while i >= 0 and arr[i] > x:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = x
        steps.append(arr.copy())
    return steps

print("Bài 16:", online_insertion_sort_stream([5, 2, 8, 1]))