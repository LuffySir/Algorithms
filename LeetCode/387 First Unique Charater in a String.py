# Given a string, find the first non-repeating character in it and
# return it's index. If it doesn't exist, return -1.

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s)
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1
