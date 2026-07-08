def Bai_5():
    print("\n--- Bài 5: Đồ thị vô hướng có trọng số (Từ A đến các đỉnh) ---")
    # Sử dụng hàm Dijkstra O(V^2) cho đồ thị vô hướng G2, nguồn A (0)
    dist = Bai_3(G2, 0)
    mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    for i, d in enumerate(dist):
        print(f"Từ A đến {mapping[i]} ngắn nhất là: {d}")



