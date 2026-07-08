def Bai_20(graph=G1, s=0, t=4, K=3):
    print(f"\n--- Bài 20: Tìm {K} đường đi ngắn nhất từ {s} đến {t} ---")
    # Đếm số lần mỗi đỉnh được lấy ra khỏi hàng đợi ưu tiên
    count = {node: 0 for node in graph}
    result = []
    pq = [(0, s)] # (cost, node)
    
    while pq and count[t] < K:
        d, u = heapq.heappop(pq)
        count[u] += 1
        
        if u == t:
            result.append(d)
            
        if count[u] <= K:
            for v, w in graph[u]:
                heapq.heappush(pq, (d + w, v))
                
    print(f"{K} khoảng cách ngắn nhất tới {t} là: {result}")



