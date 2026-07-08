class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def remove_k(head,k):
    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    for _ in range(k):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next