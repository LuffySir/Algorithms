# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # dfs recursively
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root,0,res)
        return res

    def dfs(self,root,level,res):
        if root:
            if len(res)< level +1:
                res.insert(0,[])
            res[-(level+1)].append(root.val)
            self.dfs(root.left,level+1,res)
            self.dfs(root.right,level+1,res)

    # dfs + stack
    def levelOrderBottom1(self, root):
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res

    # bfs + queue
    def levelOrderBottom2(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res

