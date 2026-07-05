def Bai_22():
    print("--- Bài 7 (Phần B): Tìm nút giữa (Slow / Fast) ---")
    head = Node(1); head.next = Node(2); head.next.next = Node(3); head.next.next.next = Node(4); head.next.next.next.next = Node(5)
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    print(f"DSLK: 1->2->3->4->5 -> Nút chính giữa tìm thấy là: {slow.data}") # Kq: 3
    print()


if __name__ == "__main__":
    Bai_22()
