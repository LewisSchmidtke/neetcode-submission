class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        adj_list = defaultdict(list)

        for index in range(len(pid)):
            adj_list[pid[index]].append(pid[index])

            if ppid[index] == 0:
                continue

            adj_list[ppid[index]].append(pid[index])
        
        return adj_list[kill]

            