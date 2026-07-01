def Bai_7(graph=G1, s=0, t=4):
    print("\n--- Bài 7: Truy vết đường đi ngắn nhất từ 0 tới 4 ---")
    V = len(graph)
    dist = [float('inf')] * V
    parent = [-1] * V
    visited = [False] * V
    dist[s] = 0
    
    for _ in range(V):
        u = -1
        min_d = float('inf')
        for i in range(V):
            if not visited[i] and dist[i] < min_d:
                min_d = dist[i]
                u = i
        if u == -1: break
        visited[u] = True
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                
    # Truy ngược đường đi từ t về s
    path = []
    curr = t
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    print(f"Đường đi ngắn nhất từ {s} đến {t}: " + " -> ".join(map(str, path)) + f" (Độ dài: {dist[t]})")



