def Bai_10():
    print("--- Bài 10: Trộn hai danh sách đã sắp xếp ---")
    def merge_sorted_lists(arr1, arr2):
        merged = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])
        return merged

    a1 = [1, 3, 5]
    a2 = [2, 4]
    print(f"Trộn {a1} và {a2} -> Kết quả: {merge_sorted_lists(a1, a2)}")
    print()


if __name__ == "__main__":
    Bai_10()
