class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def merge(a,b):
    dummy = Node(0)
    cur = dummy

    while a and b:
        if a.data < b.data:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next

        cur = cur.next

    cur.next = a if a else b

    return dummy.next


def middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge_sort(head):
    if not head or not head.next:
        return head

    mid = middle(head)
    right = mid.next
    mid.next = None

    left = merge_sort(head)
    right = merge_sort(right)

    return merge(left,right)