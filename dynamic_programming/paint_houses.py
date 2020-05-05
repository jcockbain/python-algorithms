# brute force recursion


def minCost1(costs):
    def paint_cost(n, color):
        total_cost = costs[n][color]
        if n == len(costs) - 1:
            pass
        elif color == 0:
            total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
        elif color == 1:
            total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
        else:
            total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
        return total_cost

    if costs == []:
        return 0
    return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))

# top-down


def minCost2(costs):
    def paint_cost(n, color):
        if (n, color) in memo:
            return memo[(n, color)]
        total_cost = costs[n][color]
        if n == len(costs) - 1:
            pass
        elif color == 0:
            total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
        elif color == 1:
            total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
        else:
            total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
        memo[(n, color)] = total_cost
        return total_cost

    if costs == []:
        return 0

    memo = {}
    return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))

# bottom-up


def minCost3(costs):
    for n in reversed(range(len(costs) - 1)):
        costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
        costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
        costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

    if len(costs) == 0:
        return 0
    return min(costs[0])
