def coin_change_min(coins, amount):
    """Return min coins to make amount; INF->-1. O(amount*len(coins))."""
    INF = amount+1
    dp = [INF]*(amount+1)
    dp[0] = 0
    for c in coins:
        for a in range(c, amount+1):
            dp[a] = min(dp[a], dp[a-c] + 1)
    return dp[amount] if dp[amount] != INF else -1
