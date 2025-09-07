# Common Trade-offs

- **Array vs Linked List**: Arrays give O(1) index access; LL gives O(1) head insert/delete.
- **BST vs Hash Table**: BST keeps order and supports range queries; HashMap is average O(1) but unordered.
- **Recursion vs Iteration**: Recursion is expressive but risks stack overflow; iteration controls space.
- **Time vs Space**: Use extra memory (hashing, DP tables) to cut time when needed.
