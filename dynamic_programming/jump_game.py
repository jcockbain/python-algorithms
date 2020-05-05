# brute force recursion


def canJump1(nums):
    memo = [2 for _ in range(len(nums))]
    memo[-1] = 0

    def canJumpFromPosition(pos, nums):
        if memo[pos] != 2:
            return memo[pos] == 0

        furthestJump = min(pos + nums[pos], len(nums) - 1)
        for p in range(pos + 1, furthestJump + 1):
            if canJumpFromPosition(p, nums):
                memo[pos] = 0
                return True

        memo[pos] = 1
        return False

    return canJumpFromPosition(0, nums)

# top-down


def canJump2(nums):
    memo = [2 for _ in range(len(nums))]
    memo[-1] = 0

    for i in range(len(nums) - 2, -1, -1):
        furthestJump = min(i + nums[i], len(nums) - 1)
        for j in range(i + 1, furthestJump + 1):
            if memo[j] == 0:
                memo[i] = 0
                break

    return memo[0] == 0

# bottom-up


def canJump3(nums):
    lastPos = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= lastPos:
            lastPos = i
    return lastPos == 0
