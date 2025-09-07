"""if_else.py
Demonstrate if/elif/else and truthiness.
Run: python if_else.py
"""
def classify(n: int) -> str:
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"

def main():
    for n in (-5, 0, 8):
        print(n, "->", classify(n))

if __name__ == "__main__":
    main()
