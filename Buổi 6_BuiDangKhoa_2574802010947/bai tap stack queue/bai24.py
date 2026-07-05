def Bai_24():
    print("--- Bài 9 (Phần B): BFS dùng hàng đợi ---")
    def bfs_iterative(graph, start):
        visited = set([start])
        queue = [start]
        order = []
        while queue:
            vertex = queue.pop(0)
            order.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
    print(f"Thứ tự duyệt cây/đồ thị bằng BFS bắt đầu từ gốc 'A': {bfs_iterative(graph, 'A')}")
    print()


if __name__ == '__main__':
    Bai_24()
