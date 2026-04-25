class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        adj_list = defaultdict(list)

        for index in range(len(pid)):
            adj_list[pid[index]].append(pid[index])

            if ppid[index] == 0:
                continue

            adj_list[ppid[index]].append(pid[index])
        
        r = []
        self.dfs(kill, adj_list, r, set())
        return r

    def dfs(self, node, adj, res, visited):
        if node in visited:
            return
        
        visited.add(node)
        res.append(node)

        for neighbor in adj[node]:
            self.dfs(neighbor, adj, res, visited)

            