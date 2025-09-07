class CircularQueue:
    """Fixed-size circular queue using list; O(1) ops."""
    def __init__(self, k):
        self.q = [None]*k; self.k = k; self.size = 0; self.head = 0; self.tail = 0
    def enqueue(self, x):
        if self.size == self.k: raise IndexError("full")
        self.q[self.tail] = x; self.tail = (self.tail+1)%self.k; self.size += 1
    def dequeue(self):
        if self.size == 0: raise IndexError("empty")
        v = self.q[self.head]; self.q[self.head] = None; self.head = (self.head+1)%self.k; self.size -= 1; return v
    def front(self): return None if self.size==0 else self.q[self.head]
    def rear(self):  return None if self.size==0 else self.q[(self.tail-1)%self.k]
