def Bai_16():
    print("--- Bài 1 (Phần B): Cài đặt danh sách liên kết đơn ---")
    class SinglyLinkedList:
        def __init__(self):
            self.head = None
        def pushFront(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        def pushBack(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                return
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    sll = SinglyLinkedList()
    sll.pushBack(5)
    sll.pushFront(2)
    print(f"Danh sách liên kết sau khi pushFront 2, pushBack 5: {print_singly_list(sll.head)}")
    print()


if __name__ == "__main__":
    Bai_16()
