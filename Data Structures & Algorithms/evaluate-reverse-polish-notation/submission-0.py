class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        
        result_stack = []

        for character in tokens:
            if character.isnumeric():
                result_stack.append(int(character))
            else:
                value_2 = result_stack.pop()
                value_1 = result_stack.pop()
                print(value_2, value_1)
                if character == "+":
                    result = value_2 + value_1
                elif character == "-":
                    result = value_2 - value_1
                elif character == "*":
                    result = value_2 * value_1
                elif character == "/":
                    result = value_2 / value_1

                result_stack.append(int(result))
        
        return result_stack[0]