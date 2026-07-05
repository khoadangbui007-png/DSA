def Bai_14():
    print("--- Bài 14: Mảng động 2 chiều ---")
    class DynamicMatrix:
        def __init__(self):
            self.matrix = []
        def add_row(self, row_list):
            self.matrix.append(row_list)
        def get(self, i, j):
            return self.matrix[i][j]
        def set(self, i, j, val):
            self.matrix[i][j] = val

    dm = DynamicMatrix()
    dm.add_row([1, 2, 3])
    dm.add_row([4, 5, 6])
    dm.set(1, 1, 99) # Thay đổi phần tử hàng 1 cột 1 thành 99
    print(f"Truy cập ma trận tại vị trí (1, 1) -> Kết quả: {dm.get(1, 1)}") # Kq: 99
    print()


if __name__ == "__main__":
    Bai_14()
