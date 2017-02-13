# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.

# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    res = []
    n, m = len(s), len(p)
    if n < m: return res
    # A-Za-z => 122
    phash, shash = [0] * 123, [0] * 123
    for x in p:
        phash[ord(x)] += 1
    for x in s[:m - 1]:
        shash[ord(x)] += 1
    for i in range(m - 1, n):
        shash[ord(s[i])] += 1
        if i - m >= 0:
            shash[ord(s[i - m])] -= 1
        if shash == phash:
            res.append(i - m + 1)
    return res

findAnagrams('cbaebabacd', 'abc')