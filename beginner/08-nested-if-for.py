"""08-nested-if-for.py
Nested control flow with early exit.
"""
def first_even_divisible_by(nums, k):
    for n in nums:
        if n % 2 == 0:
            if n % k == 0:
                return n
    return None

def main():
    nums = [3,5,6,9,12,14]
    print(first_even_divisible_by(nums, 3))  # 6
if __name__ == "__main__":
    main()
