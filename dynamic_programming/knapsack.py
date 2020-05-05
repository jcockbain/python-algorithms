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
