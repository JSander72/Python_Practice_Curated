"""03-list-basics.py
Create, read, update, delete (CRUD) with lists.
"""
def main():
    data = [1,2,3]
    data.append(4)
    data[0] = 99
    del data[2]
    print(data)  # [99,2,4]
if __name__ == "__main__":
    main()
