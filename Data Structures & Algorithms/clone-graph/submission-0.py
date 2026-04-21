"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj_list = {}

        def dfs(n):
            if n in adj_list:
                return adj_list[n]
            
            new_node = Node(n.val)
            adj_list[n] = new_node

            for neighbor in n.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node

        return dfs(node) if node else None
        