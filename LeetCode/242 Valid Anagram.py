# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.


class Solution(object):
    # 超时
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if m != n:
            return False
        else:
            for c in s:
                if c not in t:
                    return False
                else:
                    pos = t.index(c)
                    t = t[:pos] + t[pos + 1:]
            return True

    def isAnagram1(self, s, t):
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2
