def Bai_14(graph=G1, s=0, t=4):
    print(f"\n--- Bài 14: Tìm đường đi ngắn nhì từ {s} đến {t} ---")
    # Mảng lưu 2 giá trị khoảng cách tốt nhất: dist[u][0] (nhỏ nhất), dist[u][1] (nhỏ nhì)
    dist = {node: [float('inf'), float('inf')] for node in graph}
    dist[s][0] = 0
    pq = [(0, s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u][1]: continue
        
        for v, w in graph[u]:
            cost = d + w
            if cost < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = cost
                heapq.heappush(pq, (cost, v))
            elif dist[v][0] < cost < dist[v][1]:
                dist[v][1] = cost
                heapq.heappush(pq, (cost, v))
                
    print(f"Đường đi ngắn nhất: {dist[t][0]}, Ngắn nhì: {dist[t][1]}")



