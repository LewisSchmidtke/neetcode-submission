class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_map = defaultdict(list)
        res = []

        for data in items:
            student_map[data[0]].append(data[1])

        for student, score_list in student_map.items():
            heapq.heapify_max(score_list)
            total = 0
            for _ in range(5):
                total += heapq.heappop_max(score_list)
            
            res.append([student, total //5])

        return sorted(res)


