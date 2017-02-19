# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n, generate the nth sequence.
#
# Note: The sequence of integers will be represented as a string.


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    curr = '1'
    for _ in range(n - 1):
        count = 0
        say = curr[0]
        res = ''
        for c in curr:
            if say != c:
                res += str(count) + say
                say = c
                count = 1
            else:
                count += 1
        res += str(count) + say
        curr = res
    print(curr)
    return curr

countAndSay(1)
