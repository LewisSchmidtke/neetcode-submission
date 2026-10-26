class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid = {"+", "-", "/", "*"}
        for tok in tokens:
            if tok not in valid:
                stack.append(int(tok))
            else:
                second = stack.pop()
                first = stack.pop()
                if tok == "+":
                    res = first + second
                elif tok == "-":
                    res = first - second
                elif tok == "/":
                    res = int(first / second)
                elif tok == "*":
                    res = first * second
                stack.append(res)

        return stack[0]
