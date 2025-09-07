"""two_sum.py
Return indices of the two numbers that add up to target.
Time: O(n), Space: O(n)
"""
from typing import List
def two_sum(nums: List[int], target: int) -> list[int]:
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []
def main():
    print(two_sum([2,7,11,15], 9))  # [0,1]
if __name__ == "__main__":
    main()
