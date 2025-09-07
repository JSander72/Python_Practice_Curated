def quick_sort(a):
    if len(a) <= 1: return a
    pivot = a[len(a)//2]
    less  = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
