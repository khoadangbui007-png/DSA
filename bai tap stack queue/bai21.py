def Bai_21():
    print("--- Bài 6 (Phần B): Cài đặt hàng đợi bằng hai ngăn xếp ---")
    class QueueWithTwoStacks:
        def __init__(self):
            self.in_stack = []
            self.out_stack = []
        def enqueue(self, x):
            self.in_stack.append(x)
        def dequeue(self):
            if not self.out_stack:
                while self.in_stack:
                    self.out_stack.append(self.in_stack.pop())
            if not self.out_stack: return "Queue Underflow"
            return self.out_stack.pop()

    qs = QueueWithTwoStacks()
    qs.enqueue(1); qs.enqueue(2)
    print(f"Đẩy vào 1, 2. Thực hiện Dequeue ra: {qs.dequeue()}") # Kết quả: 1
    print()


if __name__ == '__main__':
    Bai_21()
