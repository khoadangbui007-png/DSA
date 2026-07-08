def Bai_25():
    print("--- Bài 10 (Phần B): Hàng đợi ưu tiên cơ bản ---")
    class PriorityQueueSimple:
        def __init__(self):
            self.queue = []
        def push(self, element, priority):
            # Nhận tuple (độ ưu tiên, phần tử), độ ưu tiên cao nhất xếp lên trước
            self.queue.append((priority, element))
            self.queue.sort(key=lambda x: x[0], reverse=True)
        def pop(self):
            if not self.queue: return "Underflow"
            return self.queue.pop(0)[1]

    pq = PriorityQueueSimple()
    pq.push("Task Low", 1)
    pq.push("Task Urgent", 10)
    pq.push("Task Medium", 5)
    print(f"Phần tử được lấy ra đầu tiên (Độ ưu tiên cao nhất): {pq.pop()}")
    print()


if __name__ == '__main__':
    Bai_25()
