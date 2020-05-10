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
