class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for course, prerequisite in prerequisites:
            adj_list[course].append(prerequisite)

        top_sort = []
        visited = set()
        curr_path = set()

        for course in range(numCourses):
            has_cycle = self._dfs(course, adj_list, visited, curr_path, top_sort)
            if has_cycle:
                return []
        
        return top_sort # No need to reverse top_sort due to the nature of course -> prerequisite graph direction

    def _dfs(self, vertex:int, adjacency_list:dict, visit_set:set, path_set:set, topological_list:List) -> bool:
        if vertex in path_set:
            return True
        
        if vertex in visit_set:
            return False

        visit_set.add(vertex)
        path_set.add(vertex)

        cycle = False
        for neighbor in adjacency_list[vertex]:
            cycle = self._dfs(neighbor, adjacency_list, visit_set, path_set, topological_list) or cycle

        topological_list.append(vertex)
        path_set.remove(vertex)

        return cycle
