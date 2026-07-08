def Bai_3():
    print("--- Bài 3: Chèn / xóa ở vị trí bất kỳ ---")
    class ArrayListInsertDelete:
        def __init__(self):
            self.data = [1, 2, 4]
        def insert(self, idx, val):
            self.data.insert(idx, val) # O(n) do phải dịch chuyển các phần tử phía sau
        def delete(self, idx):
            if 0 <= idx < len(self.data):
                return self.data.pop(idx) # O(n)
    
    arr = ArrayListInsertDelete()
    arr.insert(2, 3)
    print(f"[1,2,4] chèn 3 tại idx 2 -> Kết quả: {arr.data}") # Kq: [1, 2, 3, 4]
    print()


if __name__ == "__main__":
    Bai_3()
