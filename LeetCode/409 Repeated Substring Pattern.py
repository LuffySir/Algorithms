# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple
# copies of the substring together. You may assume the given string consists of lowercase English letters
# only and its length will not exceed 10000.


class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if str == '':
            return False
        str_len = len(str)
        for i in range(1, str_len):
            sub = str[:i]
            if str_len % len(sub) == 0:
                if sub * (str_len / len(sub)) == str:
                    return True
        return False
