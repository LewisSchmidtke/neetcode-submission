class Solution:
    def parseTernary(self, expression: str) -> str:
        point = len(expression) - 1
        stack = []

        while point >= 0:
            c = expression[point]
            if point == len(expression) - 1:
                stack.append(c)
                point -= 1
                continue

            if c == ':':
                stack.append(expression[point - 1])

            elif c == '?':
                if expression[point - 1] == 'F':
                    stack.pop() 

            point -= 2

        return stack[-1]
