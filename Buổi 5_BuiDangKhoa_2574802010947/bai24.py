def Bai_24():
    print("\n--- Bài 24: So sánh Dijkstra vs Bellman-Ford vs A* ---")
    headers = ["Thuật toán", "Điều kiện cạnh âm", "Độ phức tạp thời gian", "Cơ chế chính"]
    row1 = ["Dijkstra", "KHÔNG cho phép", "O((V + E) log V)", "Tham lam (Greedy), mở rộng đỉnh gần nhất"]
    row2 = ["Bellman-Ford", "CÓ (Phát hiện chu trình âm)", "O(V * E)", "Quy hoạch động, duyệt relax toàn bộ cạnh V-1 lần"]
    row3 = ["A*", "KHÔNG cho phép", "Phụ thuộc Heuristic", "Dijkstra mở rộng kết hợp hàm Heuristic h(u) hướng đích"]
    
    print(f"{headers[0]:<15} | {headers[1]:<20} | {headers[2]:<25} | {headers[3]}")
    print("-" * 90)
    print(f"{row1[0]:<15} | {row1[1]:<20} | {row1[2]:<25} | {row1[3]}")
    print(f"{row2[0]:<15} | {row2[1]:<20} | {row2[2]:<25} | {row2[3]}")
    print(f"{row3[0]:<15} | {row3[1]:<20} | {row3[2]:<25} | {row3[3]}")



