class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        visited = set()
        count = 0

        for src, dest in edges:
            adj_list[src].add(dest)
            adj_list[dest].add(src)

        for node in range(n):
            if node not in visited:
                count += 1
                self.dfs(node, visited, adj_list)

        return count

    def dfs(self, n, visited, adj):
        if n in visited:
            return
            
        visited.add(n)
        for neighbor in adj[n]:
            self.dfs(neighbor, visited, adj)
        
