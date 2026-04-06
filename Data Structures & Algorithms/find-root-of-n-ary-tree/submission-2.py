"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        self.max_depth = 0
        self.root = None
        for n in tree:
            depth = self.dfs(n)
            if depth > self.max_depth:
                self.max_depth = depth
                self.root = n

        return self.root
            
    
    def dfs(self, node):
        if not node:
            return 0
        
        max_child_depth = 0
        
        for child in node.children:
            max_child_depth = max(max_child_depth, self.dfs(child))
        
        return max_child_depth + 1
                
            
        