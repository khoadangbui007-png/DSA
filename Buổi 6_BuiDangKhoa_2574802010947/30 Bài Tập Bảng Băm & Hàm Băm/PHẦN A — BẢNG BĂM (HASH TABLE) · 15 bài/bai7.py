class RehashHashTable:
    def __init__(self, initial_size=4):
        self.size = initial_size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def _hash(self, key, size):
        return abs(hash(key)) % size

    def put(self, key, value):
        idx = self._hash(key, self.size)
        for i, kv in enumerate(self.table[idx]):
            if kv[0] == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))
        self.count += 1

        if self.count / self.size > 0.75:
            self._rehash()

    def _rehash(self):
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]
        for bucket in self.table:
            for k, v in bucket:
                new_idx = self._hash(k, new_size)
                new_table[new_idx].append((k, v))
        self.size = new_size
        self.table = new_table
        print(f"-> Đã tăng kích thước bảng lên m = {self.size}")

if __name__ == "__main__":
    ht = RehashHashTable()
    print("Bài 7 - Đang thêm các phần tử để test Rehash:")
    ht.put(1, "A"); ht.put(2, "B"); ht.put(3, "C"); ht.put(4, "D")