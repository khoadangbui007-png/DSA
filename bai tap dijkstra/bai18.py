def Bai_18():
    print("\n--- Bài 18: Vì sao Dijkstra cần trọng số không âm & Demo G3 ---")
    # Thử nghiệm chạy Dijkstra trên đồ thị G3 có cạnh âm 2->1 (-4)
    dist = {node: float('inf') for node in G3}
    dist[0] = 0
    pq = [(0, 0)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in G3[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    print(f"Dijkstra kết luận dist[1] = {dist[1]} (Bị SAI vì thực tế 0->2->1 bằng 5-4 = 1).")
    print("Giải thích: Do tính chất tham lam, Dijkstra chốt luôn đỉnh 1 khi lấy ra khỏi Heap.")
    print("Nó mặc định không có đường đi vòng nào làm giảm khoảng cách được nữa (điều này chỉ đúng khi trọng số >= 0).")
    print("Thuật toán thay thế phù hợp: Bellman-Ford hoặc SPFA.")



