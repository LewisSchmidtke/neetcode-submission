class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        shortest_path_map = {x : -1 for x in range(n)}

        adj_list = defaultdict(list)
        for source, destination, cost in edges:
            adj_list[source].append((cost, destination))

        min_heap = [(0, src)] # (Cost, Node)
        visited = set()
        while min_heap:
            current_cost, current_node = heapq.heappop(min_heap)

            if current_node in visited:
                continue

            visited.add(current_node)

            if shortest_path_map[current_node] == -1 or shortest_path_map[current_node] > current_cost:
                shortest_path_map[current_node] = current_cost
            for cost, neighbor in adj_list[current_node]:
                heapq.heappush(min_heap, (current_cost + cost, neighbor))

        return shortest_path_map

