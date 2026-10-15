class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []

        for c in s:
            if c not in mapping:
                stack.append(c)
            else:
                if not stack or (stack and mapping[c] != stack[-1]):
                    return False
                if stack:
                    stack.pop()
        
        return len(stack) == 0
