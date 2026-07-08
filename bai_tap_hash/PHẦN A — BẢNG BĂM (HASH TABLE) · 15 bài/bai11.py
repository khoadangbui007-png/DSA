class SimpleHashSet:
    def __init__(self):
        self.table = [[] for _ in range(10)]

    def _hash(self, key):
        return abs(hash(key)) % 10

    def add(self, key):
        idx = self._hash(key)
        if key not in self.table[idx]:
            self.table[idx].append(key)

    def contains(self, key):
        idx = self._hash(key)
        return key in self.table[idx]

    def remove(self, key):
        idx = self._hash(key)
        if key in self.table[idx]:
            self.table[idx].remove(key)
            return True
        return False

if __name__ == "__main__":
    s = SimpleHashSet()
    s.add(1); s.add(1); s.add(2)
    print("Bài 11 - contains(1):", s.contains(1))  
    print("Bài 11 - contains(3):", s.contains(3))  