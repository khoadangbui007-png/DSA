def Bai_23():
    print("--- Bài 8 (Phần B): Phát hiện chu trình (Floyd's Tortoise and Hare) ---")
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # Tạo DSLK có vòng lặp (1 -> 2 -> 3 -> 4 -> trỏ ngược lại 2)
    n1 = Node(1); n2 = Node(2); n3 = Node(3); n4 = Node(4)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2
    print(f"Danh sách kiểm tra có chu trình không? -> Kết quả: {has_cycle(n1)}")
    print()


if __name__ == "__main__":
    Bai_23()
