def Bai_2():
    print("--- Bài 2: Thêm / xóa ở cuối ---")
    class ArrayListEnd:
        def __init__(self):
            self.data = []
        def append(self, val):
            self.data.append(val) # O(1) trung bình
        def popBack(self):
            if not self.data: return None
            return self.data.pop() # O(1)

    arr = ArrayListEnd()
    arr.append(1); arr.append(2); arr.append(3)
    print(f"Mảng ban đầu: [1, 2, 3]. popBack trả về: {arr.popBack()}") # Kq: 3
    print()


if __name__ == "__main__":
    Bai_2()
