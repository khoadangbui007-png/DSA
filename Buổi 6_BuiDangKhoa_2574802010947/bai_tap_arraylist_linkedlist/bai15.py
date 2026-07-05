def Bai_15():
    print("--- Bài 15: Iterator và fail-fast ---")
    class FailFastArrayList:
        def __init__(self):
            self.data = []
            self.modCount = 0 # Đếm số lần sửa đổi cấu trúc
        def add(self, val):
            self.data.append(val)
            self.modCount += 1
        def __iter__(self):
            class ArrayListIterator:
                def __init__(self, outer):
                    self.outer = outer
                    self.cursor = 0
                    self.expectedModCount = outer.modCount
                def __next__(self):
                    if self.outer.modCount != self.expectedModCount:
                        raise RuntimeError("Báo lỗi Fail-fast: Danh sách đã bị sửa đổi cấu trúc trong lúc lặp!")
                    if self.cursor >= len(self.outer.data):
                        raise StopIteration
                    val = self.outer.data[self.cursor]
                    self.cursor += 1
                    return val
            return ArrayListIterator(self)

    ff_list = FailFastArrayList()
    ff_list.add(10); ff_list.add(20); ff_list.add(30)
    
    try:
        print("Bắt đầu lặp phần tử:")
        for x in ff_list:
            print(f"Đang đọc: {x}")
            if x == 10:
                ff_list.add(40) # Sửa đổi cấu trúc ngay giữa vòng lặp
    except RuntimeError as e:
        print(e)
    print()


# ==============================================================================
# PHẦN B: LINKED LIST (DANH SÁCH LIÊN KẾT) - 15 BÀI
# ==============================================================================

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def print_singly_list(head):
    curr = head
    nodes = []
    while curr:
        nodes.append(str(curr.data))
        curr = curr.next
    nodes.append("null")
    return " -> ".join(nodes)


if __name__ == "__main__":
    Bai_15()
