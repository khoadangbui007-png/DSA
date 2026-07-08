from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: []
}

visited = set()

q = deque([0])
visited.add(0)

while q:
    u = q.popleft()
    print(u, end=" ")

    for v in graph[u]:
        if v not in visited:
            visited.add(v)
            q.append(v)