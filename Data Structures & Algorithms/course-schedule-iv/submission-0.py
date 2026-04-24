class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        for prereq, course in prerequisites:
            adj_list[course].append(prereq)

        res = []
        for query in queries:
            res.append(self._dfs(query[1], query[0], adj_list, set()))

        return res

    def _dfs(self, prerequisite: int, course: int, adjacency_list:dict, visited:set) -> bool:
        if prerequisite in visited:
            return False

        if prerequisite == course:
            return True

        found = False
        visited.add(prerequisite)

        for neighbor in adjacency_list[prerequisite]:
            found = self._dfs(neighbor, course, adjacency_list, visited) or found

        return found
        

