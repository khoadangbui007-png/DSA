def Bai_18():
    print("--- Bài 3 (Phần B): Tìm kiếm một giá trị ---")
    head = Node(1); head.next = Node(2); head.next.next = Node(3)
    
    def search_value(head, target):
        curr = head
        idx = 0
        while curr:
            if curr.data == target:
                return idx
            curr = curr.next
            idx += 1
        return -1

    print(f"DSLK: 1->2->3, Tìm giá trị 2 -> Vị trí: {search_value(head, 2)}") # Kq: 1
    print()


if __name__ == "__main__":
    Bai_18()
