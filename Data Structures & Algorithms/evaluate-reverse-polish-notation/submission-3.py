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
            if token in char_map:
                b = stack.pop()
                a = stack.pop()
                stack.append(char_map[token](a, b))
            else:
                stack.append(int(token))

        return stack[-1]
