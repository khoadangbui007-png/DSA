def Bai_11():
    print("--- Bài 11: Xoay mảng k vị trí ---")
    def rotate_right(arr, k):
        n = len(arr)
        k = k % n
        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        # Áp dụng kỹ thuật đảo 3 lần
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return arr

    arr = [1, 2, 3, 4, 5]
    print(f"Xoay {arr} sang phải k=2 vị trí -> Kết quả: {rotate_right(arr, 2)}") # Kq: [4, 5, 1, 2, 3]
    print()


if __name__ == "__main__":
    Bai_11()
