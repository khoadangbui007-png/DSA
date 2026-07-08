def Bai_24():
    print("--- Bài 9 (Phần B): Trộn hai danh sách liên kết đã sắp xếp ---")
    def merge_two_lists(l1, l2):
        dummy = Node(0)
        curr = dummy
        while l1 and l2:
            if l1.data < l2.data:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next

    h1 = Node(1); h1.next = Node(3); h1.next.next = Node(5)
    h2 = Node(2); h2.next = Node(4)
    res = merge_two_lists(h1, h2)
    print(f"Trộn (1->3->5) và (2->4) -> Kết quả: {print_singly_list(res)}")
    print()


if __name__ == "__main__":
    Bai_24()
