def Bai_4():
    print("--- Bài 4: Phát hiện underflow / overflow ---")
    class FixedCapacityStack:
        def __init__(self, capacity):
            self.capacity = capacity
            self.stack = []
        def push(self, x):
            if len(self.stack) >= self.capacity:
                return "Lỗi: overflow"
            self.stack.append(x)
            return f"push {x} thành công"
        def pop(self):
            if not self.stack:
                return "Lỗi: underflow"
            return self.stack.pop()

    fs = FixedCapacityStack(2)
    print("Thử nghiệm Overflow với capacity = 2:")
    print(fs.push(1))
    print(fs.push(2))
    print(fs.push(3))
    print("Thử nghiệm Underflow:")
    print("Pop:", fs.pop())
    print("Pop:", fs.pop())
    print("Pop:", fs.pop())
    print()


if __name__ == '__main__':
    Bai_4()
