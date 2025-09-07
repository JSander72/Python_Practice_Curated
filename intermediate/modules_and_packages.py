"""modules_and_packages.py
Demonstrate importing from a local package.
Run: python modules_and_packages.py
"""
from pkg_demo import mathy

def main():
    print(mathy.double(21))
    print(mathy.add(10, 5))

if __name__ == "__main__":
    main()
