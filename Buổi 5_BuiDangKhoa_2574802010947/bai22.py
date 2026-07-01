def Bai_22(graph=G1, s=0, t=5, max_edges=2):
    print(f"\n--- Bài 22: Tìm đường rẻ nhất giới hạn tối đa {max_edges} cạnh trung chuyển ---")
    # Định nghĩa cấu trúc mảng 2 chiều: dist[u][e] là chi phí tới u dùng đúng/tối đa e cạnh
    dist = {node: [float('inf')] * (max_edges + 1) for node in graph}
    dist[s][0] = 0
    pq = [(0, s, 0)] # (chi phí, đỉnh, số cạnh đã đi)
    
    while pq:
        d, u, e = heapq.heappop(pq)
        if d > dist[u][e]: continue
        if e >= max_edges: continue
            
        for v, w in graph[u]:
            if d + w < dist[v][e + 1]:
                dist[v][e + 1] = d + w
                heapq.heappush(pq, (d + w, v, e + 1))
                
    ans = min(dist[t])
    print(f"Chi phí nhỏ nhất từ {s} tới {t} với tối đa {max_edges} cạnh là: {ans if ans != float('inf') else -1}")



