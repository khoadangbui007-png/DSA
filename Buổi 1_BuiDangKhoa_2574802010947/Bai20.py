danh_ba = []


def them_lien_he():
    ten = input("Nhap ten: ")
    sdt = input("Nhap so dien thoai: ")
    danh_ba.append({"ten": ten, "sdt": sdt})


def tim_theo_ten():
    ten = input("Nhap ten can tim: ")

    for lh in danh_ba:
        if lh["ten"] == ten:
            print("So dien thoai:", lh["sdt"])
            return

    print("Khong tim thay")


def tim_theo_sdt():
    sdt = input("Nhap so can tim: ")

    for lh in danh_ba:
        if lh["sdt"] == sdt:
            print("Ten:", lh["ten"])
            return

    print("Khong tim thay")


def dem_dau_so():
    dau_so = input("Nhap dau so: ")
    dem = 0

    for lh in danh_ba:
        if lh["sdt"].startswith(dau_so):
            dem += 1

    print("So lien he:", dem)


while True:
    print("\n1. Them")
    print("2. Tim theo ten")
    print("3. Tim theo so")
    print("4. Dem theo dau so")
    print("0. Thoat")

    chon = int(input("Chon: "))

    if chon == 1:
        them_lien_he()
    elif chon == 2:
        tim_theo_ten()
    elif chon == 3:
        tim_theo_sdt()
    elif chon == 4:
        dem_dau_so()
    elif chon == 0:
        break