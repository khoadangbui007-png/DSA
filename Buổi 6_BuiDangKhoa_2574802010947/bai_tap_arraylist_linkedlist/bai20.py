def Bai_20():
    print("--- Bài 5 (Phần B): Xóa nút theo giá trị ---")
    def delete_node(head, val):
        dummy = Node(0)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.data == val:
                curr.next = curr.next.next
                break # Chỉ xóa nút đầu tiên tìm thấy
            else:
                curr = curr.next
        return dummy.next

    head = Node(1); head.next = Node(2); head.next.next = Node(3); head.next.next.next = Node(2)
    print(f"Ban đầu: {print_singly_list(head)}")
    head = delete_node(head, 2)
    print(f"Sau khi xóa nút có giá trị bằng 2 đầu tiên: {print_singly_list(head)}")
    print()


if __name__ == "__main__":
    Bai_20()
