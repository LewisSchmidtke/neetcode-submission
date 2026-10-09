class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        running_sum = 0
        
        for op in operations:
            print(stack)
            if op == "+":
                val2 = stack.pop()
                calc = stack[-1] + val2
                stack.append(val2)
                stack.append(calc)
                running_sum += calc
            elif op == "C":
                val = stack.pop()
                running_sum -= val
            elif op == "D":
                calc = stack[-1] * 2
                stack.append(calc)
                running_sum += calc
            else:
                stack.append(int(op))
                running_sum += int(op)
        
        return running_sum