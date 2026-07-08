def Bai_6():
    print("--- Bài 6: Tự động mở rộng dung lượng (Resizing) ---")
    class DynamicArray:
        def __init__(self):
            self.capacity = 4
            self.size = 0
            self.array = [None] * self.capacity
        def append(self, val):
            if self.size == self.capacity:
                self._resize(self.capacity * 2)
            self.array[self.size] = val
            self.size += 1
        def _resize(self, new_cap):
            print(f"-> Mảng đầy (size={self.size}, cap={self.capacity})! Cấp phát dung lượng mới: {new_cap}")
            new_arr = [None] * new_cap
            for i in range(self.size):
                new_arr[i] = self.array[i]
            self.array = new_arr
            self.capacity = new_cap

    da = DynamicArray()
    for i in range(1, 6): # Thêm 5 phần tử để vượt kích thước ban đầu là 4
        da.append(i)
    print()


if __name__ == "__main__":
    Bai_6()
