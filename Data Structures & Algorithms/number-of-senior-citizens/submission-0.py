class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        threshold = 60

        for person in details:
            age = int(person[11:13])
            if age > threshold:
                seniors += 1

        return seniors