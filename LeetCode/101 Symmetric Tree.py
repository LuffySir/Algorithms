# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(L,R):
            if not L and not R: return True
            if not L or not R: return False
            return L.val == R.val and helper(L.left,R.right) and helper(L.right,R.left)
        return helper(root,root)

