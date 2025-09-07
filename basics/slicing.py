"""slicing.py
Common slicing patterns on strings and lists.
Run: python slicing.py
"""
def main():
    s = "abcdefg"
    print(s[0:3])     # 'abc'
    print(s[-3:])     # 'efg'
    print(s[::2])     # 'aceg'
    data = [10,20,30,40,50,60]
    print(data[1:4])  # [20,30,40]
    print(list(reversed(data)))  # [60,50,40,30,20,10]

if __name__ == "__main__":
    main()
