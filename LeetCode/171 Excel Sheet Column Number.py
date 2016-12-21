# Given a column title as appear in an Excel sheet, return its corresponding column number.
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in range(len(s) - 1, -1, -1):
            num += (ord(s[len(s) - 1 - i]) - ord('A') + 1) * 26 ** i
        return num

# return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])
