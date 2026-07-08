def Bai_18():
    print("--- Bài 3 (Phần B): Mô phỏng dãy thao tác ---")
    queue = []
    operations = [("enq", 5), ("enq", 7), ("deq", None)]
    for op, val in operations:
        if op == "enq":
            queue.append(val)
            print(f"- Enqueue {val}: Trạng thái hàng đợi: {queue}")
        elif op == "deq":
            deq_val = queue.pop(0) if queue else "Underflow"
            print(f"- Dequeue: In ra {deq_val}, Trạng thái hàng đợi: {queue}")
    print()


if __name__ == '__main__':
    Bai_18()
