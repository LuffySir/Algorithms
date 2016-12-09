# Write a function that takes a string as input and returns the string reversed


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = ''
        for x in s:
            rs = x + rs
        return rs
        # return s[::-1]
