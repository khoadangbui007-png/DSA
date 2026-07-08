def Bai_12():
    print("--- Bài 12: Loại bỏ trùng lặp giữ thứ tự ---")
    def remove_duplicates(arr):
        seen = set()
        result = []
        for x in arr:
            if x not in seen: # Kiểm tra trong O(1) nhờ tập băm
                seen.add(x)
                result.append(x)
        return result

    arr = [3, 1, 3, 2, 1]
    print(f"Mảng {arr} sau khi loại bỏ trùng lặp: {remove_duplicates(arr)}") # Kq: [3, 1, 2]
    print()


if __name__ == "__main__":
    Bai_12()
