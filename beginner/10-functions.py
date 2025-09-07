"""10-functions.py
Pure vs. impure functions; default args; docstrings.
"""
def greet(name:str="World")->str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"

def main():
    print(greet())
    print(greet("James"))
if __name__ == "__main__":
    main()
