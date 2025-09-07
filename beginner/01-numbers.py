"""01-numbers.py
Integer / float basics with simple arithmetic.
Run: python 01-numbers.py
"""
def main():
    a, b = 7, 3
    print("add:", a + b)
    print("div:", a / b)        # float division
    print("floor div:", a // b) # integer division
    print("mod:", a % b)
    print("pow:", a ** b)
if __name__ == "__main__":
    main()
