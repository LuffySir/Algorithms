# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    blf = '([{'
    brt = ')]}'
    if s[0] in brt or s[len(s)-1] in blf:
        return False
    if len(s) % 2 != 0:
        return False
    order1, order2 = [], []
    i = 0
    while i < len(s):
        if s[i] in blf:
            if not s[i+1]:
                return False
            if s[i+1] in brt:
                if blf.index(s[i]) == brt.index(s[i+1]):
                    i += 1
                else:
                    return False
            else:
                order1.append(blf.index(s[i]))
        else:
            if blf[brt.index(s[i])] not in s[:i]:
                return False
            if order1[-1] == brt.index(s[i]) and len(order2) == 0:
                order1.pop()
            else:
                order2 = [brt.index(s[i])] + order2
        i += 1
    print(order1 == order2)
    return order1 == order2


def isValid2(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    print(stack == [])
    return stack == []

isValid2("()[]{}")