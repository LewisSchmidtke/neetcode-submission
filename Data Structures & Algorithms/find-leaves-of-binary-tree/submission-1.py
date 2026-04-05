# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.height_traversal(root)
        return self.res

    def height_traversal(self, node):

        if not node:
            return -1

        left = self.height_traversal(node.left)
        right = self.height_traversal(node.right)
        curr = max(left, right) + 1

        if len(self.res) == curr:
            self.res.append([]) # We add a new level
        
        self.res[curr].append(node.val)
        return curr




        