class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {}
        visited = set()
        count = 0

        for src, dest in edges:
            if src not in adj_list:
                adj_list[src] = set()
            if dest not in adj_list:
                adj_list[dest] = set()
            adj_list[src].add(dest)
            adj_list[dest].add(src)

        for src, _ in edges:
            if src not in visited:
                count += 1
                self.dfs(src, visited, adj_list)
        
        return count

    def dfs(self, s, visited, adj):
        if s in visited:
            return
        
        visited.add(s)
        for neighbor in adj[s]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, adj)
        
        return
