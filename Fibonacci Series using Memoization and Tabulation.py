# Memoization
def memo(n, dp):
    if n <= 1:
        return n

    if n not in dp:
        dp[n] = memo(n-1, dp) + memo(n-2, dp)

    return dp[n]

n = 10
print("Memoization:", memo(n, {}))

# Tabulation
def tabulation(n):
    dp = [0] * (n+1)

    if n >= 1:
        dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print("Tabulation:", tabulation(n))
