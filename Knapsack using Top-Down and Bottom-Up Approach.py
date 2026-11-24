# Top-Down Approach
def knapsack(w, v, c, n):
    if n == 0 or c == 0:
        return 0

    if w[n-1] > c:
        return knapsack(w, v, c, n-1)

    return max(v[n-1] + knapsack(w, v, c-w[n-1], n-1),
               knapsack(w, v, c, n-1))

# Bottom-Up Approach
def bottom_up(w, v, c):
    n = len(w)
    dp = [[0]*(c+1) for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(c+1):

            if w[i-1] <= j:
                dp[i][j] = max(v[i-1] + dp[i-1][j-w[i-1]],
                               dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][c]

w = [1, 3, 4, 5]
v = [1, 4, 5, 7]
c = 7

print("Top-Down:", knapsack(w, v, c, len(w)))
print("Bottom-Up:", bottom_up(w, v, c))
