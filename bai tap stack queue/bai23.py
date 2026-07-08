def Bai_23():
    print("--- Bài 8 (Phần B): Hàng đợi hai đầu (Deque) ---")
    class BasicDeque:
        def __init__(self):
            self.deque = []
        def pushFront(self, x):
            self.deque.insert(0, x)
        def pushBack(self, x):
            self.deque.append(x)
        def popFront(self):
            return self.deque.pop(0) if self.deque else "Underflow"
        def popBack(self):
            return self.deque.pop() if self.deque else "Underflow"

    dq = BasicDeque()
    dq.pushFront(1)
    dq.pushBack(2)
    print(f"pushFront 1, pushBack 2 -> Trạng thái cấu trúc: {dq.deque}") # Kết quả: [1, 2]
    print()


if __name__ == '__main__':
    Bai_23()
