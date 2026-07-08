def Bai_1():
    print("--- Bài 1: Cài đặt ngăn xếp bằng mảng ---")
    class ArrayStack:
        def __init__(self):
            self.stack = []
        def push(self, x):
            self.stack.append(x)
        def pop(self):
            if self.isEmpty(): return "Stack Underflow"
            return self.stack.pop()
        def top(self):
            if self.isEmpty(): return None
            return self.stack[-1]
        def isEmpty(self):
            return len(self.stack) == 0

    s = ArrayStack()
    s.push(1); s.push(2); s.push(3)
    print(f"Ví dụ: push 1,2,3 rồi pop trả về: {s.pop()}") # Kết quả: 3
    print()


if __name__ == '__main__':
    Bai_1()
