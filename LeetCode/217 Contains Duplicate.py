# Given an array of integers, find if the array contains any duplicates. Your function should
# return true if any value appears at least twice in the array, and it should return false
# if every element is distinct.


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_dict = {}
        for i in nums:
            num_dict[i] = num_dict.get(i, 0) + 1
            if num_dict[i] > 1:
                return False
        return True

    def containsDuplicate1(self, nums):
        return len(nums) > len(set(nums))
