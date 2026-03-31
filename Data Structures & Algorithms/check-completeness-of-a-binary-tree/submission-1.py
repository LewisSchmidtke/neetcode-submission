# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        from collections import deque

        q = deque()
        q.append((root, 0))
        level = 0

        while len(q) > 0:
            level_size = 2 ** level
            place = 0
            level_cols = []
            for _ in range(len(q)):
                level_size -= 1
                curr, p = q.popleft()

                level_cols.append(p)

                if curr.left:
                    q.append((curr.left, place))
                place += 1
                if curr.right:
                    q.append((curr.right, place))
                place += 1

            if q and level_size != 0: # We have another level and the current level is not complete
                return False
            
            if not q: # We have processed last level currently
                if level_size == 0: # Fully complete level
                    return True

                prev = None
                for index, val in enumerate(level_cols):
                    if index != val:
                        return False
                    if prev is None:
                        prev = val
                        continue

                    if val - 1 != prev:
                        return False
                    prev = val
        
            level += 1

        return True

