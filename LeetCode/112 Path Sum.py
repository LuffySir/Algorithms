#  Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        cur = 0
        sums = self.helper(root, 0, [])
        return sum in sums

    def helper(self, root, res, list):
        if root:
            res += root.val
            if not root.left and not root.right:
                list.append(res)
            else:
                self.helper(root.left, res, list)
                self.helper(root.right, res, list)
        return list

# others
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # 1:27
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)