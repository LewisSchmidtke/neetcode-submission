# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root1 = self.dfs(root1, root2)

        return root1

    def dfs(self, r1, r2):
        if not r1:
            return r2

        if not r2:
            return r1

        r1.val = r1.val + r2.val

        r1.left = self.dfs(r1.left, r2.left)
        r1.right = self.dfs(r1.right, r2.right)

        return r1