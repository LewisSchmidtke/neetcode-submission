"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque

        q = deque()

        if root:
            q.append(root)

        while len(q) > 0:
            length = len(q)
            copy_q = q.copy()
            for index in range(length):
                curr = q.popleft()

                curr.next = copy_q[index + 1] if index + 1 < len(copy_q) else None

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        return root

