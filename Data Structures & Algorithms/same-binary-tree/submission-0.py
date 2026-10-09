# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.compare(p, q)

    def compare(self, p,q):
        if p is None and q is None:
            return True

        if not p and q or p and not q:
            return False
        
        if p.val != q.val:
            return False
        else:
            return self.compare(p.left, q.left) and self.compare(p.right, q.right)
