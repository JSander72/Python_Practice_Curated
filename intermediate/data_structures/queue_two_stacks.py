class MyQueue:
    def __init__(self): self._in, self._out = [], []
    def enqueue(self, x): self._in.append(x)
    def _pour(self):
        if not self._out:
            while self._in: self._out.append(self._in.pop())
    def dequeue(self):
        self._pour(); return self._out.pop()
    def peek(self):
        self._pour(); return self._out[-1]
    def empty(self): return not self._in and not self._out
