def Bai_4():
    print("--- Bài 4: Tìm kiếm tuyến tính ---")
    def index_of(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    arr = [5, 3, 7]
    print(f"Mảng {arr}, tìm vị trí của số 7 -> Vị trí: {index_of(arr, 7)}") # Kq: 2
    print()


if __name__ == "__main__":
    Bai_4()
