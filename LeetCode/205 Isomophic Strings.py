# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.


def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dict1, dict2 = {}, {}
    for pos, val in enumerate(s):
        dict1[val] = dict1.get(val, []) + [pos]
    for pos, val in enumerate(t):
        dict2[val] = dict2.get(val, []) + [pos]
    print(sorted(dict1.values()) == sorted(dict2.values()))
    return sorted(dict1.values()) == sorted(dict2.values())


isIsomorphic('arr', 'rar')
