def longestIncreasingSubsequence(nums):

    def find_LIS(currentIndex, previousIndex):
        if currentIndex == len(nums):
            return 0

        c1 = 0

        if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
            c1 = 1 + find_LIS(currentIndex + 1, currentIndex)

        c2 = find_LIS(currentIndex + 1, previousIndex)

        return max(c1, c2)

    return find_LIS(0, -1)


def longestIncreasingSubsequence2(nums):
    n = len(nums)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

    def find_LIS(currentIndex, previousIndex):
        if currentIndex == len(nums):
            return 0

        if dp[currentIndex][previousIndex + 1] == -1:
            c1 = 0

            if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
                c1 = 1 + find_LIS(currentIndex + 1, currentIndex)

            c2 = find_LIS(currentIndex + 1, previousIndex)
            dp[currentIndex][previousIndex + 1] = max(c1, c2)

        return dp[currentIndex][previousIndex + 1]

    return find_LIS(0, -1)


def longestIncreasingSubsequence3(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = 1

    maxLength = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                maxLength = max(maxLength, dp[i])

    return maxLength
