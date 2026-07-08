def Bai_9(graph=G1, s=0):
    # Cài đặt Dijkstra dùng Priority Queue / Min-Heap: O((V + E) log V)
    dist = {node: float('inf') for node in graph}
    dist[s] = 0
    pq = [(0, s)] # (distance, node)
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist



