class HashMap:
    """Educational separate-chaining hash map."""
    def __init__(self, capacity=8):
        self.n = 0
        self.cap = capacity
        self.buckets = [[] for _ in range(self.cap)]

    def _index(self, key): return hash(key) % self.cap

    def put(self, key, value):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i,(k,_) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value); return
        bucket.append((key, value)); self.n += 1
        if self.n/self.cap > 0.75: self._rehash()

    def get(self, key, default=None):
        idx = self._index(key)
        for (k,v) in self.buckets[idx]:
            if k == key: return v
        return default

    def remove(self, key):
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i,(k,_) in enumerate(bucket):
            if k == key:
                bucket.pop(i); self.n -= 1; return True
        return False

    def _rehash(self):
        old = self.buckets
        self.cap *= 2
        self.buckets = [[] for _ in range(self.cap)]
        self.n = 0
        for bucket in old:
            for (k,v) in bucket:
                self.put(k, v)
