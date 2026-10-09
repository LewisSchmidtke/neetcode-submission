class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        for prereq, course in prerequisites:
            adj_list[course].append(prereq)

        res = []
        prereq_cache = defaultdict(set)
        for pre, course in queries:
            if pre in prereq_cache[course]:
                res.append(True)
            else:
                res.append(self._dfs(pre, course, adj_list, set(), prereq_cache))

        return res



    def _dfs(self, course: int, prerequisite: int, adjacency_list:dict, visited:set, cache) -> bool:
        if prerequisite in cache[course]:
            return True

        if prerequisite in visited:
            return False

        if prerequisite == course:
            return True

        found = False
        visited.add(prerequisite)
        cache[course].add(prerequisite)

        for neighbor in adjacency_list[prerequisite]:
            found = self._dfs(course, neighbor, adjacency_list, visited, cache) or found

        return found
        

