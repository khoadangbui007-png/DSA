import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float("inf")] * n
    dist[start] = 0

    heap = [(0, start)]

    while heap:
        cost, u = heapq.heappop(heap)

        if cost > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    return dist


graph = [
    [(1, 2), (2, 4)],
    [(2, 1), (3, 7)],
    [(4, 3)],
    [(4, 1)],
    []
]

print(dijkstra(graph, 0))