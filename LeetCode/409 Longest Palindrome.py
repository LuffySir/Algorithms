# Given a string which consists of lowercase or uppercase letters, find the length of the
# longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = 0
        vals = Counter(s).values()
        for times in vals:
            if times % 2 == 1:
                odd += 1
        return (len(s) - odd + 1) if odd > 0 else len(s)

    def longestPalindrome1(self, s):
        # v & 1即判断是否为奇数
        odds = sum(v & 1 for v in Counter(s).values())
        return len(s) - odds + bool(odds)
