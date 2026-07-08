

def selection_sort_recursive(arr, i=0):
    n = len(arr)
    
   
    if i >= n - 1:
        return
        
 
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
            
  
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    

    selection_sort_recursive(arr, i + 1)

a = [5, 3, 1, 4, 2]
print("Mảng trước khi sắp xếp:", a)

selection_sort_recursive(a)
print("Mảng sau khi sắp xếp (Đệ quy):", a)