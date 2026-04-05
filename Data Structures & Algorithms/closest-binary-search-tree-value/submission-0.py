# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.targ = target
        self.min_info = (root.val, abs(target - root.val))
        self.dfs(root)
        return self.min_info[0]

    def dfs(self, node):
        if not node:
            return

        dist = abs(node.val - self.targ)
        if dist < self.min_info[1]:
            self.min_info = (node.val, dist)
        
        if self.targ > node.val:
            self.dfs(node.right)
        
        else:
            self.dfs(node.left)