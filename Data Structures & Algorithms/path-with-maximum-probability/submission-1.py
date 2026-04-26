class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # len(edges) = len(succProb)
        # minimum 2 nodes in graph
        # no single node cycle
        # Single edge between two nodes
        # Start != end
        # Start and end in nodes

        adj_list = defaultdict(list)
        for index, nodes in enumerate(edges):
            n1, n2 = nodes
            adj_list[n1].append((succProb[index], n2))
            adj_list[n2].append((succProb[index], n1))

        # Use max heap to find the likeliest path with dijktras

        max_heap = [(1, start_node)]
        heapq.heapify_max(max_heap)
        visited = set()

        while max_heap:
            current_prob, current_node = heapq.heappop_max(max_heap)

            if current_node in visited:
                continue
            visited.add(current_node)
            
            if current_node == end_node:
                return current_prob

            for prob, neighbor in adj_list[current_node]:
                if neighbor in visited:
                    continue

                heapq.heappush_max(max_heap, (current_prob * prob, neighbor))

        return 0


