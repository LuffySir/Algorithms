#  Find the sum of all left leaves in a given binary tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            sum += root.left.val
        sum += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return sum

    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        s = [root]
        res = 0
        while s:
            tmp = s.pop()
            if tmp.left:
                s.append(tmp.left)
                if not tmp.left.left and not tmp.left.right:
                    res += tmp.left.val
            if tmp.right:
                s.append(tmp.right)
        return res
