def Bai_3(graph=G1, s=0):
    # Cài đặt Dijkstra bản O(V^2) sử dụng mảng đánh dấu
    V = len(graph)
    dist = [float('inf')] * V
    visited = [False] * V
    dist[s] = 0
    
    for _ in range(V):
        # Tìm đỉnh u chưa visited có dist[u] nhỏ nhất
        u = -1
        min_d = float('inf')
        for i in range(V):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
                
        if u == -1: break
        visited[u] = True
        
        # Relax các cạnh kề của u
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    return dist



