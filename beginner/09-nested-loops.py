"""09-nested-loops.py
Print a small multiplication table.
"""
def main():
    for i in range(1,4):
        row = []
        for j in range(1,4):
            row.append(i*j)
        print(row)
if __name__ == "__main__":
    main()
