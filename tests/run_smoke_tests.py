from pathlib import Path
from intermediate.data_structures.arrays_ops import insert, delete, reverse, rotate_right
import sys
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def ok(name, cond):
    print(f"[OK] {name}" if cond else f"[FAIL] {name}")
    if not cond: sys.exit(1)

# Arrays
from intermediate.data_structures.arrays_ops import insert, delete, reverse, rotate_right
a = [1,2,4]; ok("insert", insert(a,2,3)==[1,2,3,4])
ok("delete", delete(a,1)==[1,3,4])
ok("reverse", reverse([1,2,3])==[3,2,1])
ok("rotate_right", rotate_right([1,2,3,4,5],2)==[4,5,1,2,3])

# Linked list
from intermediate.data_structures.singly_linked_list import LinkedList, has_cycle, Node
ll = LinkedList(); [ll.insert_tail(i) for i in [1,2,3]]
ok("ll.search", ll.search(2) and not ll.search(5))
ll.delete_first(2); ok("ll.delete_first", ll.search(2)==False)
ll.reverse(); ok("ll.reverse", ll.head.val==3)
n1,n2,n3 = Node(1), Node(2), Node(3); n1.next=n2; n2.next=n3; n3.next=n1
ok("ll.has_cycle", has_cycle(n1)==True)

# Stack & Queue
from intermediate.data_structures.stack_array import Stack
s = Stack(); s.push(1); s.push(2); ok("stack.peek", s.peek()==2); ok("stack.pop", s.pop()==2)

from intermediate.data_structures.queue_two_stacks import MyQueue
q = MyQueue(); q.enqueue(1); q.enqueue(2); ok("queue.peek", q.peek()==1); ok("queue.dequeue", q.dequeue()==1)

# BST
from intermediate.data_structures.bst_ops import insert, search, delete, Node as BSTNode
r = None
for x in [5,3,7,2,4,6,8]: r = insert(r, x)
ok("bst.search", search(r, 4) and not search(r, 10))
r = delete(r, 7); ok("bst.delete", search(r,7)==False)

# HashMap
from intermediate.data_structures.hash_table_chaining import HashMap
hm = HashMap(); hm.put("a",1); hm.put("b",2); ok("hash.get", hm.get("a")==1); hm.put("a",3); ok("hash.update", hm.get("a")==3); ok("hash.remove", hm.remove("b")==True)

# Searching/Sorting
from intermediate.algorithms.linear_search import linear_search
from intermediate.algorithms.binary_search import binary_search
from intermediate.algorithms.bubble import bubble_sort
from intermediate.algorithms.insertion import insertion_sort
from intermediate.algorithms.merge import merge_sort
from intermediate.algorithms.quick import quick_sort

ok("linear_search", linear_search([3,1,2],1)==1)
ok("binary_search", binary_search([1,2,3,4,5],4)==3)
ok("bubble_sort", bubble_sort([3,2,1])==[1,2,3])
ok("insertion_sort", insertion_sort([3,1,2])==[1,2,3])
ok("merge_sort", merge_sort([5,2,4,6,1,3])==[1,2,3,4,5,6])
ok("quick_sort", quick_sort([3,5,1,2,4])==[1,2,3,4,5])

# Recursion & DP & Greedy
from intermediate.algorithms.factorial import factorial
from intermediate.algorithms.fib_recursive_vs_memo import fib_recursive, fib_memo
from intermediate.algorithms.climb_stairs import climb_stairs
from intermediate.algorithms.coin_change_min_coins import coin_change_min
from intermediate.algorithms.activity_selection import max_activities
from intermediate.algorithms.fractional_knapsack import fractional_knapsack

ok("factorial", factorial(5)==120)
ok("fib_recursive", fib_recursive(5)==5)
ok("fib_memo", fib_memo(30)==832040)
ok("climb_stairs", climb_stairs(5)==8)
ok("coin_change_min", coin_change_min([1,2,5],11)==3)
ok("activity_selection", max_activities([(1,3),(2,5),(4,6),(6,7)])==3)
ok("fractional_knapsack", abs(fractional_knapsack([(60,10),(100,20),(120,30)], 50) - 240.0) < 1e-6)

print("\nAll smoke tests passed. You’re assessment-ready.\n")
