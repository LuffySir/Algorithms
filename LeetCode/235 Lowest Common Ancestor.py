# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p,q = q,p
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > q.val:
                root = root.left
            else:
                return root

    # 递归
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p,q = q,p

        if root.val < p.val:
            return self.lowestCommonAncestor1(root.right,p,q)
        elif root.val > q.val:
            return self.lowestCommonAncestor1(root.left,p,q)
        else:
            return root