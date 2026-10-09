# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.remove_node(root, key)

    def find_min(self, root_n):
        curr = root_n
        while curr and curr.left:
            curr = curr.left
        return curr.val

    def remove_node(self, root_n, val):
        if not root_n:
            return None
            
        if val < root_n.val:
            root_n.left = self.remove_node(root_n.left, val)
        elif val > root_n.val:
            root_n.right = self.remove_node(root_n.right, val)
        else:
            if not root_n.left:
                return root_n.right
            elif not root_n.right:
                return root_n.left
            else:
                min_val = self.find_min(root_n.right)
                root_n.val = min_val
                root_n.right = self.remove_node(root_n.right, min_val)
        
        return root_n