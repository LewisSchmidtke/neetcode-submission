class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            if not stack or ast > 0:
                stack.append(ast)
                continue
            
            if stack[-1] < 0:
                stack.append(ast)
                continue

            destroyed = False
            while stack and ast and stack[-1] > 0:
                prior_ast = stack.pop()
                if abs(prior_ast) > abs(ast):
                    stack.append(prior_ast)
                    destroyed = True
                    break
                elif abs(prior_ast) == abs(ast):
                    destroyed = True
                    break

            if not destroyed:
                stack.append(ast)
        
        return stack
            