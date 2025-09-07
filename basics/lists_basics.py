"""lists_basics.py
Show common list operations with clear examples.
Run: python lists_basics.py
"""
def main():
    nums = [1, 3, 5]
    # append adds to end
    nums.append(7)            # [1, 3, 5, 7]
    # insert adds at index
    nums.insert(1, 2)         # [1, 2, 3, 5, 7]
    # extend merges another iterable
    nums.extend([9, 11])      # [1, 2, 3, 5, 7, 9, 11]
    # slicing returns a new list
    odds = nums[::2]
    # list comprehension builds a new list in one line
    squares = [n*n for n in nums]

    print("nums:", nums)
    print("odds:", odds)
    print("squares:", squares)

if __name__ == "__main__":
    main()
