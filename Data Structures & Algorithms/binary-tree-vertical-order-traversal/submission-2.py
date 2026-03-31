# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        from collections import defaultdict
        min_col = max_col = 0

        q = deque()
        col_map = defaultdict(list)
        q.append((root, 0))

        while len(q) > 0:
            for _ in range(len(q)):
                node, col = q.popleft()
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                
                col_map[col].append(node.val)

                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        res = []

        for k in range(min_col, max_col + 1):
            res.append(col_map[k])
        
        return res
        # vert_traversal = sorted(list(col_map.items()))
        # vert_traversal_vals = [x[1] for x in vert_traversal]
        
        # return vert_traversal_vals

            
