# Given a non-empty integer array of size n, find the minimum number of moves required to
# make all array elements equal, where a move is incrementing n - 1 elements by 1.

# Input:
# [1,2,3]

# Output:
# 3

# Explanation:
# Only three moves are needed (remember each move increments two elements):

# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        s = min(nums)
        add_num = sum(nums)
        # N个数累加和+每次加的值*次数 = N*最后每个元素的值
        # sum + (N-1) *t = N * b
        # 最小值+次数=最后的值（最小值每次都要加）
        # s + t = b
        t = add_num - N * s
        return t
