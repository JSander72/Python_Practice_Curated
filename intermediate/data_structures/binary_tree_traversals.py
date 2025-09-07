from collections import deque

class Node:
    __slots__=("val","left","right")
    def __init__(self,val,left=None,right=None):
        self.val,self.left,self.right = val,left,right

def preorder(root):
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        if not node: continue
        res.append(node.val)
        stack.append(node.right); stack.append(node.left)
    return res

def inorder(root):
    res, stack, cur = [], [], root
    while stack or cur:
        while cur:
            stack.append(cur); cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res

def postorder(root):
    res, stack, last = [], [], None
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur); cur = cur.left
        else:
            node = stack[-1]
            if node.right and last is not node.right:
                cur = node.right
            else:
                res.append(node.val); last = stack.pop()
    return res

def level_order(root):
    if not root: return []
    res, q = [], deque([root])
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return res
