# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        q = deque()
        res = []
        lvl = 0

        if root:
            q.append(root)

        while len(q) > 0:
            length = len(q)
            is_odd = lvl % 2 != 0
            pointer = length - 1 if is_odd else 0

            level_vals = [0] * length

            for _ in range(length):
                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

                level_vals[pointer] = curr.val

                if is_odd:
                    pointer -= 1
                else:
                    pointer += 1

            res.append(level_vals)   
            lvl += 1   

        return res  