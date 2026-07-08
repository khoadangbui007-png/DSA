def Bai_22():
    print("--- Bài 7 (Phần B): Đảo ngược hàng đợi ---")
    queue = [1, 2, 3]
    stack = []
    print(f"Hàng đợi trước đảo ngược: {queue}")
    while queue:
        stack.append(queue.pop(0))
    while stack:
        queue.append(stack.pop())
    print(f"Hàng đợi sau khi đảo ngược:  {queue}")
    print()


if __name__ == '__main__':
    Bai_22()
