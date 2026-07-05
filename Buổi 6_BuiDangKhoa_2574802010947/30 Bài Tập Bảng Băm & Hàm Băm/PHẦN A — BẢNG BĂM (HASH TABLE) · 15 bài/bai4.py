def find_common_elements(arr1, arr2):
    set1 = set(arr1)
    
    return list({x for x in arr2 if x in set1})

if __name__ == "__main__":
    print("Bài 4 - Phần tử chung:", find_common_elements([1,2,3], [2,3,4]))  