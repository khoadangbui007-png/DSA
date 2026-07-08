def Bai_19():
    print("\n--- Bài 19: Đường đi có xác suất thành công lớn nhất ---")
    # Đồ thị mẫu biểu diễn xác suất thành công [0, 1] trên mỗi cạnh
    prob_graph = {
        0: [(1, 0.8), (2, 0.5)],
        1: [(3, 0.9)],
        2: [(3, 0.95)],
        3: []
    }
    s, t = 0, 3
    # Khởi tạo mảng lưu xác suất lớn nhất, nhân dồn giá trị thay vì cộng
    max_prob = {node: 0.0 for node in prob_graph}
    max_prob[s] = 1.0
    pq = [(-1.0, s)] # Dùng giá trị âm trong Min-Heap để mô phỏng Max-Heap
    
    while pq:
        p, u = heapq.heappop(pq)
        p = -p
        if p < max_prob[u]: continue
        
        for v, prob in prob_graph[u]:
            if max_prob[u] * prob > max_prob[v]:
                max_prob[v] = max_prob[u] * prob
                heapq.heappush(pq, (-max_prob[v], v))
                
    print(f"Tích xác suất lớn nhất từ {s} đến {t} là: {max_prob[t]}")



