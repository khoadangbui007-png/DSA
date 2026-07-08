class HashTable:
    def __init__(self):
        self.size = 4
        self.count = 0
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        if self.count / self.size > 0.75:
            self.rehash()

        idx = self.hash(key)
        self.table[idx].append(key)
        self.count += 1

    def rehash(self):
        old = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old:
            for key in bucket:
                self.insert(key)


h = HashTable()

for i in range(10):
    h.insert(i)

print(h.table)