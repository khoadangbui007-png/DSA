class ArrayList:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self.capacity *= 2
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data

        self.data[self.size] = value
        self.size += 1

    def display(self):
        print(self.data[:self.size])


arr = ArrayList()

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)

arr.display()