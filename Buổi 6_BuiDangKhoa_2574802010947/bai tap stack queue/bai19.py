def Bai_19():
    print("--- Bài 4 (Phần B): Kiểm tra rỗng / đầy ---")
    class BoundedQueue:
        def __init__(self, capacity):
            self.capacity = capacity
            self.queue = []
        def enqueue(self, x):
            if len(self.queue) >= self.capacity: return "Báo lỗi: Queue đầy (Overflow)"
            self.queue.append(x)
            return f"Enq {x}"
        def dequeue(self):
            if not self.queue: return "Báo lỗi: Queue rỗng (Underflow)"
            return self.queue.pop(0)
        def size(self):
            return len(self.queue)

    bq = BoundedQueue(2)
    print(bq.enqueue(10))
    print(bq.enqueue(20))
    print(bq.enqueue(30)) # Lỗi đầy
    print(f"Số lượng phần tử hiện có: {bq.size()}")
    print()


if __name__ == '__main__':
    Bai_19()
