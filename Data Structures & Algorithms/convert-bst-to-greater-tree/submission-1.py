# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ################### Recursion ########### Recursion Error for large operations
        #self.greater = 0

        # def dfs(node):
        #    if not node:
        #        return 

        #    dfs(node.right) # Right side first because BST has largest values on right side

        #    self.greater += node.val
        #    node.val = self.greater

        #    dfs(node.left)

        #dfs(root)
        #return root

        ##########################################
        ############## Iterative #################

        stack = []
        greater = 0
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.right

            node = stack.pop()
            greater += node.val
            node.val = greater
            node = node.left

        return root

