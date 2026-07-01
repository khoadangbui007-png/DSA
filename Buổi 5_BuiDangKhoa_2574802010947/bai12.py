def Bai_12(graph=G1, s=0, t=5, k=2):
    print(f"\n--- Bài 12: Đi qua đỉnh bắt buộc k = {k} (Từ {s} tới {t}) ---")
    # dist(s, t) bắt buộc qua k = dist(s, k) + dist(k, t)
    dist_from_s = Bai_9(graph, s)
    dist_from_k = Bai_9(graph, k)
    
    total_cost = dist_from_s[k] + dist_from_k[t]
    print(f"Độ dài đường đi đi qua {k}: {total_cost}")



