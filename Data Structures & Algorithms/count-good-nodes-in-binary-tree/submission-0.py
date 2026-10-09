# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.max_v = root.val
        self.count = 0
        self.dfs(root)
        return self.count

    def dfs(self, node):
        if not node:
            return None

        if node.val >= self.max_v:
            self.count += 1

        self.max_v = max(self.max_v, node.val)

        self.dfs(node.left)
        self.dfs(node.right)