# Input: [1,2,3], [1,1]

# Output: 1

# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.

# Input: [1,2], [1,2,3]

# Output: 2

# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
# You have 3 cookies and their sizes are big enough to gratify all of the children,
# You need to output 2.


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        num = 0
        i = 0
        j = 0
        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                num += 1
                j += 1
                i += 1
            else:
                j += 1
        return num
