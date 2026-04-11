from collections import defaultdict
import heapq

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        score_map = defaultdict(list)

        for score in items:
            score_map[score[0]].append(score[1])

        res = []

        for student, score_list in score_map.items():
            heapq.heapify(score_list)

            while len(score_list) > 5:
                heapq.heappop(score_list)

            res.append([student, sum(score_list) // 5])

        return sorted(res)



