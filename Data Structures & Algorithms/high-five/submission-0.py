class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        res = []

        items.sort(key=lambda x: (x[0], -x[1]))
    
        pointer = 0

        while pointer < len(items):
            student = items[pointer][0]
            top_5 = items[pointer:pointer + 5]
            scores = [x[1] for x in top_5]

            r = [student, sum(scores) // 5]
            res.append(r)
            pointer += 5
            while pointer < len(items) and items[pointer][0] == student:
                pointer += 1

        return res

