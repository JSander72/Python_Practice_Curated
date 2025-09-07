"""simple_sdk_usage.py
Fake SDK pattern: a Client with .get/.create methods.
"""
class BooksClient:
    def __init__(self, store: dict | None = None):
        self.store = store or {}
    def get(self, book_id: str):
        return self.store.get(book_id)
    def create(self, book_id: str, title: str):
        self.store[book_id] = {"id": book_id, "title": title}
        return self.store[book_id]

def main():
    client = BooksClient()
    created = client.create("b1", "Clean Code")
    print("created:", created)
    print("get b1:", client.get("b1"))

if __name__ == "__main__":
    main()
