# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

from collections import Counter


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val_num = Counter(nums)
        tup = val_num.most_common(1)
        res, times = tup[0]
        return res

        # return sorted(num)[len(num)/2]

