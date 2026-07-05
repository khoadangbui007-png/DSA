class LinearProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def _hash(self, key):
        return abs(hash(key)) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        start = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            idx = (idx + 1) % self.size
            if idx == start:
                raise Exception("Bảng đầy!")
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        idx = self._hash(key)
        start = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.size
            if idx == start:
                break
        return None

if __name__ == "__main__":
    ht = LinearProbingHashTable()
    ht.put('a', 100)
    print("Bài 2 - get('a'):", ht.get('a'))  