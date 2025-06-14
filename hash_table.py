import random

class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.p = 10**9 + 7  # Large prime number
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def _hash(self, key):
        # Universal hash function
        h = hash(key)  # built-in hash function
        return ((self.a * h + self.b) % self.p) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def __str__(self):
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.table) if bucket)

