def bubble_sort(a):
    n = len(a)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                swapped = True
    return a
