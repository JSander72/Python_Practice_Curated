def max_activities(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by finish time
    count, last_end = 0, float('-inf')
    for s,e in intervals:
        if s >= last_end:
            count += 1
            last_end = e
    return count
