class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def selection_sort_linked_list(head):
    dummy = Node(0)
    tail = dummy
    
    while head:
        min_prev = None
        min_node = head
        
        curr_prev = head
        curr = head.next
        
        while curr:
            if curr.value < min_node.value:
                min_node = curr
                min_prev = curr_prev
            curr_prev = curr
            curr = curr.next
            
        if min_node == head:
            head = head.next
        else:
            min_prev.next = min_node.next
            
        min_node.next = None
        tail.next = min_node
        tail = min_node
        
    return dummy.next

def print_list(head):
    curr = head
    out = ""
    while curr:
        out += str(curr.value) + "->"
        curr = curr.next
    out += "null"
    print(out)

# Chạy thử nghiệm với ví dụ: 3 -> 1 -> 2 -> null
head = Node(3)
head.next = Node(1)
head.next.next = Node(2)

sorted_head = selection_sort_linked_list(head)
print_list(sorted_head)