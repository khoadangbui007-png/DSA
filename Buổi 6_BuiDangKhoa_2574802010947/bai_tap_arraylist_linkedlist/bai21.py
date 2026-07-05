def Bai_21():
    print("--- Bài 6 (Phần B): Đảo ngược danh sách liên kết ---")
    # Cách lặp (Iterative - 3 con trỏ)
    def reverse_iterative(head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    head = Node(1); head.next = Node(2); head.next.next = Node(3)
    print(f"Ban đầu: {print_singly_list(head)}")
    reversed_head = reverse_iterative(head)
    print(f"Sau khi đảo ngược (Vòng lặp): {print_singly_list(reversed_head)}")
    print()


if __name__ == "__main__":
    Bai_21()
