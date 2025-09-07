"""04-user-input.py
Use input() safely by converting to int and validating.
"""
def main():
    raw = "5"  # pretend input() for non-interactive example
    try:
        n = int(raw)
        print(n, "squared =", n*n)
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()
