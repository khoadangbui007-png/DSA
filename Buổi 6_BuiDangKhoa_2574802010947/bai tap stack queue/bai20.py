def Bai_20():
    print("--- Bài 5 (Phần B): Tìm front và rear ---")
    queue = [4, 5, 6]
    front = queue[0] if queue else None
    rear = queue[-1] if queue else None
    print(f"Hàng đợi hiện tại: {queue} -> Front = {front}, Rear = {rear}")
    print()


if __name__ == '__main__':
    Bai_20()
