"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        return self.clone(root)

    def clone(self, node):
        if not node:
            return node
        
        new_node = Node(node.val)

        for child in node.children:
            new_node.children.append(self.clone(child))
        
        return new_node