class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for det in details:
            age = int(det[11:13])
            if age > 60:
                seniors += 1

        return seniors