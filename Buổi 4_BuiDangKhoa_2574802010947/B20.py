

import heapq

def heap_sort_descending(arr):
    
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    
    sorted_arr = []
    
    while max_heap:
        max_val = -heapq.heappop(max_heap)
        sorted_arr.append(max_val)
        
    return sorted_arr


a = [5, 2, 4, 6, 1]
result = heap_sort_descending(a)
print("Mảng ban đầu:", a)
print("Mảng sau khi sắp xếp giảm dần (Heap Sort):", result)