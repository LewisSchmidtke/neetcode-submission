# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.counter = 0
        self.dfs(root)
        return self.counter

    def dfs(self, node):
        if not node:
            return True

        is_left_uni = self.dfs(node.left)
        is_right_uni = self.dfs(node.right)

        if is_left_uni and is_right_uni:
            if node.left and node.val != node.left.val:
                return False
            if node.right and node.val != node.right.val:
                return False

            self.counter += 1

            return True

        return False

