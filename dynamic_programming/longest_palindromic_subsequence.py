# brute-force recursive


def find_lps_1(st):

    def longest_pal(s, startIndex, endIndex):
        if startIndex > endIndex:
            return 0

        if startIndex == endIndex:
            return 1

        if s[startIndex] == s[endIndex]:
            return 2 + longest_pal(s, startIndex + 1, endIndex - 1)

        c1 = longest_pal(s, startIndex + 1, endIndex)
        c2 = longest_pal(s, startIndex, endIndex - 1)

        return max(c1, c2)

    return longest_pal(st, 0, len(st) - 1)


# top-down


def find_lps_2(st):
    n = len(st)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    def longest_pal(s, startIndex, endIndex):
        if startIndex > endIndex:
            return 0

        if startIndex == endIndex:
            return 1

        if dp[startIndex][endIndex] == -1:
            if s[startIndex] == s[endIndex]:
                dp[startIndex][endIndex] = 2 + \
                    longest_pal(s, startIndex + 1, endIndex - 1)
            else:
                c1 = longest_pal(s, startIndex + 1, endIndex)
                c2 = longest_pal(s, startIndex, endIndex - 1)
                dp[startIndex][endIndex] = max(c1, c2)

        return dp[startIndex][endIndex]

    return longest_pal(st, 0, len(st) - 1)


def find_lps_3(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if s[startIndex] == s[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            else:
                dp[startIndex][endIndex] = max(
                    dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])

    return dp[0][n-1]
