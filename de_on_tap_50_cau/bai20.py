import heapq

def heuristic(a, b):
    # Khoảng cách Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    g = {start: 0}
    parent = {}

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        x, y = current

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_g = g[current] + 1

                if (nx, ny) not in g or new_g < g[(nx, ny)]:
                    g[(nx, ny)] = new_g
                    f = new_g + heuristic((nx, ny), goal)
                    heapq.heappush(open_set, (f, (nx, ny)))
                    parent[(nx, ny)] = current

    return None


grid = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [0,1,1,0]
]

start = (0,0)
goal = (3,3)

path = astar(grid, start, goal)

print("Đường đi:", path)