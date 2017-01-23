# Given a binary array, find the maximum number of consecutive 1s in this array.


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxHere, res = 0, 0
        for n in nums:
            maxHere = 0 if n == 0 else maxHere + 1
            res = max(res, maxHere)
        return res

