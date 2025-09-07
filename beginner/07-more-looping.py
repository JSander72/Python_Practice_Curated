"""07-more-looping.py
Comprehensions and generator expressions.
"""
def main():
    squares = [n*n for n in range(6)]
    evens = (n for n in range(10) if n%2==0)
    print("squares:", squares)
    print("first three evens:", [next(evens) for _ in range(3)])
if __name__ == "__main__":
    main()
