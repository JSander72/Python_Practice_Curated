# Queue using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinked:
    def __init__(self):
        self.front = None
        self.rear = None
