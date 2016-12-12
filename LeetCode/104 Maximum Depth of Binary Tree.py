# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Recursively
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# # DFS
# def maxDepth(self, root):
#     res = 0
#     stack = [(root, 0)]
#     while stack:
#         node, level = stack.pop()
#         if not node:
#             res = max(res, level)
#         else:
#             stack.append((node.right, level + 1))
#             stack.append((node.left, level + 1))
#     return res


# # BFS + deque
# def maxDepth(self, root):
#     """
#     :type root: TreeNode
#     :rtype: int
#     """
#     # use BFS with iterative
#     # BFS + deque
#     if not root:
#         return 0
#     queue = collections.deque([(root, 1)])  # here the 2nd number is level
#     while queue:
#         curr, val = queue.popleft()
#         if curr.left:
#             queue.append((curr.left, val + 1))
#         if curr.right:
#             queue.append((curr.right, val + 1))
#     return val
