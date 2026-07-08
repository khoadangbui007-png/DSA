def Bai_1():
    print("--- Bài 1: Cài đặt Array List cơ bản ---")
    class ArrayList:
        def __init__(self):
            self.data = []
        def add(self, val):
            self.data.append(val)
        def get(self, idx):
            return self.data[idx]
        def set(self, idx, val):
            self.data[idx] = val
        def size(self):
            return len(self.data)

    arr = ArrayList()
    arr.add(1); arr.add(2); arr.add(3)
    print(f"Danh sách sau khi add 1,2,3. get(1) trả về: {arr.get(1)}") # Kq: 2
    print()


if __name__ == "__main__":
    Bai_1()
