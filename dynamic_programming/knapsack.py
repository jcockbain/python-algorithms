# brute force recursion


def knapsack(profits, weights, capacity):
    def helper(currentIndex, capacity):
        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + \
                helper(currentIndex + 1, capacity - weights[currentIndex])

        profit2 = helper(currentIndex + 1, capacity)

        return max(profit1, profit2)

    return helper(0, capacity)

# top-down


def knapsack2(profits, weights, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]

    def helper(currentIndex, capacity):
        if capacity <= 0 or currentIndex >= len(profits):
            return 0

        if dp[currentIndex][capacity] != -1:
            return dp[currentIndex][capacity]

        profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + \
                helper(currentIndex + 1, capacity - weights[currentIndex])

        profit2 = helper(currentIndex + 1, capacity)

        dp[currentIndex][capacity] = max(profit1, profit2)
        return dp[currentIndex][capacity]

    return helper(0, capacity)


# bottom-up

def knapsack3(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = 0

    for c in range(0, capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i - 1][c - weights[i]]

            profit2 = dp[i - 1][c]

            dp[i][c] = max(profit1, profit2)

    return dp[n - 1][capacity]
