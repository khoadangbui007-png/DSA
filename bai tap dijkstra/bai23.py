def Bai_23():
    print("\n--- Bài 23: Nhiều truy vấn đường đi ngắn nhất (Chiến lược đánh đổi) ---")
    print("Khi hệ thống nhận vào số lượng lớn Q truy vấn cặp (s, t), ta có hai chiến lược:")
    print("1. Chạy trực tiếp (On-the-fly):")
    print("   Chạy Dijkstra đơn nguồn cho mỗi truy vấn khi nó đến. Phù hợp nếu Q nhỏ, bộ nhớ hạn chế.")
    print("2. Tiền xử lý toàn bộ (Pre-computation):")
    print("   Chạy Dijkstra từ MỌI đỉnh trong đồ thị (hoặc dùng thuật toán Floyd-Warshall nếu đồ thị nhỏ).")
    print("   Lưu kết quả vào ma trận 2 chiều dist[s][t] kích thước V x V.")
    print("   Đánh đổi: Tốn thời gian khởi tạo ban đầu và tốn O(V^2) bộ nhớ, nhưng trả lời mỗi truy vấn ngay lập tức với O(1).")



