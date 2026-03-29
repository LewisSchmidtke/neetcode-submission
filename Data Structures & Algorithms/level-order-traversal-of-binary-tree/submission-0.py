# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque()
        q.append([root])

        res = []

        while q:
            nodes = q.popleft()
            print(nodes)

            if not nodes:
                continue

            level_nodes = []
            level_vals = []
            for node in nodes:
                if not node:
                    continue

                level_vals.append(node.val)

                if node.left:
                    level_nodes.append(node.left)
                if node.right:
                    level_nodes.append(node.right)
                    
            if level_vals:
                res.append(level_vals)

            if level_nodes:
                q.append(level_nodes)

        return res