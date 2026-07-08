def Bai_16():
    print("--- Bài 1 (Phần B): Cài đặt hàng đợi cơ bản ---")
    class BasicQueue:
        def __init__(self):
            self.queue = []
        def enqueue(self, x):
            self.queue.append(x)
        def dequeue(self):
            if self.isEmpty(): return "Queue Underflow"
            return self.queue.pop(0)
        def front(self):
            return self.queue[0] if not self.isEmpty() else None
        def isEmpty(self):
            return len(self.queue) == 0

    q = BasicQueue()
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    print(f"Enqueue 1,2,3 rồi Dequeue trả về: {q.dequeue()}") # Kết quả: 1
    print()


if __name__ == '__main__':
    Bai_16()
