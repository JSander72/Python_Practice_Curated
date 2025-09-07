"""valid_parentheses.py
Stack pattern. Time O(n), Space O(n).
"""
def is_valid(s: str) -> bool:
    pairs = {')':'(', ']':'[', '}':'{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs.get(ch, None):
                return False
            stack.pop()
    return not stack
def main():
    print(is_valid("()[]{}"))     # True
    print(is_valid("(]"))         # False
if __name__ == "__main__":
    main()
