"""oop_basics.py
Simple OOP: classes, methods, inheritance.
Run: python oop_basics.py
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says woof"

def main():
    pets = [Dog("Rex"), Animal("Blob")]
    for p in pets:
        print(p.speak())

if __name__ == "__main__":
    main()
