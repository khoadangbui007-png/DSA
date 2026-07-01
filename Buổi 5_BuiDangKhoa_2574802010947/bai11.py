def Bai_11(graph=G1, sources=[0, 3]):
    print(f"\n--- Bài 11: Dijkstra nhiều nguồn {sources} ---")
    # Tạo siêu nguồn -1 nối tới các nguồn thực tế với trọng số 0
    extended_graph = {k: v[:] for k, v in graph.items()}
    extended_graph[-1] = [(src, 0) for src in sources]
    
    # Chạy Dijkstra từ siêu nguồn -1
    dist = {node: float('inf') for node in extended_graph}
    dist[-1] = 0
    pq = [(0, -1)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in extended_graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    del dist[-1] # Xóa siêu nguồn khỏi kết quả trả về
    print("Khoảng cách ngắn nhất tới nguồn gần nhất:", dist)



