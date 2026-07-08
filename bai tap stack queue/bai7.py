def Bai_7():
    print("--- Bài 7: Min Stack O(1) ---")
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []
        def push(self, x):
            self.stack.append(x)
            if not self.min_stack or x <= self.min_stack[-1]:
                self.min_stack.append(x)
        def pop(self):
            if not self.stack: return
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
        def getMin(self):
            return self.min_stack[-1] if self.min_stack else None

    ms = MinStack()
    ms.push(5); ms.push(3); ms.push(7)
    print(f"Push 5,3,7 -> getMin = {ms.getMin()}") # Kết quả: 3
    print()


if __name__ == '__main__':
    Bai_7()
