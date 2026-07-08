def Bai_7():
    print("--- Bài 7: Phân tích amortized của append ---")
    print("Chứng minh lý thuyết:")
    print("- Khi append n phần tử, mảng mở rộng tại các bước 1, 2, 4, 8, ..., 2^k.")
    print("- Tổng chi phí copy phần tử khi mở rộng: 1 + 2 + 4 + 8 + ... + n = 2n - 1 thao tác.")
    print("- Tổng số thao tác bao gồm cả n lần chèn trực tiếp: n + (2n - 1) = 3n - 1.")
    print("- Chi phí trung bình (Amortized) cho mỗi lần append: (3n - 1) / n = O(1).")
    print()


if __name__ == "__main__":
    Bai_7()
