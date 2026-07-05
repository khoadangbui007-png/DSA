def Bai_3():
    print("--- Bài 3: Mô phỏng dãy thao tác ---")
    stack = []
    operations = [("push", 5), ("push", 7), ("pop", None)]
    print("Thực hiện dãy thao tác:")
    for op, val in operations:
        if op == "push":
            stack.append(val)
            print(f"- push {val}: Trạng thái hiện tại: {stack}")
        elif op == "pop":
            popped = stack.pop() if stack else "Underflow"
            print(f"- pop: In giá trị {popped}, Trạng thái còn lại: {stack}")
    print()


if __name__ == '__main__':
    Bai_3()
