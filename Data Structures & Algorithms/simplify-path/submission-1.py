class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]
        right = 1

        while right < len(path):
            # With normal letters we dont do anything
            if path[right].isalnum() or path[right] == "_":
                stack.append(path[right])
            # if we get a leading / we pop from stack to merge multiple / into one
            elif path[right] == "/":
                while stack and stack[-1] == "/":
                    stack.pop()
                stack.append("/")
            # Else case for dots: .
            else:
                dot_count = 0
                while right < len(path) and path[right] == ".":
                    dot_count += 1
                    right += 1
                if dot_count == 1 and path[right] == "/": 
                    pass
                elif dot_count == 2 and path[right] == "/":
                    stack.pop()
                    while stack and stack[-1] != "/":
                        stack.pop()
                else:
                    curr_path = "." * dot_count
                    stack.append(curr_path)
                    stack.append("/")
            
            right += 1

        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        
        if not stack:
            stack = ["/"]

        return "".join(stack)

