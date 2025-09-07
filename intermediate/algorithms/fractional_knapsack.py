# Fractional Knapsack (Greedy)

def fractional_knapsack(weights, values, W):
    idx = list(range(len(weights)))
    idx.sort(key=lambda i: values[i]/weights[i], reverse=True)
    total_value = 0
    for i in idx:
        if weights[i] <= W:
            total_value += values[i]
            W -= weights[i]
        else:
            total_value += values[i] * (W / weights[i])
            break
    return total_value
