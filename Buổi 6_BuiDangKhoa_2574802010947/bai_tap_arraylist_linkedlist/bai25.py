def Bai_25():
    print("--- Bài 10 (Phần B): Xóa nút thứ k từ cuối ---")
    def remove_nth_from_end(head, k):
        dummy = Node(0)
        dummy.next = head
        first = second = dummy
        # Di chuyển con trỏ first đi trước k + 1 bước
        for _ in range(k + 1):
            first = first.next
        # Di chuyển đồng thời cả 2 con trỏ
        while first:
            first = first.next
            second = second.next
        # Xóa nút
        second.next = second.next.next
        return dummy.next

    head = Node(1); head.next = Node(2); head.next.next = Node(3); head.next.next.next = Node(4); head.next.next.next.next = Node(5)
    print(f"Ban đầu: {print_singly_list(head)}")
    head = remove_nth_from_end(head, 2) # Xóa nút thứ 2 từ cuối (nút 4)
    print(f"Sau khi xóa nút thứ k=2 từ cuối: {print_singly_list(head)}")
    print()


if __name__ == "__main__":
    Bai_25()
