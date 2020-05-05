# top-down


def rob(nums):
    maxes = [0 for _ in range(len(nums))]
    maxes[0] = nums[0]
    maxes[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        maxes[i] = max(maxes[i-2] + nums[i], maxes[i-1])

    return maxes[-1]

# bottom-up


def rob2(nums):
    prevMax = 0
    currMax = 0

    for x in nums:
        temp = currMax
        currMax = max(prevMax + x, currMax)
        prevMax = temp

    return currMax
