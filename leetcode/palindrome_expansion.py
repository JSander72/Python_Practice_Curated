"""palindrome_expansion.py
Expand-around-center to get longest palindrome substring.
Time: O(n^2) worst-case, Space: O(1)
"""
def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]

def longest_palindrome(s: str) -> str:
    best = ""
    for i in range(len(s)):
        best = max(best, expand(s,i,i), expand(s,i,i+1), key=len)
    return best

def main():
    print(longest_palindrome("babad"))  # 'bab' or 'aba'
if __name__ == "__main__":
    main()
