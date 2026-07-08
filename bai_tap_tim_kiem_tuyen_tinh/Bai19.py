def tim_sinh_vien(ds, ma_sv):
    for sv in ds:
        if sv["ma"] == ma_sv:
            return sv
    return None


ds = [
    {"ma": "SV01", "ten": "An", "diem": 8.5},
    {"ma": "SV02", "ten": "Binh", "diem": 7.0},
    {"ma": "SV03", "ten": "Chau", "diem": 9.0}
]

ma = input("Nhap ma sinh vien: ")

sv = tim_sinh_vien(ds, ma)

if sv:
    print("Thong tin:", sv)
else:
    print("Khong tim thay")