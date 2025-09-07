def climb_stairs(n):
    if n <= 2: return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a+b
    return b  # O(n) time, O(1) space

def climb_stairs_k_steps(n, k):
    """DP: Number of ways to climb n stairs with up to k steps at a time."""
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]
    return dp[n]

# Demo/test for climb_stairs_k_steps
if __name__ == "__main__":
    n, k = 5, 3
    print(f"Ways to climb {n} stairs with up to {k} steps: {climb_stairs_k_steps(n, k)}")
