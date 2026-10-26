# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)
    def dfs(self, one, two):
        if not one and two or one and not two:
            return False
        
        if not one and not two:
            return True
        
        if one.val != two.val:
            return False

        valid = self.dfs(one.left, two.left) and self.dfs(one.right, two.right)
        return valid