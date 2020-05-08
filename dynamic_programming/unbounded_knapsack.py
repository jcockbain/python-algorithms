def unboundedKnapsack1(profits, weights, capacity):
    return solve_knapsack_recursive(profits, weights, capacity, 0)


def solve_knapsack_recursive(profits, weights, capacity, currentIndex):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n or currentIndex >= n:
        return 0

    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + solve_knapsack_recursive(
            profits, weights, capacity - weights[currentIndex], currentIndex)

    profit2 = solve_knapsack_recursive(
        profits, weights, capacity, currentIndex + 1)

    return max(profit1, profit2)


def unboundedKnapsack2(profits, weights, capacity):
    n = len(profits)
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(n)]

    def solve_knapsack_recursive(profits, weights, capacity, currentIndex):
        if capacity <= 0 or n == 0 or len(weights) != n or currentIndex >= n:
            return 0

        if dp[currentIndex][capacity] == -1:
            profit1 = 0
            if weights[currentIndex] <= capacity:
                profit1 = profits[currentIndex] + solve_knapsack_recursive(
                    profits, weights, capacity - weights[currentIndex], currentIndex)

            profit2 = solve_knapsack_recursive(
                profits, weights, capacity, currentIndex + 1)

            dp[currentIndex][capacity] = max(profit1, profit2)

        return dp[currentIndex][capacity]

    return solve_knapsack_recursive(profits, weights, capacity, 0)
