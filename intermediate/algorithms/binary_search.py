def binary_search(a, x):
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if a[mid] == x: return mid
        if a[mid] < x:  lo = mid+1
        else:           hi = mid-1
    return -1

def binary_search_recursive(a, x, lo=0, hi=None):
    """Recursive binary search. Returns index or -1."""
    if hi is None:
        hi = len(a) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        return binary_search_recursive(a, x, mid + 1, hi)
    else:
        return binary_search_recursive(a, x, lo, mid - 1)

# Demo/test for binary_search_recursive
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    print("Array:", arr)
    for target in [7, 2]:
        idx = binary_search_recursive(arr, target)
        print(f"Index of {target}: {idx}")
