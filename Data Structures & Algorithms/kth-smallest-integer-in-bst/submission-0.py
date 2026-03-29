# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val_list = []
        return self.dfs(root, val_list)[k - 1]

    def dfs(self, node, vals):
        if not node:
            return []
        
        self.dfs(node.left, vals)
        vals.append(node.val)
        self.dfs(node.right, vals)

        return vals