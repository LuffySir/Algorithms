# Given an array and a value, remove all instances of that value in place and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], end = nums[end], end - 1
            else:
                start += 1
        return start

