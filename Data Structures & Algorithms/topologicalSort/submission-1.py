class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        for src, destination in edges:            
            adj_list[src].append(destination) # Only append dest to source neighbors beause of directed graph
        
        rev_top_sort = []
        visited = set()
        path_set = set()
        for v in range(n):
            has_cycle = self.dfs(v, adj_list, visited, rev_top_sort, path_set)
            if has_cycle:
                return []

        top_sort = rev_top_sort[::-1]
        return top_sort
    
    def dfs(self, vertex: int, adjacency_list: dict, visited_set: set[int], topological_order: list, current_node_path: set):
        if vertex in current_node_path:
            return True
        if vertex in visited_set:
            return False
        
        visited_set.add(vertex)
        current_node_path.add(vertex)
        cycle = False
        for neighbor in adjacency_list[vertex]:
            cycle = self.dfs(
                neighbor, 
                adjacency_list, 
                visited_set, 
                topological_order, 
                current_node_path
                ) or cycle
        
        topological_order.append(vertex)
        current_node_path.remove(vertex)

        return cycle