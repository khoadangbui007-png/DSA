class ChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def put(self, key, value):
        idx = abs(hash(key)) % self.size
        for i, kv in enumerate(self.table[idx]):
            if kv[0] == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def remove(self, key):
        idx = abs(hash(key)) % self.size
        for i, kv in enumerate(self.table[idx]):
            if kv[0] == key:
                self.table[idx].pop(i)
                return True
        return False

class OpenAddressingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.DELETED = "DELETED"

    def put(self, key, value):
        idx = abs(hash(key)) % self.size
        start = idx
        while self.keys[idx] is not None and self.keys[idx] != self.DELETED:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            idx = (idx + 1) % self.size
            if idx == start: return
        self.keys[idx] = key
        self.values[idx] = value

    def remove(self, key):
        idx = abs(hash(key)) % self.size
        start = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.keys[idx] = self.DELETED
                self.values[idx] = None
                return True
            idx = (idx + 1) % self.size
            if idx == start: break
        return False

if __name__ == "__main__":
    cc = ChainingHashTable()
    oa = OpenAddressingHashTable()
    cc.put("test", 123)
    oa.put("test", 456)
    
    print("BÁO CÁO KẾT QUẢ SO SÁNH (BÀI 6)")
    print("1. BỘ NHỚ: Chaining tốn hơn do cần danh sách phụ. Open Addressing tiết kiệm hơn[cite: 1].")
    print("2. HỆ SỐ TẢI CAO: Chaining chạy ổn định. Open Addressing chậm nặng do gom cụm[cite: 1].")
    print("3. XỬ LÝ XÓA: Chaining xóa rất dễ. Open Addressing phải xóa lười bằng nhãn DELETED[cite: 1].")
