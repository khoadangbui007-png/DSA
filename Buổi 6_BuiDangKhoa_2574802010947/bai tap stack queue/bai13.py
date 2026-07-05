def Bai_13():
    print("--- Bài 13: DFS dùng ngăn xếp (khử đệ quy) ---")
    def dfs_iterative(graph, start):
        visited = set()
        stack = [start]
        order = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                # Đảo ngược hàng xóm để duyệt đúng thứ tự từ trái sang phải giống đệ quy
                for neighbor in reversed(graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    # Đồ thị minh họa dạng kề
    graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
    print(f"Thứ tự duyệt DFS từ đỉnh 'A': {dfs_iterative(graph, 'A')}")
    print()


if __name__ == '__main__':
    Bai_13()
