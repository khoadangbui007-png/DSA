class LazyDeleteHashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.TOMBSTONE = "DELETED"

    def _hash(self, key):
        return abs(hash(key)) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        first_deleted_idx = None
        start = idx
        
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            if self.keys[idx] == self.TOMBSTONE and first_deleted_idx is None:
                first_deleted_idx = idx
            idx = (idx + 1) % self.size
            if idx == start:
                break
                
        insert_idx = first_deleted_idx if first_deleted_idx is not None else idx
        self.keys[insert_idx] = key
        self.values[insert_idx] = value

    def remove(self, key):
        idx = self._hash(key)
        start = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.keys[idx] = self.TOMBSTONE
                self.values[idx] = None
                return True
            idx = (idx + 1) % self.size
            if idx == start:
                break
        return False

if __name__ == "__main__":
    ht = LazyDeleteHashTable()
    ht.put("x", 500)
    ht.remove("x")
    print("Bài 14 - Trạng thái ô sau xóa:", ht.keys[ht._hash("x")])  