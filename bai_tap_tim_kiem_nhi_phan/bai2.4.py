def binary_search(arr, key):

    left = 0
    right = len(arr) - 1
    step = 0

    while (left <= right):

        step = step + 1

        
        mid = (left + right) // 2

        print("Bước", step)
        print("left =", left,
              ", right =", right,
              ", mid =", mid,
              ", giá trị =", arr[mid])

        
        if (arr[mid] == key):
            return mid

        
        elif (key < arr[mid]):
            right = mid - 1

        
        else:
            left = mid + 1

    
    return -1


arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print("TÌM x = 95")

key = 95

result = binary_search(arr, key)

if (result != -1):
    print("Tìm thấy tại vị trí:", result)
else:
    print("Không tìm thấy phần tử", key)

print("\n----------------------\n")
print("TÌM x = 5")

key = 5

result = binary_search(arr, key)

if (result != -1):
    print("Tìm thấy tại vị trí:", result)
else:
    print("Không tìm thấy phần tử", key)