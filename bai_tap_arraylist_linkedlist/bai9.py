def Bai_9():
    print("--- Bài 9: Đảo ngược tại chỗ ---")
    def reverse_in_place(arr):
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    arr = [1, 2, 3, 4]
    print(f"Mảng gốc: {arr} -> Sau khi đảo ngược: {reverse_in_place(arr)}") # Kq: [4, 3, 2, 1]
    print()


if __name__ == "__main__":
    Bai_9()
