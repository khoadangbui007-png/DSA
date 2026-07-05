def Bai_5():
    print("--- Bài 5: Duyệt và in phần tử ---")
    arr = [1, 2, 3, 4]
    print("Duyệt mảng: ", end="")
    for x in arr:
        print(x, end=" ")
    
    even_count = sum(1 for x in arr if x % 2 == 0)
    print(f"\nSố lượng số chẵn trong danh sách: {even_count}") # Kq: 2
    print()


if __name__ == "__main__":
    Bai_5()
