# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.range_sum = 0
        self.dfs(root)
        return self.range_sum

    def dfs(self, node):
        if not node:
            return

        if self.low <= node.val <= self.high:
            self.range_sum += node.val

        if node.val > high:
            self.dfs(node.left)
            return
        if node.val < low:
            self.dfs(node.right)
            return
            
        self.dfs(node.left)
        self.dfs(node.right)
    