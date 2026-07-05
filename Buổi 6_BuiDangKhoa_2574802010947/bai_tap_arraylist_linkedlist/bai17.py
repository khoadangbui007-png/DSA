def Bai_17():
    print("--- Bài 2 (Phần B): Tính độ dài / duyệt ---")
    head = Node(1); head.next = Node(2); head.next.next = Node(3)
    
    # Duyệt và đếm số nút
    curr = head
    length = 0
    print("Duyệt DSLK: ", end="")
    while curr:
        print(curr.data, end=" ")
        length += 1
        curr = curr.next
    print(f"\nĐộ dài danh sách: {length}") # Kq: 3
    print()


if __name__ == "__main__":
    Bai_17()
