class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        mst_weight = 0
        adj_list = defaultdict(list)
        for src, dest, weight in edges:
            adj_list[src].append((weight, dest))
            adj_list[dest].append((weight, src))

        min_heap = [(0, 0)] # start at node 0, with cost 0+
        heapq.heapify(min_heap)
        visited = set()

        while min_heap and len(visited) < n: # number of edges in MST must be n - 1
            curr_cost, curr_node = heapq.heappop(min_heap)
            if curr_node in visited:
                continue
            mst_weight += curr_cost
            
            visited.add(curr_node)

            for weight, neighbor in adj_list[curr_node]:
                if neighbor in visited:
                    continue
                heapq.heappush(min_heap, (weight, neighbor))

        return mst_weight if len(visited) == n else -1
