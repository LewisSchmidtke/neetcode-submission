# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        self.tree_map = {}
        self.valid = False
        self.dfs(root1, insert=True)
        self.dfs(root2, insert=False)
        return self.valid

    def dfs(self, node, insert):
        if not node:
            return

        missing = target - node.val

        if insert:
            self.tree_map[missing] = 1
        else:
            if node.val in self.tree_map:
                self.valid = True

        self.dfs(node.left, insert)
        self.dfs(node.right, insert)

        