# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def move(node):
            if not node:
                return None
            
            move(node.left)
            res.append(node.val)
            move(node.right)
            
        move(root)

        return res


