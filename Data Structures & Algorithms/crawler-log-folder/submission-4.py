class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0

        for log in logs:
            if log[0] != ".":
                count += 1
            elif log[1] == ".":
                if count > 0:
                    count -= 1
            
        return count