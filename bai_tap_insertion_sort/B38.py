
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insertion_sort_linked_list(head):
    if not head or not head.next:
        return head
        
    dummy = Node(0)
    curr = head
    
    while curr:
        next_node = curr.next
        
        prev = dummy
        while prev.next and prev.next.value < curr.value:
            prev = prev.next
            
        curr.next = prev.next
        prev.next = curr
        
        curr = next_node
        
    return dummy.next

def print_linked_list(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(str(curr.value))
        curr = curr.next
    nodes.append("null")
    return " -> ".join(nodes)

head13 = Node(3)
head13.next = Node(1)
head13.next.next = Node(2)

sorted_head13 = insertion_sort_linked_list(head13)
print("Bài 13:", print_linked_list(sorted_head13))