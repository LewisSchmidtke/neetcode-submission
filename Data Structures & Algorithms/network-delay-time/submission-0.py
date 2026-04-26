class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res_map = {x : -1 for x in range(1, n + 1)}

        adj_map = defaultdict(list)
        for src, dest, time in times:
            adj_map[src].append((time, dest))

        min_heap = [(0, k)] # time, node
        heapq.heapify(min_heap)
        visited = set()

        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            visited.add(node)

            if res_map[node] == -1 or res_map[node] > cost:
                res_map[node] = cost

            for n_time, n_node in adj_map[node]:
                heapq.heappush(min_heap, (n_time + cost, n_node))

        network_times = res_map.values()
        
        return -1 if min(network_times) == -1 else max(network_times)

        
            

            