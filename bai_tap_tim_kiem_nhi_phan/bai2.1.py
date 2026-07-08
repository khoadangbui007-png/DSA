def binary_search(array, element):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


array = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
element = 28

result = binary_search(array, element)

print("Phần tử tìm kiếm được là:", result)