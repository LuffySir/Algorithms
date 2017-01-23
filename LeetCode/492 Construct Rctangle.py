# 1. The area of the rectangular web page you designed must equal to the given target area.

# 2. The width W should not be larger than the length L, which means L >= W.

# 3. The difference between length L and width W should be as small as possible.


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        dd = {}
        for w in range(1, int(math.sqrt(area))+2):
            if area % w == 0:
                L = int(area / w)
                if L >= w:
                    diff = L - w
                    dd[diff] = (L,w)
                else:
                    pass
        min_diff = min(dd.keys())
        return dd[min_diff]
