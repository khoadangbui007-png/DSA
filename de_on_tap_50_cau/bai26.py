class CircularQueue:
    def __init__(self, size):
        self.q = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0
        self.size = size

    def enqueue(self, x):
        if self.count == self.size:
            print("Queue đầy")
            return

        self.q[self.rear] = x
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("Queue rỗng")
            return None

        x = self.q[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return x


q = CircularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.dequeue())