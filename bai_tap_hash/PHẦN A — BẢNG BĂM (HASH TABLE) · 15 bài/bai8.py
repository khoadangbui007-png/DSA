class DoubleHashingHashTable:
    def __init__(self, size=11):
        self.size = size  
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def _hash1(self, key):
        return abs(hash(key)) % self.size

    def _hash2(self, key):
        return 7 - (abs(hash(key)) % 7)

    def put(self, key, value):
        h1 = self._hash1(key)
        h2 = self._hash2(key)
        i = 0
        while i < self.size:
            idx = (h1 + i * h2) % self.size
            if self.keys[idx] is None or self.keys[idx] == key:
                self.keys[idx] = key
                self.values[idx] = value
                return
            i += 1
        raise Exception("Bảng băm đầy!")

    def get(self, key):
        h1 = self._hash1(key)
        h2 = self._hash2(key)
        i = 0
        while i < self.size:
            idx = (h1 + i * h2) % self.size
            if self.keys[idx] is None:
                break
            if self.keys[idx] == key:
                return self.values[idx]
            i += 1
        return None

if __name__ == "__main__":
    ht = DoubleHashingHashTable()
    ht.put("user1", "Data1")
    print("Bài 8 (Double Hashing) - get:", ht.get("user1"))