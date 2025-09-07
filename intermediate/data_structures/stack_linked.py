# Stack using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinked:
    def __init__(self):
        self.top = None
