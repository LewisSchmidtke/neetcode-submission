# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, node, max_v):
        if not node:
            return 0

        res = 1 if node.val >= max_v else 0

        max_v = max(max_v, node.val)

        res += self.dfs(node.left, max_v)
        res += self.dfs(node.right, max_v)

        return res