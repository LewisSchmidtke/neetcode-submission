class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

        def multiply(a, b):
            return a * b

        def divide(a, b):
            return int(a / b)

        char_map = {
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide
        }

        
        stack = []

        for token in tokens:
            if token.isnumeric():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(char_map[token](a, b))

        return stack[-1]
