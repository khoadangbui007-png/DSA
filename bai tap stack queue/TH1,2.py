from collections import deque  # Import deque từ thư viện collections

myStack = deque()  # Tạo ngăn xếp rỗng

myStack.append('data science')  # Push
myStack.append('data structures and algorithms')
myStack.append('learning data analytics')
myStack.append('big data')

print("Stack ban đầu:")
print(myStack)

myStack.pop()  # Pop
myStack.pop()

print("Stack sau khi pop 2 lần:")
print(myStack)