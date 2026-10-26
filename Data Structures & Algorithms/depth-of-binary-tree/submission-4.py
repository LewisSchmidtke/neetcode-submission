# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
        
    def dfs(self, r, count):
        if not r:
            return count
        
        count = max(self.dfs(r.left, count + 1), self.dfs(r.right, count + 1))
        return count