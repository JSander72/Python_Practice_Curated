# Activity Selection (Greedy)

def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    last_end = -1
    count = 0
    for start, end in activities:
        if start >= last_end:
            count += 1
            last_end = end
    return count
