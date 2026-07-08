def Bai_21():
    print("\n--- Bài 21: Dijkstra trên trạng thái mở rộng ---")
    print("Ý tưởng cốt lõi: Định nghĩa lại một trạng thái (State) trong Heap.")
    print("Thay vì chỉ lưu trữ đơn thuần là 'đỉnh u', ta mở rộng thành cặp: tuple (u, phụ_trợ).")
    print("Ví dụ bài toán nạp nhiên liệu:")
    print("  State = (u, fuel) biểu thị đang ở đỉnh u và còn lại 'fuel' đơn vị xăng.")
    print("Mảng khoảng cách trở thành mảng 2 chiều: dist[u][fuel].")
    print("Các bước di chuyển (Relax) bao gồm 2 trạng thái kế tiếp có thể:")
    print("  1. Đi tới đỉnh kề v: (u, fuel) -> (v, fuel - chi_phí_xăng) nếu đủ xăng.")
    print("  2. Đứng yên tại chỗ để đổ thêm xăng: (u, fuel) -> (u, fuel + 1) tốn chi phí mua xăng.")



