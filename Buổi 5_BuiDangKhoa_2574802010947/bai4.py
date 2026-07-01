def Bai_4():
    print("\n--- Bài 4: In khoảng cách tới mọi đỉnh từ nguồn 0 ---")
    dist = Bai_3(G1, 0)
    for i, d in enumerate(dist):
        val = d if d != float('inf') else -1
        print(f"dist[{i}] = {val}")



