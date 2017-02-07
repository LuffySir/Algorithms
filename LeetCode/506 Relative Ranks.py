# Given scores of N athletes, find their relative ranks and the people with the top three highest scores,
# who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal",
# "Silver Medal" and "Bronze Medal".
# For the left two athletes, you just need to output their relative ranks according to their scores.


def findRelativeRanks(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    sort = sorted(nums)[::-1]
    res = [0 for i in range(len(nums))]
    for pos, num in enumerate(sort):
        k = nums.index(num)
        if pos == 0:
            res[k] = 'Gold Medal'
        elif pos == 1:
            res[k] = 'Silver Medal'
        elif pos == 2:
            res[k] = 'Bronze Medal'
        else:
            res[k] = str(pos+1)
    print(res)
    return res

findRelativeRanks([10, 3, 8, 9, 4])


