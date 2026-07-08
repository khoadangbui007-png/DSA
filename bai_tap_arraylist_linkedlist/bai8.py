def Bai_8():
    print("--- Bài 8: Xóa các phần tử thỏa điều kiện (2 con trỏ) ---")
    def remove_if_even(arr):
        read = 0
        write = 0
        while read < len(arr):
            if arr[read] % 2 != 0: # Giữ lại số lẻ
                arr[write] = arr[read]
                write += 1
            read += 1
        return arr[:write]

    arr = [1, 2, 3, 4]
    print(f"Mảng gốc: {arr} -> Sau khi xóa số chẵn: {remove_if_even(arr)}") # Kq: [1, 3]
    print()


if __name__ == "__main__":
    Bai_8()
