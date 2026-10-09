# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.greater = 0
        self.dfs(root)
        return root


    def dfs(self, node):
        if not node:
            return 

        self.dfs(node.right) # Right side first because BST has largest values on right side

        temp = node.val
        node.val += self.greater
        self.greater += temp

        self.dfs(node.left)

