class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def put(self, key, value):
        idx = self.hash(key)

        for item in self.table[idx]:
            if item[0] == key:
                item[1] = value
                return

        self.table[idx].append([key, value])

    def get(self, key):
        idx = self.hash(key)

        for k, v in self.table[idx]:
            if k == key:
                return v

        return None


ht = HashTable()

ht.put(10, "A")
ht.put(20, "B")

print(ht.get(20))