def Bai_8(D=3):
    print(f"\n--- Bài 8: Số đỉnh trong bán kính D = {D} từ nguồn 0 ---")
    dist = Bai_3(G1, 0)
    count = sum(1 for d in dist if d <= D)
    nodes = [i for i, d in enumerate(dist) if d <= D]
    print(f"Số đỉnh thỏa mãn: {count} (Gồm các đỉnh: {nodes})")



