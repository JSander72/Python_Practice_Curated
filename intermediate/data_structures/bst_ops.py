class Node:
    __slots__=("val","left","right")
    def __init__(self,val): self.val,self.left,self.right = val,None,None

def insert(root, x):
    if not root: return Node(x)
    if x < root.val:   root.left  = insert(root.left, x)
    elif x > root.val: root.right = insert(root.right, x)
    return root

def search(root, x):
    while root:
        if x == root.val: return True
        root = root.left if x < root.val else root.right
    return False

def find_min(node):
    while node and node.left: node = node.left
    return node

def delete(root, x):
    if not root: return None
    if x < root.val: root.left = delete(root.left, x)
    elif x > root.val: root.right = delete(root.right, x)
    else:
        if not root.left:  return root.right
        if not root.right: return root.left
        succ = find_min(root.right)
        root.val = succ.val
        root.right = delete(root.right, succ.val)
    return root
