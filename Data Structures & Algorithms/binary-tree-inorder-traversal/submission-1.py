# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        return self.traverse(root, res)

    def traverse(self, node, val_list):
        if not node:
            return []
        
        # val_list.append(node.val) # Pre order
        self.traverse(node.left, val_list)

        val_list.append(node.val) # In Order

        self.traverse(node.right, val_list)

        # val_list.append(node.val) # post order

        return val_list



        
        
        


