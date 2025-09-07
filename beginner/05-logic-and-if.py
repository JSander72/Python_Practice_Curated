"""05-logic-and-if.py
Boolean logic with if/elif/else.
"""
def is_teen(age:int)->bool:
    return 13 <= age <= 19

def main():
    for a in (12,15,22):
        print(a, "is teen?", is_teen(a))
if __name__ == "__main__":
    main()
