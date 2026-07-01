def Bai_15(grid=GRID):
    print("\n--- Bài 15: Dijkstra trên lưới (Grid) 3x3 ---")
    R, C = len(grid), len(grid[0])
    dist = [[float('inf')] * C for _ in range(R)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)] # (chi phí, dòng, cột)
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while pq:
        d, r, c = heapq.heappop(pq)
        if d > dist[r][c]: continue
        if r == R - 1 and c == C - 1: break
            
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if dist[r][c] + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + grid[nr][nc]
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))
                    
    print(f"Tổng chi phí nhỏ nhất tới ô góc dưới-phải: {dist[R-1][C-1]}")



