"""06-loop-basics.py
for and while with counters.
"""
def main():
    total = 0
    for n in range(1,6):
        total += n
    print("sum 1..5:", total)

    # while loop
    count = 3
    while count > 0:
        print("tick", count)
        count -= 1
if __name__ == "__main__":
    main()
