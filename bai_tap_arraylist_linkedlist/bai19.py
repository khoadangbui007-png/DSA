def Bai_19():
    print("--- Bài 4 (Phần B): Chèn sau một nút cho trước ---")
    head = Node(1); head.next = Node(3)
    print(f"Ban đầu: {print_singly_list(head)}")
    
    # Chèn nút 2 ngay sau nút 1
    new_node = Node(2)
    new_node.next = head.next
    head.next = new_node
    
    print(f"Sau khi chèn số 2 sau số 1: {print_singly_list(head)}")
    print()


if __name__ == "__main__":
    Bai_19()
