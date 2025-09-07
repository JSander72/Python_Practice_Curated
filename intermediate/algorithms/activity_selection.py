def max_activities(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by finish time
    count, last_end = 0, float('-inf')
    for s,e in intervals:
        if s >= last_end:
            count += 1
            last_end = e
    return count
    
def activity_selection(activities):
    """activities: list of (start, end) tuples. Returns max set of non-overlapping activities."""
    # Sort by end time
    activities = sorted(activities, key=lambda x: x[1])
    result = []
    last_end = float('-inf')
    for start, end in activities:
        if start >= last_end:
            result.append((start, end))
            last_end = end
    return result

# Demo/test for activity_selection
if __name__ == "__main__":
    acts = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    selected = activity_selection(acts)
    print("Selected activities:", selected)
