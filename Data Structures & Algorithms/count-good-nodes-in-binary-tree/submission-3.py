# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        path_counter = defaultdict(int)
        self._dfs(root, path_counter)
        return self.count


    def _dfs(self, node: TreeNode, path_set: set) -> None:
        if not node:
            return None
        
        if not path_set or (path_set and node.val >= max(path_set)):
            self.count += 1
        
        path_set[node.val] += 1

        self._dfs(node.left, path_set)
        self._dfs(node.right, path_set)

        path_set[node.val] -= 1