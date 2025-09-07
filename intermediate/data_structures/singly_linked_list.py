
from __future__ import annotations
from typing import Optional

class Node:
    __slots__ = ("val", "next")
    def __init__(self, val, nxt: Optional["Node"] = None):
        self.val = val
        self.next = nxt

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def insert_head(self, val):
        self.head = Node(val, self.head)

    def insert_tail(self, val):
        if not self.head:
            self.head = Node(val); return
        cur = self.head
        while cur.next: cur = cur.next
        cur.next = Node(val)

    def search(self, target):
        cur = self.head
        while cur:
            if cur.val == target: return True
            cur = cur.next
        return False

    def delete_first(self, target):
        dummy = Node(0, self.head); prev, cur = dummy, self.head
        while cur:
            if cur.val == target:
                prev.next = cur.next
                break
            prev, cur = cur, cur.next
        self.head = dummy.next

    def reverse(self):
        prev, cur = None, self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
