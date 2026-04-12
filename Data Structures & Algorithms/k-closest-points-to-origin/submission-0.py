import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.calc_distance(point), point) for point in points]
        res = []
        heapq.heapify(distances)

        for _ in range(k):
            res.append(heapq.heappop(distances)[1])

        return res
    
    def calc_distance(self, point: List[int]) -> float:
        dist_to_origin = ((0 - point[0])**2 + (0 - point[1])**2)**0.5
        return dist_to_origin