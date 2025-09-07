"""02-strings.py
String manipulation and f-strings.
"""
def main():
    name = "James"
    msg = f"Hello, {name}!"
    print(msg.upper())
    print("trim".strip())
    print(",".join(["a","b","c"]))
if __name__ == "__main__":
    main()
