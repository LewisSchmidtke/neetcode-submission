"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def move(node):
            if node is None:
                return None
            
            for child in node.children:
                move(child)
            
            res.append(node.val)


        move(root)

        return res