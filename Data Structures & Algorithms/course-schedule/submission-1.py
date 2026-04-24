class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for source, destination in prerequisites:
            adj_list[source].append(destination)

        visited_set = set()
        current_path = set()
        for vert in range(numCourses):
            if self._dfs(vert, adj_list, visited_set, current_path):
                return False
        
        return True

    def _dfs(self, vertex, adjacency, visited, path):
        if vertex in path:
            return True
        
        if vertex in visited:
            return False

        visited.add(vertex)
        path.add(vertex)
        cycle = False

        for neighbor in adjacency[vertex]:
            cycle = self._dfs(neighbor, adjacency, visited, path) or cycle
        
        path.remove(vertex)
        return cycle
        
