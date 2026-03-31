# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        from collections import defaultdict

        q = deque()
        col_map = defaultdict(list)

        if root:
            q.append((root, 0))

        while len(q) > 0:
            for _ in range(len(q)):
                node, col = q.popleft()

                col_map[col].append(node.val)

                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        vert_traversal = sorted(list(col_map.items()))
        vert_traversal_vals = [x[1] for x in vert_traversal]
        
        return vert_traversal_vals

            
