def Bai_17():
    print("--- Bài 2 (Phần B): Hàng đợi vòng (Circular Queue) ---")
    class CircularQueue:
        def __init__(self, capacity):
            self.capacity = capacity
            self.queue = [None] * capacity
            self.head = -1
            self.tail = -1
        def enqueue(self, x):
            if (self.tail + 1) % self.capacity == self.head:
                return "Overflow"
            if self.head == -1:
                self.head = 0
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = x
            return True
        def dequeue(self):
            if self.head == -1:
                return "Underflow"
            res = self.queue[self.head]
            if self.head == self.tail:
                self.head = self.tail = -1
            else:
                self.head = (self.head + 1) % self.capacity
            return res

    cq = CircularQueue(4)
    cq.enqueue(5); cq.enqueue(6)
    print(f"Mô phỏng hàng đợi vòng với sức chứa 4. Dequeue: {cq.dequeue()}")
    print()


if __name__ == '__main__':
    Bai_17()
