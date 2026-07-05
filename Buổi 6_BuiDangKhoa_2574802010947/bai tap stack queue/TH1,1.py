# Thực hành 1.1
myStack = []  # Khởi tạo ngăn xếp rỗng

myStack.append('data science')  # Đưa phần tử vào đỉnh stack
myStack.append('data analytics')
myStack.append('data structures and algorithms')
myStack.append('big data')
myStack.append('learning data analytics')

print("Stack ban đầu:")
print(myStack)

myStack.pop()  # Lấy phần tử ở đỉnh stack ra
myStack.pop()

print("Stack sau khi pop 2 lần:")
print(myStack)