# brute-force


def longestPalindromicSubstring1(s):
    def longest_pal(startIndex, endIndex):
        if startIndex > endIndex:
            return 0

        if startIndex == endIndex:
            return 1

        if s[startIndex] == s[endIndex]:
            remainingLength = endIndex - startIndex - 1

            if remainingLength == longest_pal(startIndex + 1, endIndex - 1):
                return remainingLength + 2

        c1 = longest_pal(startIndex + 1, endIndex)
        c2 = longest_pal(startIndex, endIndex - 1)

        return max(c1, c2)

    return longest_pal(0, len(s) - 1)


def longestPalindromicSubstring2(s):
    n = len(s)
    dp = [[-1 for _ in range(n)] for _ in range(n)]

    def longest_pal(startIndex, endIndex):
        if startIndex > endIndex:
            return 0

        if startIndex == endIndex:
            return 1

        if dp[startIndex][endIndex] == -1:
            if s[startIndex] == s[endIndex]:
                remainingLength = endIndex - startIndex - 1

                if remainingLength == longest_pal(startIndex + 1, endIndex - 1):
                    dp[startIndex][endIndex] = 2 + remainingLength
                    return dp[startIndex][endIndex]

            c1 = longest_pal(startIndex + 1, endIndex)
            c2 = longest_pal(startIndex, endIndex - 1)
            dp[startIndex][endIndex] = max(c1, c2)

        return dp[startIndex][endIndex]

    return longest_pal(0, len(s) - 1)


def longestPalindromicSubstring3(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    maxLength = 1

    for startIndex in range(n-1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if s[startIndex] == s[endIndex]:
                if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                    dp[startIndex][endIndex] = True
                    maxLength = max(maxLength, endIndex - startIndex + 1)

    return maxLength

