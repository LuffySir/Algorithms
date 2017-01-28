# Given a positive integer num, write a function which returns True if num is a perfect square else False.


class Solution(object):
    # a square number is 1+3+5+7+... Time Complexity O(sqrt(N)) (Credit to lizhibupt, thanks for correcting this).
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        if num < 1:
            return False
        while num > 0:
            num -= i
            i += 2
        return num == 0

    # binary search. Time Complexity O(logN)
    def isPerfectSquare1(self,num):
        low = 1
        high = num
        while low <= high:
            mid = (low + high) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False



