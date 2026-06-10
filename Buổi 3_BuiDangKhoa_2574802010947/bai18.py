class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bubble_sort_linked_list(head):
    if not head:
        return None
    
    end = None
    while end != head.next:
        current = head
        while current.next != end:
            next_node = current.next
            if current.data > next_node.data:
                current.data, next_node.data = next_node.data, current.data
            current = current.next
        end = current
    return head

head = Node(1)
head.next = Node(3)
head.next.next = Node(2)

sorted_head = bubble_sort_linked_list(head)
curr = sorted_head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
print("None")  