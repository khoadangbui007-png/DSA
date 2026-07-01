def Bai_10():
    print("\n--- Bài 10: Chọn cài đặt theo mật độ đồ thị ---")
    print("- Đồ thị dày (Dense Graph: E ≈ V^2):")
    print("  + Bản O(V^2) tốn thời gian tỷ lệ với V^2.")
    print("  + Bản Heap tốn O(V^2 * log V) vì E ≈ V^2. Do đó bản O(V^2) KHÔNG DÙNG HEAP sẽ tốt hơn.")
    print("- Đồ thị thưa (Sparse Graph: E ≈ V):")
    print("  + Bản O(V^2) vẫn tốn V^2 phép tính.")
    print("  + Bản Heap chỉ tốn O(V log V) do E nhỏ. Bản HEAP vượt trội hoàn toàn.")



