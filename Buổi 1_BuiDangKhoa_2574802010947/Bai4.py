def phan_tich_do_phuc_tap(n):
    # Trường hợp tốt nhất
    best_case = 1

    # Trường hợp xấu nhất
    worst_case = n

    # Trường hợp trung bình
    average_case = (n + 1) / 2

    print("So phan tu cua mang n =", n)
    print("a) Truong hop tot nhat:", best_case, "phep so sanh")
    print("b) Truong hop xau nhat:", worst_case, "phep so sanh")
    print("c) Truong hop trung binh:", average_case, "phep so sanh")
    print("Do phuc tap thoi gian: O(n)")


n = int(input("Nhap so phan tu cua mang: "))
phan_tich_do_phuc_tap(n)