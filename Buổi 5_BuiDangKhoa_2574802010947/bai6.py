def Bai_6(graph=G1, s=0, t=4):
    # Tìm đường đi ngắn nhất giữa s và t (Dừng sớm)
    V = len(graph)
    dist = [float('inf')] * V
    visited = [False] * V
    dist[s] = 0
    
    for _ in range(V):
        u = -1
        min_d = float('inf')
        for i in range(V):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
                
        if u == -1 or u == t: # Dừng sớm nếu lấy được đích t
            break
        visited[u] = True
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    return dist[t]


    
