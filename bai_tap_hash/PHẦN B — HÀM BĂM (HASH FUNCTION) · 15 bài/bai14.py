class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bits = [0] * size

    def hash1(self, item):
        return hash(item) % self.size

    def hash2(self, item):
        return (hash(item) * 7) % self.size

    def hash3(self, item):
        return (hash(item) * 13) % self.size

    def add(self, item):
        self.bits[self.hash1(item)] = 1
        self.bits[self.hash2(item)] = 1
        self.bits[self.hash3(item)] = 1

    def contains(self, item):
        return (
            self.bits[self.hash1(item)] and
            self.bits[self.hash2(item)] and
            self.bits[self.hash3(item)]
        )


bf = BloomFilter(20)

bf.add("apple")
bf.add("banana")
bf.add("orange")

print(bf.contains("apple"))
print(bf.contains("banana"))
print(bf.contains("grape"))