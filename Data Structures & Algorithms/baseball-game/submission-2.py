class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for op in operations:
            if op == "+":
                res = stack[-2] + stack[-1]
                stack.append(res)
                total += res
            elif op == "C":
                res = stack.pop()
                total -= res
            elif op == "D":
                res = stack[-1] * 2
                total += res
                stack.append(res)
            else:
                stack.append(int(op))
                total += int(op)
        
        return total