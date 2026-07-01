def Bai_17(graph=G1, s=0, t=5):
    print(f"\n--- Bài 17: Đường đi Bottleneck (Minimax) từ {s} tới {t} ---")
    # Biến thể: Tìm đường sao cho max_edge_weight là bé nhất có thể
    dist = {node: float('inf') for node in graph}
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v, w in graph[u]:
            # Phép thư giãn (Relax) được đổi thành: tìm cực tiểu của giá trị cực đại cạnh
            bottleneck = max(dist[u], w)
            if bottleneck < dist[v]:
                dist[v] = bottleneck
                heapq.heappush(pq, (dist[v], v))
                
    print(f"Cạnh lớn nhất nhỏ nhất (minimax) trên đường đi là: {dist[t]}")



