"""Basic array operations with time/space notes."""
def insert(arr, idx, val):
    """Insert val at idx (0<=idx<=len). O(n) time due to shifts."""
    arr[idx:idx] = [val]
    return arr

def delete(arr, idx):
    """Delete element at idx. O(n) due to shifts."""
    del arr[idx]
    return arr

def reverse(arr):
    """Reverse in-place. O(n)."""
    i, j = 0, len(arr)-1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1; j -= 1
    return arr

def rotate_right(arr, k):
    """Rotate right by k. O(n)."""
    n = len(arr)
    if n == 0: return arr
    k %= n
    arr[:] = arr[-k:] + arr[:-k]

    return arr

def rotate_left(arr, k):
    """Rotate left by k. O(n)."""
    n = len(arr)
    if n == 0:
        return arr
    k %= n
    arr[:] = arr[k:] + arr[:k]
    return arr

# Demo/test for rotate_left
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Original:", arr)
    rotate_left(arr, 2)
    print("After rotate_left by 2:", arr)
