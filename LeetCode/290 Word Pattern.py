# Given a pattern and a string str, find if str follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
#
# Examples:
#
#     pattern = "abba", str = "dog cat cat dog" should return true.
#     pattern = "abba", str = "dog cat cat fish" should return false.
#     pattern = "aaaa", str = "dog cat cat dog" should return false.
#     pattern = "abba", str = "dog dog dog dog" should return false.


def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    words = str.split(' ')
    dict1, dict2 = {}, {}
    for pos, val in enumerate(pattern):
        dict1[val] = pos
    for pos, val in enumerate(words):
        dict2[val] = pos
    print(dict1, dict2)
    print(sorted(dict1.values()) == sorted(dict2.values()))
    return sorted(dict1.values()) == sorted(dict2.values())

wordPattern("abba", "dog cat cat dog")

def wordPattern1(pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
