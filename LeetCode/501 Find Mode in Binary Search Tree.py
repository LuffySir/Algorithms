# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

# Assume a BST is defined as follows:

from collections import Counter

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 超时
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        count = Counter()
        res = self.helper(count, root)
        return res

    def helper(self, count, root):

        if root:
            count[root.val] += 1
            self.helper(count, root.left)
            self.helper(count, root.right)

        max_ct = max(count.itervalues())
        return [k for k,v in count.iteritems() if v == max_ct]


from collections import defaultdict

class Solution1(object):
    def helper(self, root, cache):
        if root == None:
            return
        cache[root.val] += 1
        self.helper(root.left, cache)
        self.helper(root.right, cache)
        return

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        cache = defaultdict(int)
        self.helper(root, cache)
        max_freq = max(cache.values())
        result = [k for k, v in cache.items() if v == max_freq]
        return result




