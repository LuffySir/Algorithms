#  Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# For example,
# Given nums = [0, 1, 3] return 2.


class Solution(object):
    # sum
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)

    # XOR
    def missingNumber1(self,nums):
        n = len(nums)
        res = 0
        for i in range(n):
            res ^= nums[i]
            res ^= i
        return res



