# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        def calc_depth(root, counter):
            if root is None:
                return counter

            counter += 1 # Because its not None we found another Node
            left = calc_depth(root.left, counter)
            right = calc_depth(root.right, counter)
            counter = max(left, right)
            return counter

        return max(calc_depth(root.left, depth), calc_depth(root.right, depth))
