import heapq

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

n = 4
start = 0

dist = [float("inf")] * n
parent = [-1] * n

dist[start] = 0

pq = [(0, start)]

while pq:
    d, u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            parent[v] = u
            heapq.heappush(pq, (dist[v], v))

target = 3
path = []

while target != -1:
    path.append(target)
    target = parent[target]

path.reverse()

print(path)