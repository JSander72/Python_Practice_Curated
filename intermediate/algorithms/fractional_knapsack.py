def fractional_knapsack(items, capacity):
    """items: list of (value, weight). Returns max value (float)."""
    items = sorted(items, key=lambda vw: vw[0]/vw[1], reverse=True)
    total = 0.0
    for v,w in items:
        if capacity == 0: break
        take = min(w, capacity)
        total += v * (take / w)
        capacity -= take
    return total
