class Stack:
    def __init__(self): self._a = []
    def push(self, x): self._a.append(x)        # amortized O(1)
    def pop(self):    return self._a.pop()      # O(1)
    def peek(self):   return self._a[-1] if self._a else None
    def empty(self):  return not self._a
