# Given an integer, write a function to determine if it is a power of two.


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if bin(n).count('1') == 1 and n > 0:
            return True
        else:
            return False
