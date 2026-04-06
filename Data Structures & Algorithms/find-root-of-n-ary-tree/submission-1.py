"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        from collections import defaultdict
        
        d = defaultdict(int)

        for n in tree:
            d[n] += 1

            for child in n.children:
                d[child] += 1

        for key, value in d.items():
            if value == 1:
                return key
                
            
        