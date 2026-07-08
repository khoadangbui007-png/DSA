class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        return self.stack.pop()

    def getMin(self):
        return self.min_stack[-1]


s = MinStack()

s.push(5)
s.push(3)
s.push(7)

print(s.getMin())