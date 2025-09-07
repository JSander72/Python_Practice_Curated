"""loops_for.py
Basic for-loop patterns.
Run: python loops_for.py
"""
def main():
    names = ["Ada", "Alan", "Grace"]
    # index + value via enumerate
    for i, name in enumerate(names):
        print(f"{i}: {name}")
    # break/continue demo
    for n in range(10):
        if n % 2 == 0:
            continue  # skip evens
        if n > 7:
            break     # stop early
        print("odd <= 7:", n)

if __name__ == "__main__":
    main()
