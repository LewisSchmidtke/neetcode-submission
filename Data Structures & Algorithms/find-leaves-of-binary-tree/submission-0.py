# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        while root:
            leaves = []
            root = self.dfs(root, leaves)
            self.res.append(leaves)
        
        return self.res

    def dfs(self, node, r):
        if not node:
            return None

        if not node.left and not node.right:
            r.append(node.val)
            return None
            
        node.left = self.dfs(node.left, r)
        node.right = self.dfs(node.right, r)

        return node




        