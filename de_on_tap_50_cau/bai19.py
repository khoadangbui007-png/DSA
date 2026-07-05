import heapq

grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

m = len(grid)
n = len(grid[0])

dist = [[float("inf")] * n for _ in range(m)]
dist[0][0] = grid[0][0]

pq = [(grid[0][0], 0, 0)]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while pq:
    cost, x, y = heapq.heappop(pq)

    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < m and 0 <= ny < n:
            new_cost = cost + grid[nx][ny]

            if new_cost < dist[nx][ny]:
                dist[nx][ny] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny))

print(dist[m-1][n-1])