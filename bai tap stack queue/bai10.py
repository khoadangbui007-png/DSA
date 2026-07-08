import collections

def Bai_10():
    print("--- Bài 10: Cài đặt ngăn xếp bằng hai hàng đợi ---")
    class StackUsingTwoQueues:
        def __init__(self):
            self.q1 = collections.deque()
            self.q2 = collections.deque()
        def push(self, x): # Chi phí O(1)
            self.q1.append(x)
        def pop(self):     # Chi phí O(n)
            if not self.q1: return "Underflow"
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            popped = self.q1.popleft()
            self.q1, self.q2 = self.q2, self.q1
            return popped

    sq = StackUsingTwoQueues()
    sq.push(1); sq.push(2); sq.push(3)
    print(f"Pop phần tử từ ngăn xếp: {sq.pop()}") # LIFO nên trả về 3
    print()


if __name__ == '__main__':
    Bai_10()
