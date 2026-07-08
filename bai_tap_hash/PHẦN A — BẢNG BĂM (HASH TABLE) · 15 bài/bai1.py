class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return abs(hash(key)) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        for i, kv in enumerate(self.table[idx]):
            if kv[0] == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for kv in self.table[idx]:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        idx = self._hash(key)
        for i, kv in enumerate(self.table[idx]):
            if kv[0] == key:
                self.table[idx].pop(i)
                return True
        return False

if __name__ == "__main__":
    ht = ChainingHashTable()
    ht.put('a', 1)
    print("Bài 1 - get('a'):", ht.get('a'))  