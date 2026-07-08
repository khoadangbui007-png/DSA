def Bai_13(graph=G1, s=0):
    print("\n--- Bài 13: Đếm số đường đi ngắn nhất từ nguồn 0 ---")
    dist = {node: float('inf') for node in graph}
    paths_count = {node: 0 for node in graph}
    
    dist[s] = 0
    paths_count[s] = 1
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                paths_count[v] = paths_count[u] # Reset số đường đi bằng đỉnh u trung chuyển
                heapq.heappush(pq, (dist[v], v))
            elif dist[u] + w == dist[v]:
                paths_count[v] += paths_count[u] # Cộng dồn nếu độ dài bằng nhau
                
    for node in paths_count:
        print(f"Đỉnh {node}: có {paths_count[node]} đường đi ngắn nhất.")



